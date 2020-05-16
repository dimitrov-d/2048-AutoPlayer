from selenium import webdriver


class Player2048:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://play2048.co/')

    def close(self):
        self.browser.quit()
