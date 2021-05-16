import re
import copy

input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

input_split = input.split('\n')

NUMBER_REGEX = r'[a-z]+:\s(?P<lower_bound_1>[0-9]+)-(?P<upper_bound_1>[0-9]+)\sor\s(?P<lower_bound_2>[0-9]+)-(?P<upper_bound_2>[0-9]+)'
TICKET_REGEX = r'(?<=nearby\stickets\:\n)[0-9\s,]+'
ALLOWABLE_NUMBER_ARRAY = []
TICKET_ARRAY = []

for lines in input_split:
    try:
        match = re.match(NUMBER_REGEX, lines)
        ALLOWABLE_NUMBER_ARRAY.append(*list(range(int(match.group('lower_bound_1')), int(match.group('upper_bound_1')) + 1, 1)))
        ALLOWABLE_NUMBER_ARRAY.append(*list(range(int(match.group('lower_bound_2')), int(match.group('upper_bound_2')) + 1, 1)))
    except AttributeError:
        break

ALLOWABLE_NUMBER_SET = set(ALLOWABLE_NUMBER_ARRAY)

for lines in input_split:
    try:
        match = re.match(TICKET_REGEX, lines)
        number_split = match.group(0).split(',')
        for number in number_split:
            if number != '\n':
                TICKET_ARRAY.append(number)
    except AttributeError:
        break

TICKET_SET = set(TICKET_ARRAY)

INVALID_NUMBERS = TICKET_SET - ALLOWABLE_NUMBER_SET

print(ALLOWABLE_NUMBER_SET)
print(TICKET_SET)