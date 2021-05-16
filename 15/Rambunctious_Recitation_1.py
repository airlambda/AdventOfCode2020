import re

input = ['placeholder', 11,0,1,10,5,19]

list_of_numbers_said = ['placeholder']

end_turn = 2021
current_turn = 1
last_number_spoken = 0
previous_occurrence = 0

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
        previous_occurrence = [index for index, number in enumerate(list_of_numbers_said) if number == last_number_spoken]
        comparison = previous_occurrence[-2:]
        list_of_numbers_said.append(str((int(comparison[1]) - int(comparison[0]))))
    
    current_turn += 1

print(list_of_numbers_said[2020])

