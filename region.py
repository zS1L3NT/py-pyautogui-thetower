from constants import *
from utilities.parser import Parser, ValueType
from PIL import Image
import pyautogui as ui
import imagehash
import pytesseract # type: ignore
import time
import os

class Region:
    id = ""
    x = 0
    y = 0
    width = 0
    height = 0
    image = None

    cached = None

    def difference(self, reference: Image.Image) -> int:
        subject = ui.screenshot(region = self.compact())

        rhash = imagehash.average_hash(reference) # type: ignore
        shash = imagehash.average_hash(subject) # type: ignore

        return rhash - shash

    def is_present(self, acceptable_difference: int = 5):
        if self.image:
            # print(f"[RID: {self.id}] >>> Checking if element is visible...")

            difference = self.difference(Image.open(self.image))

            if difference > acceptable_difference:
                # print(f"[RID: {self.id}] <<< Element is not present, difference is too large: {difference}")
                return False
            else:
                # print(f"[RID: {self.id}] <<< Element is present, difference is small enough: {difference}")
                return True
        else:
            raise Exception(f"Cannot check {self.id} without image")

    def click(self):
        if self.image and not self.is_present():
            folder_name = os.path.join("errors", time.strftime("%Y-%m-%d_%H-%M-%S"))
            os.mkdir(folder_name)

            ui.screenshot().save(os.path.join(folder_name, f"screenshot.png"))
            ui.screenshot(region = self.compact()).save(os.path.join(folder_name, f"region.png"))
            with open(os.path.join(folder_name, "log.txt"), "w") as file:
                file.write("\n".join([
                    f"x: {self.x}",
                    f"y: {self.y}",
                    f"width: {self.width}",
                    f"height: {self.height}",
                ]))

            raise Exception(f"Element is not present, cannot click!")

        # print(f"[RID: {self.id}] Clicking...")
        ui.leftClick(self.x + self.width / 2, self.y + self.height / 2)

    def read(
        self,
        type: ValueType = ValueType.NUMBER,
        simplify_colors: bool = False,
    ):
        config = "--psm 7"
        if type.characters() is not None:
            config += f" -c tessedit_char_whitelist=\"{type.characters()}\""

        for _ in range(5):
            # print(f"[RID: {self.id}] >>> Reading with config \"{config}\" ({i + 1}/{retries})")

            image = ui.screenshot(region = self.compact()).convert("RGB")
            pixels: list[tuple[int, int, int]] = list(image.getdata()) # type: ignore
            processed = Image.new("RGB", image.size)
            processed.putdata([ # type: ignore
                (255, 255, 255) if all(channel >= 225 for channel in pixel) else (0, 0, 0) \
                if simplify_colors else pixel for pixel in pixels
            ])

            string = str(pytesseract.image_to_string(processed, config = config)).strip() # type: ignore

            # print(f"[RID: {self.id}] OCR result: \"{string}\", parsing as {type.name}")

            value = Parser(string).type(type)
            if value is None:
                # print(f"[RID: {self.id}] ❔ Failed to parse \"{string}\" as {type.name}, retrying...")
                continue

            # print(f"[RID: {self.id}] <<< Parsed OCR result: {value}")
            return value

        # print(f"[RID: {self.id}] ❌ Failed to parse OCR result after 5 retries!!!")

    def cascade(self):
        properties = [getattr(self, key) for key in dir(self)]
        regions = [region for region in properties if isinstance(region, Region)]

        for region in regions:
            region.x += self.x
            region.y += self.y

        for region in regions:
            region.cascade()
    
    def preview(self, name: str = "preview"):
        ui.screenshot(region = self.compact()).save(f"{name}.png")

    def compact(self):
        return (self.x, self.y, self.width, self.height)

    def __str__(self):
        return f"{self.id} {{ x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height} }}"