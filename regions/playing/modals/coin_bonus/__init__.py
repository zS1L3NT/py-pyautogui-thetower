from region import Region
from .watch_button import WatchButtonRegion

class CoinBonusRegion(Region):
    id = "playing.modals.coin_bonus"
    x = 164
    y = 244
    width = 456
    height = 472

    watch_button = WatchButtonRegion()