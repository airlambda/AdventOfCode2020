import re 

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

def joltage_difference(input_list):
    idx_1 = 0
    idx_2 = 1
    num_one_jolt_diff = 0
    num_three_jolt_diff = 0
    while idx_2 <= (len(input_list) - 1):
        difference = input_list[idx_2] - input_list[idx_1]
        if difference == 1:
            num_one_jolt_diff += 1
        elif difference == 3:
            num_three_jolt_diff += 1
        idx_1 = idx_2
        idx_2 += 1
    return num_one_jolt_diff * num_three_jolt_diff

print(joltage_difference(sorted_joltage))
print(sorted_joltage)