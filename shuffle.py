import random
import copy

"""
This function returns a new list that is created by shuffling the elements of the
provided list
:param li: The list to be shuffled
:return shuffled_list: The shuffled list
"""

user_list = input("Put a few comma separated characters\n").split(',')


def shuffle(li):
	list = []
	for p in range(0,len(li)):
		x = random.randint(0,len(li)-1)
		print(x)
		list.append(li[x])
	return list

print(shuffle(user_list))
