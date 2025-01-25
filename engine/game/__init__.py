from constants import *
from regions.playing import PlayingScreen
from engine.game.data import GameData
import time
import os

class GameEngine:
    data = GameData()
    region: PlayingScreen

    def __init__(self, region):
        self.region = region

    def start(self):
        self.read_upgrades()

        print(self.data)

        # while True:
        #     self.read_upgrades()

        #     os.system("clear")
        #     print(self.data)

    def read_static(self):
        self.data.resources.cash = self.region.resources.cash.read()
        self.data.resources.coins = self.region.resources.coins.read()
        self.data.resources.gems = self.region.resources.gems.read()

        self.data.player.damage = self.region.player.damage.read()
        self.data.player.healths = self.region.player.healths.read()
        self.data.player.health_regen = self.region.player.health_regen.read()

        self.data.enemies.wave = self.region.enemies.wave.read()
        self.data.enemies.damage = self.region.enemies.damage.read()
        self.data.enemies.health = self.region.enemies.health.read()

    def read_upgrades(self):
        def read_one(category, region, index, remaining):
            upgrade = category.list[index]

            upgrade.value = region.value.read()
            upgrade.cost = region.cost.read(characters = "$1234567890")

            region.name.click()
            upgrade.level = self.region.upgrade_progress.level.read(process = False, characters = "1234567890")
            region.name.click()

            index += 1
            remaining -= 1

            return index, remaining

        categories = [
            self.data.upgrades.attack,
            self.data.upgrades.defence,
            self.data.upgrades.utiltiy,
        ]

        for category in categories:
            index = 0
            remaining = len(category.list)

            # Read until near the end
            while remaining >= 5:
                regions = [
                    self.region.upgrades.first_left,
                    self.region.upgrades.first_right,
                    self.region.upgrades.second_left,
                    self.region.upgrades.second_right,
                ]

                for region in regions:
                    index, remaining = read_one(category, region, index, remaining)

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
                    index, remaining = read_one(category, region, index, remaining)
                
            # Remaining 1 ~ 2
            self.region.upgrades.scroll(1)

            regions = [self.region.upgrades.last_left] if remaining == 1 else [
                self.region.upgrades.last_left,
                self.region.upgrades.last_right,
            ]

            for region in regions:
                index, remaining = read_one(category, region, index, remaining)

            # Reset scroll
            items = len(category.list)
            if items % 2 == 1: items += 1
            items -= 6
            items /= 2

            self.region.upgrades.scroll(-items - 1)

            # Move to next page
            category = category.category
            if category == "attack":
                self.region.categories.defence.click()
            elif category == "defence":
                self.region.categories.utility.click()
            elif category == "utility":
                self.region.categories.attack.click()