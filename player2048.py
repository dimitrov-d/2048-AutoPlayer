import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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


    def close(self):
        self.browser.quit()
