# https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python

# James Hull

# Original Solution
def check(seq, elem):
    if elem in seq:
        return True
    return False

# Revised Solution
def check(seq, elem):
    return elem in seq: