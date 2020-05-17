import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utilities import *

class Player2048:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://play2048.co/')
        self.html = self.browser.find_element_by_tag_name('html')
        self.keys = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
        self.keys_hor = self.keys[2:]
        self.keys_ver = self.keys[:2]
        self.grid_rows = []
        self.grid_cols = []
        self.tile_mapping = {}

    def evaluate_tiles(self):
        tile_container = self.browser.find_element_by_class_name('tile-container')
        positions, numbers = parse_string_regex(tile_container.get_attribute('innerHTML'))
        distinctify(positions, numbers)

        self.grid_cols = [[pos for pos in positions if pos[0] == '1'], [pos for pos in positions if pos[0] == '2'],
                            [pos for pos in positions if pos[0] == '3'], [pos for pos in positions if pos[0] == '4']]

        self.grid_rows = [[pos for pos in positions if pos[1] == '1'], [pos for pos in positions if pos[1] == '2'],
                            [pos for pos in positions if pos[1] == '3'], [pos for pos in positions if pos[1] == '4']]

        self.tile_mapping = {}
        for i in range(len(positions)):
            self.tile_mapping[positions[i]] = numbers[i]

    def find_matching_col_tiles(self):
        for column in self.grid_cols:
            for tile in range(1, len(column) - 1):
                if int(self.tile_mapping[column[tile]]) == int(self.tile_mapping[column[tile - 1]]):
                    return True
        return False

    def find_matching_row_tiles(self):
        for row in self.grid_rows:
            for tile in range(1, len(row) - 1):
                if int(self.tile_mapping[row[tile]]) == int(self.tile_mapping[row[tile - 1]]):
                    return True
        return False

    def play_game(self):
        while True:
            if self.find_matching_row_tiles():
                self.html.send_keys(random.choice(self.keys_hor))

            elif self.find_matching_col_tiles():
                self.html.send_keys(random.choice(self.keys_ver))

            else:
                self.html.send_keys(random.choice(self.keys))
            sleep(0.5)
            self.evaluate_tiles()

    def close(self):
        self.browser.quit()
