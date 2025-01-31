from constants import *
from regions.playing.upgrades import UpgradeRegion
from utilities.parser import ValueType
from regions.game import game_region
from ..data import data
from ..process import Process
import time

class Algorithm(Process):
    id = "ALGORITHM"

    def handle_one(self, region: UpgradeRegion):
        for _ in range(5):
            region.value.click()
        return region.cost.read(type = ValueType.COST) == float('inf')

    def iteration(self):
        playing_region = game_region.playing

        # Collect gems
        for _ in range(5):
            for gem_point in playing_region.tower.gem_points:
                if super().is_stopped(): return

                gem_point.click()
                time.sleep(0.25)

        for category_index, category in enumerate(data.categories):
            if data.wave < 50 and category_index != 2:
                continue

            if data.wave >= 50:
                playing_region.categories.all[category_index].click()

            upgrade_index = 0
            remaining = len(category)

            if super().is_stopped(): return

            # Read until near the end
            while remaining >= 5:
                regions = [
                    playing_region.upgrades.first_left,
                    playing_region.upgrades.first_right,
                    playing_region.upgrades.second_left,
                    playing_region.upgrades.second_right,
                ]

                for region in regions:
                    if super().is_stopped(): return

                    if not category[upgrade_index]:
                        category[upgrade_index] = self.handle_one(region)
                        if category[upgrade_index]:
                            self.log(f"✅ MAXED {CATEGORIES[category_index]}/{UPGRADES[category_index][upgrade_index]}")

                    upgrade_index += 1
                    remaining -= 1

                if data.wave < 50:
                    remaining = -1
                    break

                if remaining >= 5:
                    if super().is_stopped(): return

                    playing_region.upgrades.scroll(2)

            if remaining == -1:
                continue

            if super().is_stopped(): return

            # Remaining 1 ~ 4
            if remaining >= 3:
                playing_region.upgrades.scroll(1)

                regions = [
                    playing_region.upgrades.second_left,
                    playing_region.upgrades.second_right,
                ]

                for region in regions:
                    if super().is_stopped(): return

                    if not category[upgrade_index]:
                        category[upgrade_index] = self.handle_one(region)
                        if category[upgrade_index]:
                            self.log(f"✅ MAXED {CATEGORIES[category_index]}/{UPGRADES[category_index][upgrade_index]}")

                    upgrade_index += 1
                    remaining -= 1

            if super().is_stopped(): return
                
            # Remaining 1 ~ 2
            playing_region.upgrades.scroll_last(1)

            regions = [playing_region.upgrades.last_left] if remaining == 1 else [
                playing_region.upgrades.last_left,
                playing_region.upgrades.last_right,
            ]

            for region in regions:
                if super().is_stopped(): return

                if not category[upgrade_index]:
                    category[upgrade_index] = self.handle_one(region)
                    if category[upgrade_index]:
                        self.log(f"✅ MAXED {CATEGORIES[category_index]}/{UPGRADES[category_index][upgrade_index]}")
                upgrade_index += 1
                remaining -= 1

            if super().is_stopped(): return

            # Reset scroll
            items = len(category)
            if items % 2 == 1: items += 1
            items -= 6
            items /= 2

            playing_region.upgrades.scroll(-int(items) - 1)

algorithm = Algorithm()