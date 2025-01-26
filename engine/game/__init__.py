from constants import *
from regions.playing import PlayingScreen
from engine.game.data import GameData
from regions.game import GameRegion
import time
import os

class GameEngine:
    data = GameData()
    region: GameRegion
    screen: PlayingScreen

    def __init__(self, region):
        self.region = region
        self.screen = region.playing

    def start(self):
        while True:
            self.region.game_over.retry_button.click()
            for category in self.screen.categories.all:
                category.click()
                for _ in range(5):
                    self.screen.upgrades.first_left.click()
                    self.screen.upgrades.first_right.click()
                    self.screen.upgrades.second_left.click()
                    self.screen.upgrades.second_right.click()
                self.screen.upgrades.scroll(2)
                for _ in range(5):
                    self.screen.upgrades.first_left.click()
                    self.screen.upgrades.first_right.click()
                    self.screen.upgrades.second_left.click()
                    self.screen.upgrades.second_right.click()
                self.screen.upgrades.scroll(2)
                for _ in range(5):
                    self.screen.upgrades.first_left.click()
                    self.screen.upgrades.first_right.click()
                    self.screen.upgrades.second_left.click()
                    self.screen.upgrades.second_right.click()
                self.screen.upgrades.scroll(-4)

    def read_static(self):
        self.data.resources.cash = self.screen.resources.cash.read()
        self.data.resources.coins = self.screen.resources.coins.read()
        self.data.resources.gems = self.screen.resources.gems.read()

        self.data.player.damage = self.screen.player.damage.read()
        self.data.player.healths = self.screen.player.healths.read()
        self.data.player.health_regen = self.screen.player.health_regen.read()

        self.data.enemies.wave = self.screen.enemies.wave.read()
        self.data.enemies.damage = self.screen.enemies.damage.read()
        self.data.enemies.health = self.screen.enemies.health.read()

    def read_upgrades(self):
        def read_one(category, region, index, remaining):
            upgrade = category.list[index]

            upgrade.value = region.value.read()
            upgrade.cost = region.cost.read(characters = "$1234567890")

            region.name.click()
            upgrade.level = self.screen.upgrade_progress.level.read(process = False, characters = "1234567890")
            region.name.click()

            index += 1
            remaining -= 1

            return index, remaining

        for category in self.screen.categories.all:
            index = 0
            remaining = len(category.list)

            # Read until near the end
            while remaining >= 5:
                regions = [
                    self.screen.upgrades.first_left,
                    self.screen.upgrades.first_right,
                    self.screen.upgrades.second_left,
                    self.screen.upgrades.second_right,
                ]

                for region in regions:
                    index, remaining = read_one(category, region, index, remaining)

                if remaining >= 5:
                    self.screen.upgrades.scroll(2)

            # Remaining 1 ~ 4
            if remaining >= 3:
                self.screen.upgrades.scroll(1)

                regions = [
                    self.screen.upgrades.second_left,
                    self.screen.upgrades.second_right,
                ]

                for region in regions:
                    index, remaining = read_one(category, region, index, remaining)
                
            # Remaining 1 ~ 2
            self.screen.upgrades.scroll(1)

            regions = [self.screen.upgrades.last_left] if remaining == 1 else [
                self.screen.upgrades.last_left,
                self.screen.upgrades.last_right,
            ]

            for region in regions:
                index, remaining = read_one(category, region, index, remaining)

            # Reset scroll
            items = len(category.list)
            if items % 2 == 1: items += 1
            items -= 6
            items /= 2

            self.screen.upgrades.scroll(-items - 1)

            # Move to next page
            category = category.category
            if category == "attack":
                self.screen.categories.defence.click()
            elif category == "defence":
                self.screen.categories.utility.click()
            elif category == "utility":
                self.screen.categories.attack.click()