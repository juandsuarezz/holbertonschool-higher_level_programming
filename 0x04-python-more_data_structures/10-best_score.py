#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    keys = list(a_dictionary.keys())
    maxn = keys[0]
    for i in keys:
        maxn = i if a_dictionary[i] > a_dictionary[maxn] else maxn
    return maxn
