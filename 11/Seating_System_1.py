import re
import copy

input = """LLLLLLLLLL.LLLLL.LLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLL.LLLLL.LLLLLLLLLLL.LLLLLL.LLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLL.L
LLLLLLLL.L.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLL..LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL
LLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.L.LLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLL.
L.LLLLLLLLLLLLLL.LLLL.LLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLLLLLLLL.LLLL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL
L..LL......LL.L..LL...L.........L.......LLL........L...L....L...LL.L....L.....LL....L..LL...L..
LL.LLLLLLLLLLLLLLLLLL.LLLL.L.LLLLLL.LLLLLL.L.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLL.LLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLL.LL.LLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLL.L
LLLLLLLLLL.LLLLLLLLLL.LLLLLL.LL.LLL.LLLLLLLL.L.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLL.L
L.LLLLLLLL.LL.LL.LLLL..LLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL
...L.L.........LL..L.L.....L....L....L...L...L.LL...LLLLL....L...L......L..LLL..LL.....L..LL..L
LLLLLLLLLL.LLLLL.LLLL.LLLLLL..LLLLL.LLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLL.LLL.
LLLLLLLLLL.LL.LL.LLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLL.LL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLL.LLLLL.LLLL.LL.LLL..LLLLL.LLLLLLLL.LLLL.LL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLL.LLL.LLLLLL.LLLLLL.LLLLL.LL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLL.LLL.L.LLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL
...L....LL....L.L....L.L.LL.L.LL.L..LL....LL.LL.........L..LL........L.LL..L....LL...L.......LL
LLLLLLLLLL.LLLLL.LLLL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL
L.LLLLLLLL.LLLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LL.LLLLLL.LLLLL.LLLL.LLL
LLLLLLLLLL.LLLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLL.LLLLL..LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL
LL.LLLLLLL.LLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLL.LLLL.LL.LLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
..L.....L........LLL.......LL.LL....LL........L..L.L.LLLL.....L..LL....LL.L.L........LL.L.....L
LLLLLLLLLL.LLLLL.L.LL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LL.LL.LLLLL.LL
LLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLL..LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLL..LLLLL.LLLLLLLLLLLLLLL.LL.LLLLLLLL.LLLLLLL..LLLLLL.LLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLL
LLLLLLLLLL.LLLLL.LLLL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLL.LLL.LLL.LLLL.LLLL.LLLLLLLLL.LLLLLLLLLL.LLL
LLLLLL.LLLLLLLLL.LL.L.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LL.LLLLL
L....L..LL..LL..LL......L..LL..LL.LL...L.....L.....L.L...L.LL.....L.......L..LL.........LLLL...
LLLLLLLLLL.LLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLL.LL.LLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLL.L.LLLLLL
LLLLLLLLLL.LLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLL..LLLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLL.L.LLLLL.L.LLLLL.LLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLLLLLLLL.LLLL.LLLLLL.LLLLLL.LLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.L.LLL.LLLLLLLL
L..L.L...LL.......L...............L..L....L.LLLL...L.L..L..LL.L...L...L...L.....L...L.....LLL..
LLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLL.LLLLL.LLLL.L.LLLL.LLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLL.LLLLL.LLLL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLL.LL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.L.LL.LLL
L.LLLLLLLLLLLLLLLLLLL.LL.LLL.LLLLLL.LLLLLLLL.LLLLLLL.LLLLLLL.LLLL.LLLL.L.LLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLL.LLLLL..LLLLLLLL.L.LLLLLL.LLLLLLLL.LLLLLLLLLLLLL...LLLLLLLLL.LLLLLLLLL..LLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLL.LLLLLL.LLLLLL.LLLLLL.LLLLLLLLL.L.LLLLLLLLLLLLLLL.LL.LLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLL.LL.LL.LLLLLLLLLLL.LLLLLL.LLLL.LLLLLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
..L.L....L.L......L..L.....L..L.LLLLL..L...............LLL.LLL.....L.L..L...L.LL.....L...L.....
.LLL.LLL.LLLLLLL.LLLL.LLLLLL.LL.LLL.LLLLLLLLLLLLLLLL.LL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLL..LLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLLL.L.LLLLL.LLLLLLLL
LLLLLLLLLL.LLLLL.LLLL.LLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLL..LLLL.LLLL.LLLLLL.LLL.LL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL..LLLLLLL
LLLLLLLLLL.LLLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLL..LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL
....LLL........L......L.LL.......LL.LL.LL.L.L..LL.L.....L.LLL.....L........LL......L..L.......L
LLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LL.LLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLL.L
LLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLL.LLLLL.LLLL.L.LLLL.LLL.LL.LLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLL..LLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL..LLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL
...............L.L...L...L....L..L..L......L.......L..L......LL.LL.LL.L.......L....L......L...L
LLLLL.LLLL.LLLLL.LLLLLLLLLLL.LLLLLL.LLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLL.L.LL.LL.LLL.LLLLLL.LLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLL.LLLL
LLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLL.LLLLLL.L.LLLLLLLLLLLLLLL.LLLLLLLL..LLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLL
LLLLL.LLLLLLLLLL.LL.LLLLLLLLLLLLLLL.LLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
....LLL...LL.L....LL.L..L..L.........L.L...L.LLL..L...L..L..L.......L..L.LL.L..LL....LL.L..LLLL
LLLLLLLLLL.LLLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LL.LL.LLLLLLLL
LLLLLLLLLL.LLLLLLLLLL.LLLLLL.LLL.LLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLL
LLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLL..LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLL.LL.LLLLLLLLLLLLLL.LL.LLLLLL
LLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLL.LLL.LLLLL.LLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLL.LLLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLL.L.LLLLLLL.L.LLLLLLLLLLLLLLL.LLLLLLLL
.LLLLL.LLL.LLLLL.LLLL.LL.LLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL
LLLL.LLLLLLLLLLL.LLLLLLLL.L..LLLLLLLLLLLLLLL.LLLL..LLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLL.LL
LLLLLLLL.L.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLL.LL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLL.LLLLLLLLLL.LLLLLLLL
LLLLLLLLLL.LLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LL.LLLLLLLLLLL
L......L...LL...L.L.L...LL.L...L......L......LL......LL.L.L....LL.LL.......LL...L..LLL...LL...L
LLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLL..LLLLLLLLLLLLLL.LLL.LLLL
LLLLLLLLLL.LLLLL.LLLL.LLLLLL.LLLLLL.LLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLL.LL.LLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLL.L.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL..LLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLL.LLLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLL.LLLLL.LLLL.LLLLLL.LLLLLLLLLLLLL..LL.LLLLL.LLLLLLL.LLLLLLLLL.L.LLLLLLL.LLLLL.LLLLLLLL
...L.L.L.....L........LLL.....LL.L.L.LL.....L...LL..L.LLL.....LL.L....L.L...LLL....L...LLLL...L
LLLLLLLLLL.LLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLL..LLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLL
LLLLLLLLLL.LLLLL.LLL..LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.L.LL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLL..LLLLL.LLLL..LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLL.LLLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLLLLLLLLL.LLLLLLL.LLL.LLLLLLLLLLLLLLLLLL.LL.LLLLLLL.
LLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL
LLLLLLLLLL.LLLLL.LLLLLL.LLLLLLLLLLL...LLLLLLLLLLLLLL.L.L.LLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLLLLLLL.LLLLL.LL.LLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL
.LLLLLLLL..LLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLL.LLLLLL.LLLLL.LLLLL.LL
LLLLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLL..LLL.LLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLL.L.LL.L.L.LLLLLL.LLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL"""

input_split = input.split('\n')

seat_array = []

for row_number, row in enumerate(input_split):
    row_array = [x for x in row]
    seat_array.append(row_array)

MAX_COL_NUMBER = len(seat_array[0]) - 1
MAX_ROW_NUMBER = len(seat_array) - 1

IS_STABLE = False

def check_if_stable(original_list, new_list):
    if original_list == new_list:
        return True
    else:
        return False

def get_surrounding_seat_info(input_list, row_number, col_number, max_row_number, max_col_number):
    num_occupied_seats = 0
    row_shift_array = [-1, 0, 1]
    col_shift_array = [-1, 0, 1]
    for row_shift in row_shift_array:
        for col_shift in col_shift_array:
            if row_number + row_shift < 0 or row_number + row_shift > max_row_number or col_number + col_shift < 0 or col_number + col_shift > max_col_number or (row_shift == 0 and col_shift == 0):
                continue
            elif input_list[row_number + row_shift][col_number + col_shift] == '#':
                num_occupied_seats += 1
    return num_occupied_seats

def update_seat_info(input_list, row_number, col_number, num_occupied_seats):
    current_state = input_list[row_number][col_number]
    if current_state == '.':
        new_state = '.'
    elif current_state == 'L' and num_occupied_seats == 0:
        new_state = '#'
    elif current_state == '#' and num_occupied_seats >= 4:
        new_state = 'L'
    else:
        new_state = current_state
    return new_state

def count_num_occupied_seats(input_list):
    num_occupied_seats = 0
    for row in input_list:
        for seat in row:
            if seat == '#':
                num_occupied_seats += 1
    return num_occupied_seats

while IS_STABLE is False:
    updated_seat_array = []
    for row_number, row in enumerate(seat_array):
        updated_row = []
        for seat_number, seat in enumerate(row):
            surrounding_seat_info = get_surrounding_seat_info(seat_array, row_number, seat_number, MAX_ROW_NUMBER, MAX_COL_NUMBER)
            new_seat_state = update_seat_info(seat_array, row_number, seat_number, surrounding_seat_info)
            updated_row.append(new_seat_state)
        updated_seat_array.append(updated_row)
    IS_STABLE = check_if_stable(seat_array, updated_seat_array)
    seat_array = copy.deepcopy(updated_seat_array)
    print(count_num_occupied_seats(seat_array))