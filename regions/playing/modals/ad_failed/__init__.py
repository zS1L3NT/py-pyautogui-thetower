from region import Region
from .ok_button import OkButtonRegion

class AdFailedRegion(Region):
    id = "playing.modals.ad_failed"
    x = 168
    y = 340
    width = 448
    height = 374

    ok_button = OkButtonRegion()