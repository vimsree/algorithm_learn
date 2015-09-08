__author__ = 'vimsree'

import random


def monkeyonkeyboard():
    match_string = "methinks it is like a weasel"
    count = 1;
    closest_match = []
    while True:
        generated_string  = generatestring()
        validation = validatestring(match_string,generated_string)
        if validation[0] == True:
            print("Perfect Match at %d : %s"%(count,generated_string))
            break
        if validation[1] == True:
            closest_match.append(generated_string)
        if not count%1000:
            print("At iteration %d:"%(count))
            print("Absolute Matches %d"%len(closest_match))
        count = count+1


def generatestring():
    string_out = ''
    for i in range(27):
        string_out = string_out + (random.choice(' abcdefghijklmnopqrstuvwxyxz'))
    return string_out


def validatestring(match_string,generated_string):
    perfect_match = False
    absolute_match = False
    match_split_words = set(match_string)
    generated_split_words = set(generated_string)
    if len(generated_split_words - match_split_words) == 0:
        perfect_match = True
        return [perfect_match,absolute_match]
    elif len(generated_split_words-match_split_words) < 3:
        absolute_match = True
        return [perfect_match,absolute_match]
    else:
        return [perfect_match,absolute_match]


monkeyonkeyboard()

