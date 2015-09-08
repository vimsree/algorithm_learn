__author__ = 'vimsree'

import random


def monkeyonkeyboard():
    match_string = "methinks it is like a weasel"
    match_length = len(match_string)
    position_array = list(range(0, match_length))
    generated_string = ''
    count = 1
    while True:
        generated_string = generatestring(position_array, generated_string, match_length)
        position_array = checkandmutatestrand(match_string, generated_string)
        if len(position_array) == 0:
            print("Strand Mutation Complete at %d." % count)
            break
        count = count + 1


def generatestring(position_array, string_out, match_length):
    generated_string = ''
    if string_out == '':
        for i in range(match_length):
            generated_string = generated_string+(random.choice(' abcdefghijklmnopqrstuvwxyxz'))
        print("Source Strand:\t %s"%(generated_string))
        return generated_string
    else:
        generated_list = list(string_out)
        for position in position_array:
            generated_list[position] = random.choice(' abcdefghijklmnopqrstuvwxyxz')
        generated_string = ''.join(generated_list)
        print("Mutated Strand:\t %s"%(generated_string))
        return generated_string


def checkandmutatestrand(match_string, generated_string):
    position_array = []
    for number, letter in enumerate(generated_string):
        if letter != match_string[number]:
            position_array.append(number)
    return position_array

monkeyonkeyboard()