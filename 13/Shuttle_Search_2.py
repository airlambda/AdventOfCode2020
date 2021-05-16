import re
import copy
import math

input = """19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,859,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,373,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37"""

bus_services = input.split(',')

condition_satisfied = False
start_number = 110000000000000

# candidate_array holds numbers to be tested
candidate_array = []
# not_x_array holds the indices of things in bus_array that are not x
not_x_array = [bus_services.index(x) for x in bus_services if x != 'x']
bus_services_not_x = [int(x) for x in bus_services if x != 'x']

while not condition_satisfied:
    candidate_array = [start_number + x for x in not_x_array]
    remainder = [test_number % divisor for (test_number, divisor) in zip(candidate_array, bus_services_not_x)]
    if not any(remainder):
        print(start_number)
        condition_satisfied = True
    else:
        start_number += 1