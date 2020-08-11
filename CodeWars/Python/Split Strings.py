# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

from textwrap import wrap
def solution(s):
    x = wrap(s, 2)
    List = []
    for i in range(len(x)):
        if len(x[i]) == 2:
            List.append(x[i])
        elif len(x[i]) == 1:
            List.append(x[i]+'_')
    return List