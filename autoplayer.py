import random
from time import sleep
from player2048 import Player2048
from utilities import *

player = Player2048()
sleep(2)
for i in range(5):
    player.html.send_keys(random.choice(player.keys))
    sleep(0.5)

print('Columns: ', player.grid_cols)
print('Rows: ', player.grid_rows)
print(player.tile_mapping)

player.play_game()


# player.close()
