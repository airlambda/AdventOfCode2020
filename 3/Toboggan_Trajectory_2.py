import math

input = """........#.............#........
...#....#...#....#.............
.#..#...#............#.....#..#
..#......#..##............###..
..........#......#..#..#.......
.#..#.......#.........#.#......
.........#..#....##..#.##....#.
..#....##...#..................
##..........#.##...#....##..#..
...#....#...#..............#...
...........................#..#
..##.##.#..................#...
...#.##..#............#........
........#.......#...#.....##.#.
.##..........#......#.......#..
...#..........#...#..#.......#.
......#...#...#.##.......#.#...
........#...#...#...##.........
#..............#.#....#.......#
..#..#..#.#....#...............
.....#........#...#..........#.
##......#...#..#.##.......#....
..#.#.....#.#.............#.#.#
#..#..##......##...#...........
..#......#........#.....#......
.....#.......#....#.#...#......
...#........#...........#...#..
.......#.#...........###....#..
...#...........##....##........
#....#..####....#.....#..#....#
..........#...........#........
...#.......#....#.#.........#..
....#...#.......#..###.........
......#......#..#......#..#....
...#.....#............#..#.....
...#.#.#.#..#.......#.....#....
#....##...#.........#...##.....
#..#.......#..#..#..#...##.....
#.......#............#.....#...
.#........##....##...#........#
.....#...#.....................
.......#........#..............
.....#............#.#.#...#.#..
.....##..#.............#.......
..#.##..#........#..#...#......
.........#.#....#...........#..
.#.....#..#....#.....#...#.....
....#.#................#.......
...............##......#...#...
.##...#...#.......##.#....#....
............#........#.......#.
......##.#.#...................
.#.#..............#.......#....
#.....#...#.......#..#...#.....
.............#....#..#......#..
........#...##................#
.......#...#..#..##............
..#..#...##...#..#.#.....#...#.
.#.#...#.........#.#...........
...###....#.......#...#........
........#......##.#...#..##..#.
.....................#.#.......
.............#...........#...#.
#..#..#.....#.#...#............
...#....#.....#...........#....
..##.....##...#......#..##.....
#.....#.....###.#.....#....##..
.#...........###...............
..................#..##.#...#..
................#....##.#......
.#.#.#...#....#.........#..#.#.
#.......#........##............
.......##.#....#.#............#
..........#..##.#....#.........
........##..#....#.............
.........#....#...........##...
#.........#.#..#..#..........#.
.....#........#......#.........
....#.#.#...............#......
.#..#..##...#.##..........#....
..#....................#.#.....
.........#....#...........#.#.#
........#....##.##.............
..#.....#.......#..#......#....
#..........#.#.....#.#....#....
........##.#.....#..#.....#.#..
...................#...#....#.#
............#..#....#...#...#..
..............#.#.........#....
...#..#..#.#..##..##...........
.#...........................#.
.#.......#...........#....#.#.#
......#..#...#........#...##...
.........#......#.#.......#...#
...#..##................#......
.............#.#..##....#.#....
...............#..#......#.....
.#......#.#.#....#........#....
........#..#.##..#..#.........#
...#....#.#...#..#.......#..#..
..#...##.........#..#...#......
...#...........#.............#.
....#.....................#....
.....#..#...............#.#...#
....#..........#........#......
..#....#........##..##.........
...#....#..#.#.......#...#.....
..#........#....#...##....#.#..
.#...#........##.....#....###..
#....#....##......#........#...
.........#..#.#..........#....#
....#...#.....#.......##.......
..............#..........#.##..
#...#..#..............#......#.
.................#......##....#
..#..##..#.......#..#.#......#.
.............#........#.....#.#
.#.##............#..#..........
..#...#...........#..##........
.#....#...#....#.......#.......
...#.#..#..#..#....#.....#..#..
....#..##..............#...#...
#..........###......###........
.##.##......#..#............#..
.#...........#.#.....#...#.....
#.#..#...#............#........
.........#...#...#..........##.
.......###..#..........#.......
...........###.....#........#..
.#.............#.....#......#..
...#.....#....#.#.........##...
....##..##...#.......##........
......#....##.........#......#.
..........#.....##..#.....#..#.
..........####...#..#.........#
.##....#..#.#...#.......#......
...#.#.##.#.#...#....#.#.#.....
.........#...##........##.....#
..#........#..........##...##.#
##...##..........#.#...........
..............#......#.........
........#.....#.#.......#......
.#...#.....#....#.#..#.........
.....#....................##...
....#..................#.#...##
.....#............#..##........
#..........#....#.#.......##.#.
....#..#.....................#.
#..#....##.....#...............
..#...#..#..##....#.#..........
.......#......#.#.......#.....#
...#.#.......#...#.##..........
....#..........#....#.#.#......
.......#..#..........#..##.....
#......#......#...#......#...#.
###..#....##......##........#..
.#..........#.....#.......#.#..
.......#.....#.....#.#.........
..#...#....#...................
..............#.##.............
.#...#.......#.##...#.#.......#
.......#......................#
....#.#...#.#........#.........
.#......#....#...#.............
#.......#...###.....#.#.#..#...
#....##.#...............##.....
..#.......#..................#.
.....####...............#......
.##......#......#.#.......##.#.
#......##..###....#....#......#
.##.......##.##...#.##.........
......##............#.......#..
......#..#.....##.#............
.#..........#.....##...........
#.........#......#......##.#...
.........#.......#..#......#.#.
.........#.......#...........#.
.#..##.#..................##...
.............#.............#...
.....##........#......##...##..
..#..#.#.....#..#....#.........
.....#....#.....#.....#........
#......##.....#....#....#......
#.................#..#.#......#
.......#..#......#....#.#...#.#
....#.........#..#..........#.#
##......#............#...#...#.
....##......#...#.....#....##..
.#...##.........#..............
......#.....................#..
..#..........###....#..........
#....#...#..#.............#....
#........#.#......#....#.......
.#...#.......#..#...#.#...#..#.
................##.#.....#.....
###.......#...#................
...#.......#...#.#.....#.......
..#.........#.....#.#.......#..
......#.......................#
#.....#.#..#....#.......#......
...#....#..#....####...........
.............#.....#...##......
.......#.........#...#..#......
.##..#.........#....#.#........
....##...#.#...........#....#..
.........................##....
..###.......##....#.#.........#
.#....#.#.#...........##....#..
......#...#..#..#..#..#.......#
..#....#.#.......#..#..#..#...#
.....##...#.##....#.#...#......
.........#..#....#..#..........
.##..##.........#.#.....#......
..........#...##...#.#...#.....
#.##..#..#.............#.......
...#...........#.......#......#
.......#....#....#...##.......#
..#.##........###..#......#....
...#...........###......#..#..#
.#.........#.#.........#.#.....
##.......##.##.##......##......
............#...#..........#...
....................#..........
...#..#...........#...#...#....
.................#...#......###
...#................#.#.##.....
...............#........#......
#.............##......#.#..#...
..#.#.....#..#.##.....##...#...
......#.........#......#.......
#.......#......#....#........#.
.#..##.....#.........#.........
....##.##.#...#.........##.#...
...............#..#..#..##.....
.#..#...............###........
.##............##..............
...............#...##...#...#.#
..#.#......#.#..#.............#
#.#..#..##.........#.#.#...#...
....##.#....................##.
.........#..#.....#.....#..#..#
....#......#......#.##....#....
........###..#.............#..#
##................#.........#..
#.....#.......#....#...........
..#.......#..#........#....#...
..#.#.##..#.#...##........#.##.
..#..........#............#....
..........#...............##...
..........###........#.#.......
.....###..#.............#......
##.............#...#.....#.....
.....#......#....#........#.#..
............#..#..............#
.................#...........##
#........#.........###.....#...
..#.#..............##......#.#.
.#...........#.........#..##..#
...............................
.#.....#..#....#....#......#...
.#...#......#.#..#....#.......#
......#.##.......#......#......
......#..###..#................
#..#.....#........##...#.......
......##.........##....#...##..
.#..........#.................#
#..#.......#...............#...
.........#..###....#.#.##.#....
..#...#.##..##...............##
.........#.....................
.#....##...#......#....#.......
............#..........#..#....
...#......##....#....#........#
.#...................#.........
#.#........###....#..........#.
.........#....#....#........##.
.#....#..#.........#..#........
...............#..#...#..#...##
.........#....##....#......#...
.#.............................
...#........#...#.#...#.#..#...
.....#..##...#.#...............
#.....#....#.........#.........
#...#...........##.........#...
..##........#.#...#...#......#.
...........#.....#...#.#.......
......###....#.....#...........
......##...#..........#....#.#.
.......##..##..........#.......
....#............#..#....##....
..##...................#.#.....
...#.#..#.#....................
.#..##..#............##.###..#.
#.#...#....#.#..........#.#....
........#....#.....#...........
..##....#...#.......#..........
...........##.##....#..........
.....#............#............
.......#.............#....#....
.................#......#......
......##.......#....#..##...#..
.#..#....#.....................
...#.#.#...#......##...........
##........##.#....#....#.......
.......#.....#..#..#...#.##....
#..........#....#.#..#..#..#...
...##..............#...........
.........#.....#.#....#.......#
.........#....##..#..##..#.....
.....#......................#..
...###...#..#......#...........
....#.....................#....
...............................
..#.....###.......#..#....#....
#..........#.................#.
......#.......###.......#..##..
.............#.##..............
......#..#.#..#...........#....
...#....##.#...#..#.#...#....#.
..................#...#....#.##
......#.#....#.................
......#.#.....#.....#..##......
#..##...........#..#.....#.##.."""

input_split = input.split('\n')

def tree_counter(num_trees, check_symbol):
    if check_symbol == '#':
        num_trees += 1
    return num_trees

map_array = []
# Get one line into a list with one character per entry of list
for idx in range(len(input_split)):
    map_array.append(list(input_split[idx]))

# Map is 31 wide (0 - 30) by 324 deep (0 - 323)
# Define x coordinate as running left to right, y coordinate as running top to bottom
X = 0
Y = 0
num_trees = 0

# Define a series of strides by X and Y
x_strides = [1, 3, 5, 7, 1]
y_strides = [1, 1, 1, 1, 2]

# Define a result array of trees hit by each slope
result_array = []

for idx in range(len(x_strides)):
    # Wrap map right to left by doing things modulo 31
    if map_array[Y][X] == '#':
        num_trees == 1
    while Y < len(map_array):
        X += x_strides[idx]
        Y += y_strides[idx]
        if X >= 31:
            new_X = X % 31
            X = new_X
        if Y >= 323:
            break
        num_trees = tree_counter(num_trees, map_array[Y][X])

    result_array.append(num_trees)
    X = 0
    Y = 0
    num_trees = 0

print(math.prod(result_array))
