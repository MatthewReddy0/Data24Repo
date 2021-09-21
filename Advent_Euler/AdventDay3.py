# Function that returns position
def new_position(x, y, change_x=3, change_y=1):
    x += change_x
    if x > 30:
        x += -31
    y += change_y
    return x, y


# Function that returns if a position is Tree or False
def is_tree(x, y, forest_map):
    if forest_map[y][x] == '#':
        return True
    else:
        return False


# Convert file to something
with open('Advent3input.txt') as file:
    data = file.readlines()

    forest_map = [line.strip() for line in data]
    x = 0
    y = 0
    tree_counter = 0

    for i in range(322):
        x, y = new_position(x, y, 3, 1)
        if is_tree(x, y, forest_map):
            tree_counter += 1

print(tree_counter)
