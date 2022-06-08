#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    scs = list(a_dictionary.keys())[0]
    biggest = a_dictionary[scs]
    for key, value in a_dictionary.items():
        if value > biggest:
            biggest = value
            scs = key
    return scs
