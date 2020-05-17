import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Player2048:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://play2048.co/')
        self.html = self.browser.find_element_by_tag_name('html')
        self.keys = [Keys.UP, Keys.DOWN,Keys.LEFT, Keys.RIGHT]
        self.keys_hor = self.keys[2:]
        self.keys_ver = self.keys[:2]

    def parse_string_regex(self, string):
        regex_pos = re.compile(r'tile-position-\d-\d')
        regex_nums = re.compile(r'"tile-inner">\d')
        positions = [pos[-4:].replace('-', '') for pos in regex_pos.findall(string)]
        numbers = [num[-1] for num in regex_nums.findall(string)]

        return positions, numbers

    def close(self):
        self.browser.quit()
