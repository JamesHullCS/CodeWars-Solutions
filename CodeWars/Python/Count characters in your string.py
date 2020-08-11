# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

def count(string):

    all_freq = {} 
    for i in string: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    return all_freq


from collections import Counter
def count(string):
    return Counter(string)