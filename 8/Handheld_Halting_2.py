import re
import copy

input = """nop +612
acc -6
acc +41
acc -4
jmp +388
acc +3
acc +25
acc +11
nop +56
jmp +110
jmp +479
jmp +129
nop +436
jmp +339
acc -3
acc -17
acc -14
acc +37
jmp +24
jmp +324
jmp +233
jmp +1
acc +44
acc +17
nop +150
jmp +163
acc +0
acc +10
acc +49
jmp +170
acc +36
jmp +339
acc +28
acc -8
nop +194
jmp +84
acc +11
jmp +241
acc +0
jmp +1
acc +1
jmp +370
jmp +245
jmp +235
acc -6
acc +27
jmp +493
nop +401
acc +40
acc +7
jmp +562
acc +6
nop +472
acc -7
nop +508
jmp +44
nop +2
jmp -6
nop +542
acc +1
acc +34
acc +39
jmp +239
jmp +238
acc +30
acc -5
acc -11
jmp +357
jmp +65
acc +42
acc -14
acc +18
jmp -53
acc -14
jmp +493
acc +37
acc +23
nop +36
acc +0
jmp +95
jmp +119
acc -10
acc +16
jmp +3
nop +144
jmp -16
nop +27
jmp +219
acc +22
jmp +30
acc -16
acc +6
acc +18
jmp -51
acc -10
acc -18
acc -4
acc -16
jmp +508
nop +202
acc +6
jmp +261
acc +13
jmp -45
acc +0
jmp +1
acc +12
jmp +133
acc -12
acc -8
acc +43
nop +59
jmp +370
acc +40
jmp -78
acc -13
acc -16
acc +5
jmp +283
jmp +95
nop +133
jmp -109
acc +45
jmp +1
acc +44
nop +357
jmp +356
acc -1
jmp +348
jmp +216
nop +183
acc +10
jmp +350
acc +15
jmp +162
acc +42
jmp +1
jmp +1
acc +27
jmp -75
jmp +182
jmp +396
acc +8
acc +35
nop +128
acc -19
jmp +458
acc -7
jmp +45
acc +16
nop +43
nop +85
jmp +129
acc +26
acc +32
acc -13
jmp -52
acc +8
acc +35
jmp +1
nop +264
jmp -71
jmp +286
acc +9
jmp +16
acc +8
nop +258
nop +294
nop +352
jmp -56
acc +26
acc -1
jmp +48
jmp +7
acc +17
acc +28
jmp -155
acc +9
acc -14
jmp -115
acc +26
nop -68
acc -6
jmp -41
acc -16
acc +46
acc +33
jmp +295
acc +29
jmp +387
acc +40
acc +40
jmp -29
acc -8
acc +9
acc +0
acc -8
jmp +340
jmp +66
nop +1
jmp +261
acc +0
jmp -138
nop -29
acc -10
jmp +271
acc +2
acc +17
acc +9
jmp +192
acc +42
acc +2
jmp +174
jmp +393
acc -4
acc -14
acc +13
jmp +286
acc +8
jmp +318
acc +49
acc -12
jmp +42
acc +50
acc +33
acc +2
acc +25
jmp -24
nop +147
acc +19
jmp +324
acc +45
acc +20
acc +49
acc -16
jmp -72
jmp -200
acc -7
jmp +1
jmp -11
acc +4
acc +12
acc -18
nop -55
jmp +9
acc +6
acc +47
jmp +273
acc +6
acc +22
acc +17
jmp +101
jmp +230
acc +3
acc -3
acc -11
nop -170
jmp -182
jmp +20
jmp +79
nop -118
acc +19
nop -52
jmp -251
acc -2
acc +36
jmp -30
nop -231
acc -19
acc +16
acc +34
jmp +169
jmp -69
acc +49
acc +41
acc +41
acc +29
jmp +184
acc +35
jmp -116
jmp +320
acc +48
acc +16
acc +16
jmp +66
nop +2
jmp -167
acc +16
nop -202
acc +30
jmp +306
acc +42
nop -211
acc +21
acc -12
jmp +11
nop +122
acc -2
jmp +195
acc +19
jmp -196
jmp +327
acc -9
acc +49
acc +36
jmp -206
acc +11
acc +17
acc +1
jmp -139
acc +41
acc +0
jmp -132
acc +12
acc -14
acc +2
jmp +197
acc +24
acc +49
acc -12
acc +33
jmp +140
acc +17
acc +43
acc -9
jmp -105
acc -14
acc +29
acc +50
acc -5
jmp -188
acc +4
acc +27
jmp -184
nop -248
acc +39
acc +48
jmp -208
nop -198
jmp -210
acc -8
nop -192
jmp +44
jmp +241
jmp +87
nop -81
acc +39
jmp +265
acc +4
jmp -259
jmp +217
jmp +24
jmp +59
jmp -22
nop +70
nop +199
nop +36
acc +44
jmp +60
jmp +1
acc -2
jmp +17
acc -2
acc -17
jmp +1
acc -10
jmp +196
acc -11
acc -10
jmp +193
acc -17
jmp +149
acc +32
nop -19
jmp -87
jmp -311
acc +46
jmp -39
nop +189
nop -275
acc +20
nop -360
jmp -278
acc +24
acc +20
jmp +152
jmp -376
acc +4
acc -10
nop +228
nop -268
jmp -198
acc +28
acc -11
acc +45
jmp -196
acc +47
acc +1
acc -11
acc +33
jmp -62
acc +45
jmp -372
acc +47
acc -4
acc -14
acc -2
jmp -85
acc +36
jmp -181
jmp -132
nop -399
jmp +36
nop -369
acc +3
acc -19
acc -13
jmp +114
acc -9
acc +36
nop +186
jmp -228
acc +14
jmp -230
nop +188
acc +50
acc +10
jmp +1
jmp -416
acc -6
jmp +37
acc +43
nop -244
nop -180
jmp -359
acc -3
acc +42
acc -9
acc +1
jmp -375
acc +13
nop -49
acc -8
acc +13
jmp -325
acc +0
acc -17
jmp -328
acc -6
jmp -118
acc +13
jmp -129
acc +28
acc +14
acc +4
acc +41
jmp +161
acc -16
acc +25
acc -6
jmp +16
acc +3
nop -61
acc +2
acc +13
jmp -57
jmp -91
acc +19
nop -20
acc -7
acc +39
jmp +135
acc +0
acc +33
acc +30
jmp -465
nop -198
nop -396
acc +3
acc +26
jmp -167
jmp -282
acc -2
acc -6
nop +29
jmp +104
acc +23
acc +19
jmp -366
jmp -217
nop +99
acc -11
jmp -471
nop -483
acc -15
acc +13
acc -19
jmp +127
acc +45
acc +2
acc +10
acc +21
jmp -35
jmp +1
acc -12
acc +35
acc +47
jmp -229
acc +44
acc +16
nop -435
acc -18
jmp -142
acc +27
acc +37
acc -8
jmp -268
acc -17
acc +42
jmp -507
jmp -59
acc +29
acc -4
jmp -112
acc +29
nop -474
nop -164
jmp -476
acc +17
acc +46
jmp -431
jmp -130
acc +8
acc +46
acc +38
nop -42
jmp -515
jmp -129
jmp -416
acc +9
jmp -148
acc -9
acc -16
acc -13
jmp -534
nop -382
acc +39
nop -44
acc +19
jmp -97
acc +9
acc +10
acc +47
jmp -167
nop -490
nop -16
jmp +16
acc +45
acc +9
acc +39
acc -10
jmp +56
jmp -504
acc +17
acc -4
acc +30
jmp -467
nop -30
acc +6
acc +17
jmp -311
jmp -351
acc +18
acc +10
jmp -441
jmp -401
acc +47
acc -8
nop -319
jmp -112
nop -26
acc +15
nop -372
jmp -380
acc -6
jmp -54
acc +4
acc +25
jmp -335
acc -2
acc +41
nop -241
jmp -479
acc +39
acc +10
jmp -194
jmp -51
acc -1
acc +17
jmp -96
jmp -76
acc +22
acc +14
jmp -79
jmp -535
jmp -21
jmp -334
acc +4
acc +0
acc -10
acc +38
jmp -482
jmp +1
acc -17
acc +3
jmp -458
jmp -27
jmp +1
acc -16
jmp -479
acc -18
acc -1
acc -1
jmp -510
acc -17
jmp -194
nop -133
jmp -15
acc +17
acc +5
acc +38
acc +39
jmp +1"""

input_split = input.split('\n')

def evaluate_commands(input_list):

    _COMMAND_REGEX = r'(?P<command>[a-z]+)\s(?P<offset>(\+|-)\d+)'

    _SEEN_COMMANDS = []
    _repeated_instruction_seen = False
    _command_index = 0
    _ACCUMULATOR = 0

    while _repeated_instruction_seen is False:
        if _command_index >= len(input_list):
            return _ACCUMULATOR
        if (_command_index, input_list[_command_index]) in _SEEN_COMMANDS:
            _repeated_instruction_seen = True
            break
        else:
            _SEEN_COMMANDS.append((_command_index, input_list[_command_index]))

        if _repeated_instruction_seen is False:
            _match = re.match(_COMMAND_REGEX, input_list[_command_index])
            if _match['command'] == 'nop':
                _command_index += 1
            elif _match['command'] == 'acc':
                _ACCUMULATOR += int(_match['offset'])
                _command_index += 1
            elif _match['command'] == 'jmp':
                _command_index += int(_match['offset'])
        else:
            break

COMMAND_REGEX = r'(?P<command>[a-z]+)\s(?P<offset>(\+|-)\d+)'

SEEN_COMMANDS = []
repeated_instruction_seen = False
command_index = 0
ACCUMULATOR = 0

while repeated_instruction_seen is False:
    if (command_index, input_split[command_index]) in SEEN_COMMANDS:
        repeated_instruction_seen = True
        break
    else:
        SEEN_COMMANDS.append((command_index, input_split[command_index]))

    if repeated_instruction_seen is False:
        match = re.match(COMMAND_REGEX, input_split[command_index])
        if match['command'] == 'nop':
            command_index += 1
        elif match['command'] == 'acc':
            ACCUMULATOR += int(match['offset'])
            command_index += 1
        elif match['command'] == 'jmp':
            command_index += int(match['offset'])
    else:
        break

# Populate seen commands
# Go through seen commands, and vary the jmp and nop commands within
for entry in SEEN_COMMANDS:
    if entry[1][0:3] == 'nop':
        edited_command_list = copy.deepcopy(input_split)
        edited_command_list[entry[0]] = 'jmp' + entry[1][3:]
        if evaluate_commands(edited_command_list) is not None:
            print(evaluate_commands(edited_command_list))
            break 
    elif entry[1][0:3] == 'jmp':
        edited_command_list = copy.deepcopy(input_split)
        edited_command_list[entry[0]] = 'nop' + entry[1][3:]
        if evaluate_commands(edited_command_list) is not None:
            print(evaluate_commands(edited_command_list))
            break