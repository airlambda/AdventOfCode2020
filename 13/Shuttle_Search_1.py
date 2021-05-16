import re
import copy
import math

input = """1001798
19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,859,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,373,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37"""

input_split = input.split('\n')

earliest_time = int(input_split[0])
bus_services = input_split[1].split(',')
available_bus_array = [int(x) for x in bus_services if 'x' not in x]

time_to_wait = 1000
optimal_bus = 0

for bus in available_bus_array:
    next_available_time = (math.ceil(earliest_time/bus)*bus)
    time_delta = next_available_time - earliest_time
    if time_delta <= time_to_wait:
        time_to_wait = time_delta
        optimal_bus = bus

print("Puzzle solution: " + str(optimal_bus * time_to_wait))