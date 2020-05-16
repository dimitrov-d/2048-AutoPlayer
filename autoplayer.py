from player2048 import Player2048

player = Player2048()

tile_container = player.browser.find_element_by_class_name('tile-container')
positions, numbers = player.parse_string_regex(tile_container.get_attribute('innerHTML'))
print(positions, numbers)


player.close()
