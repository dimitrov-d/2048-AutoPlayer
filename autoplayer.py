from time import sleep

from player2048 import Player2048

player = Player2048()
sleep(2)
tile_container = player.browser.find_element_by_class_name('tile-container')
positions, numbers = player.parse_string_regex(tile_container.get_attribute('innerHTML'))

print(positions, numbers)
# grid = [[pos for pos in positions if pos[0]=='1'], [pos for pos in positions if pos[0]=='2'],
#         [pos for pos in positions if pos[0]=='3'], [pos for pos in positions if pos[0]=='4']]
grid = {}
for i in range(len(positions)):
    grid[positions[i]] = numbers[i]

print(grid)
# player.close()
