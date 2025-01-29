from engine.game.data import GameData
from engine.game.data.upgrades.categories import CategoryData
from regions.playing import PlayingRegion
from regions.playing.upgrades.upgrade import UpgradeRegion
from utilities.parser import ValueType

class GameReader:
    data: GameData
    region: PlayingRegion

    def __init__(self, data, region):
        self.data = data
        self.region = region

    def run(self):
        self.read_upgrades()

    def read_static(self):
        self.data.resources.cash = self.region.resources.cash.read()
        self.data.resources.coins = self.region.resources.coins.read()
        self.data.resources.gems = self.region.resources.gems.read()

        self.data.player.damage = self.region.player.damage.read()
        self.data.player.healths = self.region.player.healths.read(ValueType.NUMBER_SLASH_NUMBER)
        self.data.player.health_regen = self.region.player.health_regen.read(ValueType.PER_SECOND)

        self.data.enemies.wave = self.region.enemies.wave.read()
        self.data.enemies.damage = self.region.enemies.damage.read()
        self.data.enemies.health = self.region.enemies.health.read()

    def read_one_upgrade(self, category: CategoryData, region: UpgradeRegion, index: int, remaining: int):
        upgrade = category.upgrades[index]

        region.id = f"playing.upgrades.{category.id}.{upgrade.id}"
        region.value.id = f"{region.id}.value"
        region.cost.id = f"{region.id}.cost"

        upgrade.value = region.value.read(upgrade.type)
        upgrade.cost = region.cost.read(type = ValueType.COST, characters = "$1234567890")

        region.name.click()
        upgrade.level = self.region.upgrade_progress_modal.level.read(process_image = False, characters = "1234567890")
        region.name.click()

        index += 1
        remaining -= 1

        return index, remaining

    def read_upgrades(self):
        # In case they're in some modal, close it

        # Check if the upgrade box is visible
        

        for category in self.data.upgrades.categories:
            index = 0
            remaining = len(category.upgrades)

            # Read until near the end
            while remaining >= 5:
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
            if remaining >= 3:
                self.region.upgrades.scroll(1)

                regions = [
                    self.region.upgrades.second_left,
                    self.region.upgrades.second_right,
                ]

                for region in regions:
                    index, remaining = self.read_one_upgrade(category, region, index, remaining)
                
            # Remaining 1 ~ 2
            self.region.upgrades.scroll(1)

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