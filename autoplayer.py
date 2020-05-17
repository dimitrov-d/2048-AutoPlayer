import random
from time import sleep

from player2048 import Player2048
from utilities import *

player = Player2048()
sleep(2)
for i in range(5):
    player.html.send_keys(random.choice(player.keys))
    sleep(0.5)
tile_container = player.browser.find_element_by_class_name('tile-container')
positions, numbers = parse_string_regex(tile_container.get_attribute('innerHTML'))
distinctify(positions, numbers)

player.grid_cols = [[pos for pos in positions if pos[0] == '1'], [pos for pos in positions if pos[0] == '2'],
                    [pos for pos in positions if pos[0] == '3'], [pos for pos in positions if pos[0] == '4']]

player.tile_mapping = {}
for i in range(len(positions)):
    player.tile_mapping[positions[i]] = numbers[i]

print(player.grid_cols)
print(player.tile_mapping)

for column in player.grid_cols:
    if len(column) > 1:
        for tile in range(1, len(column) - 1):
            if int(player.tile_mapping[column[tile]]) == int(player.tile_mapping[column[tile - 1]]):
                player.html.send_keys(random.choice(player.keys_ver))

player.grid_rows = [[pos for pos in positions if pos[1] == '1'], [pos for pos in positions if pos[1] == '2'],
                    [pos for pos in positions if pos[1] == '3'], [pos for pos in positions if pos[1] == '4']]

print(player.grid_rows)

for row in player.grid_rows:
    for tile in range(1, len(row) - 1):
        if int(player.tile_mapping[row[tile]]) == int(player.tile_mapping[row[tile - 1]]):
            player.html.send_keys(random.choice(player.keys_hor))

# player.close()
