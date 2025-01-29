from engine.game.data import GameData
from regions.playing import PlayingRegion

class GameAlgorithm:
    data: GameData
    region: PlayingRegion

    def __init__(self, data, region):
        self.data = data
        self.region = region

    def run(self):
        while True:
            self.region.game_over.retry_button.click()
            for category in self.region.categories.all:
                category.click()
                for _ in range(5):
                    self.region.upgrades.first_left.click()
                    self.region.upgrades.first_right.click()
                    self.region.upgrades.second_left.click()
                    self.region.upgrades.second_right.click()
                self.region.upgrades.scroll(2)
                for _ in range(5):
                    self.region.upgrades.first_left.click()
                    self.region.upgrades.first_right.click()
                    self.region.upgrades.second_left.click()
                    self.region.upgrades.second_right.click()
                self.region.upgrades.scroll(2)
                for _ in range(5):
                    self.region.upgrades.first_left.click()
                    self.region.upgrades.first_right.click()
                    self.region.upgrades.second_left.click()
                    self.region.upgrades.second_right.click()
                self.region.upgrades.scroll(-4)
