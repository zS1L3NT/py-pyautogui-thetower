from constants import *
from engine.game.data import GameData
from regions.playing import PlayingRegion
from regions.playing.upgrades.upgrade import UpgradeRegion
from utilities.parser import ValueType
import threading
import time

class GameAlgorithm:
    data: GameData
    region: PlayingRegion

    stop_event = threading.Event()

    def __init__(self, data: GameData, region: PlayingRegion):
        self.data = data
        self.region = region

    def run(self):
        print("[GAME_ALGORITHM] Starting algorithm thread")
        thread = threading.Thread(target = self.thread)
        thread.start()
    
    def collect_gems(self):
        for _ in range(5):
            self.region.tower.gem_point_top.click()
            time.sleep(0.25)
            self.region.tower.gem_point_right.click()
            time.sleep(0.25)
            self.region.tower.gem_point_bottom.click()
            time.sleep(0.25)
            self.region.tower.gem_point_left.click()
            time.sleep(0.25)

    def handle_one(self, region: UpgradeRegion):
        for _ in range(5):
            region.value.click()
        return region.cost.read(type = ValueType.COST) == float('inf')

    def thread(self):
        while not self.stop_event.is_set():
            self.collect_gems()

            for category_index, category in enumerate(self.data.categories):
                if self.data.wave < 50 and category_index != 2:
                    continue

                if self.data.wave >= 50:
                    self.region.categories.all[category_index].click()

                upgrade_index = 0
                remaining = len(category)

                # Read until near the end
                while remaining >= 5:
                    regions = [
                        self.region.upgrades.first_left,
                        self.region.upgrades.first_right,
                        self.region.upgrades.second_left,
                        self.region.upgrades.second_right,
                    ]

                    for region in regions:
                        if not category[upgrade_index]:
                            category[upgrade_index] = self.handle_one(region)
                            if category[upgrade_index]:
                                print(f"[GAME_ALGORITHM] ✅ MAXED {CATEGORIES[category_index]}/{UPGRADES[category_index][upgrade_index]}")
                        upgrade_index += 1
                        remaining -= 1

                    if self.data.wave < 50:
                        remaining = -1
                        break

                    if remaining >= 5:
                        self.region.upgrades.scroll(2)

                if remaining == -1:
                    continue

                # Remaining 1 ~ 4
                if remaining >= 3:
                    self.region.upgrades.scroll(1)

                    regions = [
                        self.region.upgrades.second_left,
                        self.region.upgrades.second_right,
                    ]

                    for region in regions:
                        if not category[upgrade_index]:
                            category[upgrade_index] = self.handle_one(region)
                            if category[upgrade_index]:
                                print(f"[GAME_ALGORITHM] ✅ MAXED {CATEGORIES[category_index]}/{UPGRADES[category_index][upgrade_index]}")
                        upgrade_index += 1
                        remaining -= 1
                    
                # Remaining 1 ~ 2
                self.region.upgrades.scroll_last(1)

                regions = [self.region.upgrades.last_left] if remaining == 1 else [
                    self.region.upgrades.last_left,
                    self.region.upgrades.last_right,
                ]

                for region in regions:
                        if not category[upgrade_index]:
                            category[upgrade_index] = self.handle_one(region)
                            if category[upgrade_index]:
                                print(f"[GAME_ALGORITHM] ✅ MAXED {CATEGORIES[category_index]}/{UPGRADES[category_index][upgrade_index]}")
                        upgrade_index += 1
                        remaining -= 1

                # Reset scroll
                items = len(category)
                if items % 2 == 1: items += 1
                items -= 6
                items /= 2

                self.region.upgrades.scroll(-items - 1)