from player2048 import Player2048

player = Player2048()
tile_container = player.browser.find_element_by_class_name('tile-container')
player.close()
