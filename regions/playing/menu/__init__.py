from regions import Region
from regions.playing.menu.button import ButtonRegion
from regions.playing.menu.end_button import EndButtonRegion
class MenuRegion(Region):
    id = "playing.menu"
    x = 658
    y = 2
    width = 128
    height = 350

    shop = ButtonRegion(0)
    toggle = ButtonRegion(1)
    missions = ButtonRegion(4)
    settings = ButtonRegion(5)
    cards = ButtonRegion(6)
    labs = ButtonRegion(7)
    event = ButtonRegion(8)
    modules = ButtonRegion(9)
    end_button = EndButtonRegion()

    def __init__(self):
        for key in dir(self):
            value = getattr(self, key)
            if isinstance(value, ButtonRegion):
                if key != "toggle":
                    value.id = f"playing.menu.{key}"
                    value.image = __file__.replace("__init__.py", f"{key}.png")
