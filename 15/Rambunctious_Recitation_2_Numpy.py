import re
import cProfile
import numpy as np

input = ['placeholder', 11,0,1,10,5,19]

def ram_rec_2(input_list, end_turn):

    list_of_numbers_said = np.full(end_turn + 1, -1, dtype=int)
    list_of_numbers_said[0] = -1

    current_turn = 1
    last_number_spoken = 0

    def find_previous_occurrences(number, list_of_numbers_said, turn_number):
        list_of_turn_numbers = []
        index = int(turn_number) - 1
        while index > 0 and len(list_of_turn_numbers) != 2:
            if list_of_numbers_said[index] == str(number):
                list_of_turn_numbers.append(index)
            index -= 1
        return list_of_turn_numbers

    while current_turn < end_turn:
        # Update last number spoken
        if current_turn != 1:
            last_number_spoken = int(list_of_numbers_said[current_turn - 1])
        
        # Starting number case
        if current_turn < len(input):
            list_of_numbers_said[current_turn] = int(input[current_turn])
        # Consider last number spoken
        elif last_number_spoken not in list_of_numbers_said[0:current_turn-1]:
            list_of_numbers_said[current_turn] = 0
        elif last_number_spoken in list_of_numbers_said:
            comparison = np.where(list_of_numbers_said == last_number_spoken)[0]
            most_recent = comparison[-2:]
            list_of_numbers_said[current_turn] = (int(most_recent[1]) - int(most_recent[0]))
        
        current_turn += 1

    return(list_of_numbers_said[end_turn - 1])

def main():
    value = ram_rec_2(input, 500001)
    print(value)

if __name__ == '__main__':
    cProfile.run('main()')
    # main()