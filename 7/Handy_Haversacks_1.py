import re

input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

input_split = input.split('\n')

COLOUR_REGEX = r'[a-z\s]+?(?=bag)'

NUM_BAGS = 0
ALL_COLOUR_ARRAY = []
COLOUR_ARRAY = []
checked_colours = []
graph = {}

def find_shiny_gold(entries, graph):
    global NUM_BAGS
    global checked_colours
    if type(entries) is list:
        for entry in entries:
            if 'shiny gold' in graph[entry] or entry == 'shiny gold' and entry not in checked_colours and graph[entry] not in checked_colours:
                NUM_BAGS += 1
                checked_colours.append(entry)
            elif len(entries) == 0:
                return
            else:
                find_shiny_gold(graph[entry], graph)
    elif type(entries) is str:
        checked_colours.append(entries)
        find_shiny_gold(graph[entries], graph)

for entry in input_split:
    COLOUR_ARRAY.append([*re.findall(COLOUR_REGEX, entry)])

for entry in COLOUR_ARRAY:
    for colour in entry:
        if colour.strip() == 'bags contain no other':
            pass
        else:
            ALL_COLOUR_ARRAY.append(colour.strip())

ALL_COLOUR_SET = set(ALL_COLOUR_ARRAY)

for entry in COLOUR_ARRAY:
    value_list = []
    for index, colour in enumerate(entry):
        if index == 0:
            index_key = colour.strip()
            graph[index_key] = {}
        elif index != 0 and colour.strip() == 'bags contain no other':
            pass
        else:
            value_list.append(colour.strip())
    graph[index_key] = value_list
    
for entry in graph:
    find_shiny_gold(entry, graph)
print(NUM_BAGS)