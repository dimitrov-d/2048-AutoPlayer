from selenium import webdriver


class Player2048:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://play2048.co/')


player = Player2048()
tile_container = player.browser.find_element_by_class_name('tile-container')
divs = tile_container.find_elements_by_tag_name('div')
divHTML = [div.find_element_by_xpath('.').get_attribute('outerHTML') for div in divs]
player.browser.quit()