import random

board_size = 5
mine_count = 5

mine_field = [[' ' for _ in range(board_size)] for _ in range(board_size)]
mines_placed = 0

while mines_placed < mine_count:
    x = random.randint(0, board_size - 1)
    y = random.randint(0, board_size - 1)
    if mine_field[x][y] != 'X':
        mine_field[x][y] = 'X'
        mines_placed += 1

for row in mine_field:
    print(" ".join(row))