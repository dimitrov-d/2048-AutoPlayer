import random
from time import sleep

from player2048 import Player2048
from utilities import *

player = Player2048()
sleep(2)
for i in range(13):
    player.html.send_keys(random.choice(player.keys))
    sleep(0.3)
tile_container = player.browser.find_element_by_class_name('tile-container')
positions, numbers = player.parse_string_regex(tile_container.get_attribute('innerHTML'))

distinctify(positions,numbers)

grid = [[pos for pos in positions if pos[0] == '1'], [pos for pos in positions if pos[0] == '2'],
        [pos for pos in positions if pos[0] == '3'], [pos for pos in positions if pos[0] == '4']]

tile_mapping = {}
for i in range(len(positions)):
    tile_mapping[positions[i]] = numbers[i]

print(grid)
print(tile_mapping)

for column in grid:
    if len(column) > 1:
        for tile in range(1, len(column) - 1):
            if (int(tile_mapping[column[tile]]) == int(tile_mapping[column[tile - 1]])) and column[tile] != column[tile-1]:
                print('col equal')

from itertools import zip_longest
rows = r = [list(filter(None,i)) for i in zip_longest(*grid)]

for row in rows:
    for tile in range(1, len(row) - 1):
        if (int(tile_mapping[row[tile]]) == int(tile_mapping[row[tile - 1]])) and row[tile] != row[tile - 1]:
            print('row equal')


# player.close()
