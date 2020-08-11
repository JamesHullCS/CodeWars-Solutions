# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number):
	List = []
	for i in range(number):
		if i % 5 == 0 and i % 3 == 0 and i != None:
			List.append(i)
		elif i % 5 == 0 and i % 3 != 0 and i != None:
			List.append(i)
		elif i % 3 == 0 and i % 5 != 0 and i != None:
			List.append(i)

	return sum(List)

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

print(solution(15))