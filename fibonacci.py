'''
Write a program that, given the index, will calculate
the n-th number in the fibonacci sequence.
The fibonacci sequence is defined as 
f(x) = 
	| x == 0     = 0
	| x == 1     = 1
	| otherwise  = f(x - 1) + f(x - 2)
The index is to be read from the standard input and 
the fibonacci number at that index is to be printed
to the standard output. You may assume that your
program will be tested with valid inputs only.
'''

index = int(input())-1


# Define this function to return the expected output
# Do not print it from this function
def fib_sequence(num):
    # TODO
    if num < 2:
    	return 1
    else:
    	return fib_sequence(num-1) + fib_sequence(num-2)
    pass

print(fib_sequence(index))
