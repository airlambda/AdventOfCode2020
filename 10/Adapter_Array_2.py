import re 
import copy
import math

input = """30
73
84
136
132
117
65
161
49
68
139
46
21
127
109
153
163
160
18
22
131
146
62
113
172
150
171
98
93
130
170
59
1
110
2
55
37
44
148
102
40
28
35
43
56
169
33
5
141
83
15
105
142
36
116
11
45
82
10
17
159
140
12
108
29
72
121
52
91
166
88
97
118
99
124
149
16
9
143
104
57
79
123
58
96
24
162
23
92
69
147
156
25
133
34
8
85
76
103
122"""

input_split = input.split('\n')
input_as_num = [int(x) for x in input_split]

# Account for charging port at 0 joltage
input_as_num.append(0)

# Account for device adapter at +3 the highest existing joltage
input_as_num.append((max(input_as_num) + 3))

sorted_joltage = sorted(input_as_num)

def find_valid_joltage(start_joltage, sorted_input_list):
    end_joltage = start_joltage + 3
    intermediate_list = [i for i in sorted_input_list if i >= start_joltage and i <= end_joltage]
    output_list = copy.deepcopy(intermediate_list)
    for index, number in enumerate(intermediate_list):
        if (number + 3) in sorted_input_list and index != (len(intermediate_list) - 1) and (number + 3) not in intermediate_list:
            output_list.append((number + 3))
    return sorted(output_list)

def num_ways(sublist):
    if len(sublist) == 2:
        return 1
    elif len(sublist) == 3:
        return 2
    elif len(sublist) == 4:
        if (sublist[3] - sublist[0]) == 3:
            return 4
        else:
            return 3 
    else:
        output = 0
        n = len(sublist) - 2
        k = n
        while k != 0:
            output += math.comb(n, k)
            k -= 1
        return output
    
current_joltage = 0
arrangements = 1

while current_joltage != max(sorted_joltage):
    current_sublist = find_valid_joltage(current_joltage, sorted_joltage)
    sublist_arrangements = num_ways(current_sublist)
    arrangements *= sublist_arrangements
    current_joltage = max(current_sublist)

print(arrangements)
