import re
import cProfile
import numpy as np

input = ['placeholder', 11,0,1,10,5,19]

def ram_rec_2(input_list):

    list_of_numbers_said = ['placeholder']

    end_turn = 50001
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
            last_number_spoken = str(list_of_numbers_said[current_turn - 1])
        
        # Starting number case
        if current_turn < len(input):
            list_of_numbers_said.append(str(input[current_turn]))
        # Consider last number spoken
        elif last_number_spoken not in list_of_numbers_said[:-1]:
            list_of_numbers_said.append('0')
        elif last_number_spoken in list_of_numbers_said:
            comparison = find_previous_occurrences(last_number_spoken, list_of_numbers_said, current_turn)
            list_of_numbers_said.append(str((int(comparison[0]) - int(comparison[1]))))
        
        current_turn += 1

    return(list_of_numbers_said[50000])

def main():
    ram_rec_2(input)

if __name__ == '__main__':
    cProfile.run('main()')