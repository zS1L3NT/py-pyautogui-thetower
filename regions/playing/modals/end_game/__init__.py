from regions import Region
from regions.playing.modals.end_game.no_button import NoButtonRegion
from regions.playing.modals.end_game.yes_button import YesButtonRegion

class EndGameRegion(Region):
    id = "playing.modals.end_game"
    x = 168
    y = 354
    width = 448
    height = 346

    no_button = NoButtonRegion()
    yes_button = YesButtonRegion()