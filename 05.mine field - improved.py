import random

def create_mine_field(size, count):
    mine_field = [[' ' for _ in range(size)] for _ in range(size)]
    mines_placed = 0
    
    while mines_placed < count:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if mine_field[x][y] != 'X':
            mine_field[x][y] = 'X'
            mines_placed += 1
    
    return mine_field

def display_mine_field(mine_field):
    for row in mine_field:
        print(" ".join(row))

if __name__ == "__main__":
    board_size = 5
    mine_count = 5

    mine_field = create_mine_field(board_size, mine_count)
    display_mine_field(mine_field)