from constants import *
from telegram.api import TelegramAPI
from typing import Callable
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

    def difference(self, reference: Image.Image) -> int:
        subject = ui.screenshot(region = self.compact())

        rhash = imagehash.average_hash(reference) # type: ignore
        shash = imagehash.average_hash(subject) # type: ignore

        return rhash - shash

    def is_present(self, acceptable_difference: int = 5):
        if self.image:
            return self.difference(Image.open(self.image)) <= acceptable_difference
        else:
            raise Exception(f"Cannot check {self.id} without image")

    def click(self):
        if self.image and not self.is_present():
            folder_name = os.path.join("logs", "images", time.strftime("%Y-%m-%d %H-%M-%S"))
            os.mkdir(folder_name)

            ui.screenshot().save(os.path.join(folder_name, "screenshot.png"))
            os.system(f"cp \"{self.image}\" \"{os.path.join(folder_name, "expected.png")}\"")
            ui.screenshot(region = self.compact()).save(os.path.join(folder_name, "actual.png"))

            with open(os.path.join(folder_name, "info.log"), "w") as file:
                file.write("\n".join([
                    f"region: {self.id}",
                    f"x: {self.x}",
                    f"y: {self.y}",
                    f"width: {self.width}",
                    f"height: {self.height}",
                ]))
            
            TelegramAPI.send_media_group([
                ("photo", "Screenshot", os.path.join(folder_name, "screenshot.png")),
                ("photo", "Expected", os.path.join(folder_name, "expected.png")),
                ("photo", "Actual", os.path.join(folder_name, "actual.png")),
            ])

            raise Exception(f"Element is not present, cannot click!")

        ui.leftClick(self.x + self.width / 2, self.y + self.height / 2)

    def read(
        self,
        type: ValueType = ValueType.NUMBER,
        is_valid: Callable[[tuple[float, float] | str | float | None], bool] = lambda _: True,
        simplify_colors: bool = False,
    ):
        config = "--psm 7"
        if type.characters() is not None:
            config += f" -c tessedit_char_whitelist=\"{type.characters()}\""

        for _ in range(5):
            image = ui.screenshot(region = self.compact()).convert("RGB")
            pixels: list[tuple[int, int, int]] = list(image.getdata()) # type: ignore
            processed = Image.new("RGB", image.size)
            processed.putdata([ # type: ignore
                (255, 255, 255) if all(channel >= 225 for channel in pixel) else (0, 0, 0) \
                if simplify_colors else pixel for pixel in pixels
            ])

            string = str(pytesseract.image_to_string(processed, config = config)).strip() # type: ignore

            value = Parser(string).type(type)
            if value is None:
                continue

            if not is_valid(value):
                continue

            return value

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