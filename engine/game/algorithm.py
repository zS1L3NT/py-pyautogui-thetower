from engine.game.data import GameData
from regions.game import GameRegion
from regions.playing import PlayingScreen

class GameAlgorithm:
    data: GameData
    region: GameRegion
    screen: PlayingScreen

    def __init__(self, data, region):
        self.data = data
        self.region = region
        self.screen = region.playing

    def run(self):
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
