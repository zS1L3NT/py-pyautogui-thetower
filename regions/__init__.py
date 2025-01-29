from typing import Callable
from constants import *
from utilities.parser import Parser, ValueType
from PIL import Image
import pyautogui as ui
import imagehash
import pytesseract

def isolate_white(pixel: tuple[int, int, int]):
    if all(channel >= 225 for channel in pixel):
        return (255, 255, 255)
    else:
        return (0, 0, 0)

class Region:
    id = ""
    x = 0
    y = 0
    width = 0
    height = 0
    image = None

    cached = None

    def difference(self, reference: Image):
        subject = ui.screenshot(region=self.compact())

        rhash = imagehash.average_hash(reference)
        shash = imagehash.average_hash(subject)

        return rhash - shash

    def is_present(self, acceptable_difference = 5):
        if self.image:
            print(f"[RID: {self.id}] >>> Checking if element is visible...")

            difference = self.difference(Image.open(self.image))

            if difference > acceptable_difference:
                print(f"[RID: {self.id}] <<< Element is not present, difference is too large: {difference}")
                return False
            else:
                print(f"[RID: {self.id}] <<< Element is present, difference is small enough: {difference}")
                return True
        else:
            raise Exception(f"Cannot check {self.id} without image")

    def click(self):
        if self.image and not self.is_present():
            raise Exception(f"Element is not present, cannot click!")

        print(f"[RID: {self.id}] Clicking...")
        ui.leftClick(self.x + self.width / 2, self.y + self.height / 2)

    def read(
        self,
        type = ValueType.NUMBER,
        process_image = True,
        retries = 5,
        is_valid: Callable[[any], bool] = lambda _: True,
        psm = 7,
        characters = None,
    ):
        config = " ".join([
            value for value in [ # type: ignore
                f"--psm {psm}",
                f"-c tessedit_char_whitelist=\"{characters}\"" if characters else None
            ] if value is not None
        ])

        for i in range(retries):
            print(f"[RID: {self.id}] >>> Reading with config \"{config}\" ({i + 1}/{retries})")

            image = ui.screenshot(region=self.compact()).convert("RGB")
            processed = Image.new("RGB", image.size)
            processed.putdata([isolate_white(pixel) if process_image else pixel for pixel in image.getdata()]) # type: ignore

            string = str(pytesseract.image_to_string(processed, config=config)).strip()

            print(f"[RID: {self.id}] OCR result: \"{string}\", parsing and validating as {type.name}")

            value = Parser(string).type(type)
            if not value:
                print(f"[RID: {self.id}] ❔ Failed to parse \"{string}\" as {type.name}, retrying...")
                continue
            
            if not is_valid(value):
                print(f"[RID: {self.id}] ❔ Value deemed as invalid by caller, retrying...")
                continue

            print(f"[RID: {self.id}] <<< Parsed and Validated OCR result: {value}")
            return value

        print(f"[RID: {self.id}] ❌ Failed to parse and validate OCR result after {retries} retries!!!")

    def cascade(self):
        properties = [getattr(self, key) for key in dir(self)]
        regions = [region for region in properties if isinstance(region, Region)]

        for region in regions:
            region.x += self.x
            region.y += self.y

        for region in regions:
            region.cascade()
    
    def preview(self, name = "preview"):
        ui.screenshot(region=self.compact()).save(f"{name}.png")

    def compact(self):
        return (self.x, self.y, self.width, self.height)

    def __str__(self):
        return f"{self.id} {{ x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height} }}"