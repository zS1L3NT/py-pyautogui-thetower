from engine.game.data import GameData
from engine.game.data.upgrades.categories import CategoryData
from regions.playing import PlayingRegion
from regions.playing.upgrades.upgrade import UpgradeRegion
import threading

class GameReader:
    data: GameData
    region: PlayingRegion

    stop_event = threading.Event()

    def __init__(self, data: GameData, region: PlayingRegion):
        self.data = data
        self.region = region

    def run(self):
        print("[GAME_READER] ✅ Starting static reader thread")
        static_thread = threading.Thread(target = self.read_static)
        static_thread.start()

        print("[GAME_READER] ✅ Starting upgrades reader thread")
        upgrades_thread = threading.Thread(target = self.read_upgrades)
        upgrades_thread.start()

    def read_static(self):
        while not self.stop_event.is_set():
            self.data.resources.cash = self.region.resources.cash.read()
            self.data.resources.coins = self.region.resources.coins.read()
            self.data.resources.gems = self.region.resources.gems.read()

            self.data.player.damage = self.region.player.damage.read()
            self.data.player.health_regen = self.region.player.health_regen.read()
            self.data.player.healths = self.region.player.healths.read()

            self.data.enemies.wave = self.region.enemies.wave.read(is_valid = lambda wave: wave >= self.data.enemies.wave)
            self.data.enemies.damage = self.region.enemies.damage.read(is_valid = lambda damage: damage >= self.data.enemies.damage)
            self.data.enemies.health = self.region.enemies.health.read(is_valid = lambda health: health >= self.data.enemies.health)

    def read_one_upgrade(self, category: CategoryData, region: UpgradeRegion, index: int, remaining: int):
        upgrade = category.upgrades[index]

        if upgrade.level != upgrade.max_level:
            region.id = f"playing.upgrades.{category.id}.{upgrade.id}"
            region.name.id = f"{region.id}.name"
            region.value.id = f"{region.id}.value"
            region.cost.id = f"{region.id}.cost"

            # Shockwave frequency is the only upgrade where upgrading it decreases the value
            is_valid = lambda value: (value <= upgrade.value if upgrade.id == "playing.upgrades.defence.shockwave_frequency" else value >= upgrade.value) # type: ignore

            while True:
                upgrade.value = region.value.read(upgrade.type, is_valid = is_valid)
                upgrade.cost = region.cost.read(is_valid = lambda cost: cost >= upgrade.cost)

                region.name.click()
                upgrade.level = self.region.upgrade_progress_modal.level.read(is_valid = lambda level: level >= upgrade.level)
                region.name.click()

                if upgrade.cost < upgrade.target_cost:
                    region.click()
                else:
                    break

        index += 1
        remaining -= 1

        return index, remaining

    def read_upgrades(self):
        while not self.stop_event.is_set():
            for category in self.data.upgrades.categories:
                # Set the upgrade multiplier to 1x
                print(f"[GAME_READER: {category.id}] Setting multiplier to 1x")
                if not self.region.upgrade_border.multiplier_one.is_present():
                    self.region.upgrade_border.multipliers.click()
                self.region.upgrade_border.multiplier_one.click()

                # Check if the scroll is at the top first
                print(f"[GAME_READER: {category.id}] Scrolling to the top")
                for _ in range(10):
                    self.region.upgrades.first_left.name.id = f"playing.upgrades.{category.id}.first_left.name"
                    if self.region.upgrades.first_left.name.read() != category.first:
                        self.region.upgrades.scroll(-2)
                    else:
                        break
                else:
                    raise Exception("Failed to scroll to the top of the category")

                index = 0
                remaining = len(category.upgrades)

                # Read until near the end
                while remaining >= 5:
                    print(f"[GAME_READER: {category.id}] {remaining} upgrades left")

                    regions = [
                        self.region.upgrades.first_left,
                        self.region.upgrades.first_right,
                        self.region.upgrades.second_left,
                        self.region.upgrades.second_right,
                    ]

                    for region in regions:
                        index, remaining = self.read_one_upgrade(category, region, index, remaining)

                    if remaining >= 5:
                        self.region.upgrades.scroll(2)

                # Remaining 1 ~ 4
                print(f"[GAME_READER: {category.id}] {remaining} upgrades left")
                if remaining >= 3:
                    self.region.upgrades.scroll(1)

                    regions = [
                        self.region.upgrades.second_left,
                        self.region.upgrades.second_right,
                    ]

                    for region in regions:
                        index, remaining = self.read_one_upgrade(category, region, index, remaining)
                    
                # Remaining 1 ~ 2
                print(f"[GAME_READER: {category.id}] {remaining} upgrades left")
                self.region.upgrades.scroll_last(1)

                regions = [self.region.upgrades.last_left] if remaining == 1 else [
                    self.region.upgrades.last_left,
                    self.region.upgrades.last_right,
                ]

                for region in regions:
                    index, remaining = self.read_one_upgrade(category, region, index, remaining)

                # Reset scroll
                items = len(category.upgrades)
                if items % 2 == 1: items += 1
                items -= 6
                items /= 2

                self.region.upgrades.scroll(-items - 1)

                # Move to next page
                category = category.id
                if category == "attack":
                    self.region.categories.defence.click()
                elif category == "defence":
                    self.region.categories.utility.click()
                elif category == "utility":
                    self.region.categories.attack.click()