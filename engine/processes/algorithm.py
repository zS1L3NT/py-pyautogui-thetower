from constants import *
from regions.playing.upgrades import UpgradeRegion
from utilities.parser import ValueType
from regions.game import region
from ..data import data
from ..process import Process
import logging
import time

class Algorithm(Process):
    id = "ALGORITHM"

    def handle_one(self, upgrade_region: UpgradeRegion):
        for _ in range(5):
            upgrade_region.value.click()
        return upgrade_region.cost.read(type = ValueType.COST) == float('inf')

    def iteration(self):
        # Collect gems
        for _ in range(5):
            for gem_point in region.playing.tower.gem_points:
                if super().is_stopped(): return

                gem_point.click()
                time.sleep(0.25)

        for category_index, category in enumerate(data.categories):
            if data.wave < 50 and category_index != 2:
                continue

            if data.wave >= 50:
                region.playing.categories.all[category_index].click()

            upgrade_index = 0
            remaining = len(category)

            if super().is_stopped(): return

            # Read until near the end
            while remaining >= 5:
                upgrade_regions = [
                    region.playing.upgrades.first_left,
                    region.playing.upgrades.first_right,
                    region.playing.upgrades.second_left,
                    region.playing.upgrades.second_right,
                ]

                for upgrade_region in upgrade_regions:
                    if super().is_stopped(): return

                    if not category[upgrade_index]:
                        category[upgrade_index] = self.handle_one(upgrade_region)
                        if category[upgrade_index]:
                            logging.info(f"✅ MAXED {CATEGORIES[category_index]}/{UPGRADES[category_index][upgrade_index]}")

                    upgrade_index += 1
                    remaining -= 1

                if data.wave < 50:
                    remaining = -1
                    break

                if remaining >= 5:
                    if super().is_stopped(): return

                    region.playing.upgrades.scroll(2)

            if remaining == -1:
                continue

            if super().is_stopped(): return

            # Remaining 1 ~ 4
            if remaining >= 3:
                region.playing.upgrades.scroll(1)

                upgrade_regions = [
                    region.playing.upgrades.second_left,
                    region.playing.upgrades.second_right,
                ]

                for upgrade_region in upgrade_regions:
                    if super().is_stopped(): return

                    if not category[upgrade_index]:
                        category[upgrade_index] = self.handle_one(upgrade_region)
                        if category[upgrade_index]:
                            logging.info(f"✅ MAXED {CATEGORIES[category_index]}/{UPGRADES[category_index][upgrade_index]}")

                    upgrade_index += 1
                    remaining -= 1

            if super().is_stopped(): return
                
            # Remaining 1 ~ 2
            region.playing.upgrades.scroll_last(1)

            upgrade_regions = [region.playing.upgrades.last_left] if remaining == 1 else [
                region.playing.upgrades.last_left,
                region.playing.upgrades.last_right,
            ]

            for upgrade_region in upgrade_regions:
                if super().is_stopped(): return

                if not category[upgrade_index]:
                    category[upgrade_index] = self.handle_one(upgrade_region)
                    if category[upgrade_index]:
                        logging.info(f"✅ MAXED {CATEGORIES[category_index]}/{UPGRADES[category_index][upgrade_index]}")
                upgrade_index += 1
                remaining -= 1

            if super().is_stopped(): return

            # Reset scroll
            items = len(category)
            if items % 2 == 1: items += 1
            items -= 6
            items /= 2

            region.playing.upgrades.scroll(-int(items) - 1)

algorithm = Algorithm()