import re

from selenium import webdriver


class Player2048:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://play2048.co/')
        self.html = self.browser.find_element_by_tag_name('html')

    def parse_string_regex(self, string):
        regex_pos = re.compile(r'tile-position-\d-\d')
        regex_nums = re.compile(r'"tile-inner">\d')
        positions = [pos[-4:].replace('-', '') for pos in regex_pos.findall(string)]
        numbers = [num[-1] for num in regex_nums.findall(string)]

        return positions, numbers

    def close(self):
        self.browser.quit()
