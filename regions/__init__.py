from constants import *
from PIL import Image
import pyautogui as ui
import imagehash
import pytesseract

def isolate_white(pixel):
    if all(channel >= 225 for channel in pixel):
        return (255, 255, 255)
    else:
        return (0, 0, 0)

def image_difference(a: Image, b: Image):
    ahash = imagehash.average_hash(a)
    bhash = imagehash.average_hash(b)
    return ahash - bhash

class Region:
    name = ""
    x = 0
    y = 0
    width = 0
    height = 0
    image = None

    cached = None

    def click(self):
        if self.image:
            print(f"Checking image of {self.id}...")

            reference = Image.open(self.image)
            subject = ui.screenshot(region=self.compact())
            difference = image_difference(reference, subject)

            if difference > 5:
                print(f"You are not clicking {self.id}!! {{ difference: {difference} }}")
                exit()

        ui.leftClick(self.x + self.width / 2, self.y + self.height / 2)

    def read(self):
        screenshot = ui.screenshot(region=self.compact()).convert("RGB")
        processed = Image.new("RGB", screenshot.size)
        processed.putdata([isolate_white(pixel) for pixel in screenshot.getdata()])
        return pytesseract.image_to_string(processed, config="--psm 7")

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