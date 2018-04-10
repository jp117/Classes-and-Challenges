'''
iterators and generators hw
'''

'''
PROBLEM 1
Create a generator that generates squares of numbers up to some number n
'''
def gensquares(n):
    for x in range(n):
        yield x**2

for x in gensquares(10):
    print(x)


'''
PROBLEM 2
Create a generator that yields 'n' random numbers between a low and high number 
'''
import random

def rand_num(low, high, n):
    for x in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)


'''
PROBLEM 3
Use the iter() function to convert the string below into an iterator
'''
s = 'hello'
s_iter = iter(s)


'''
PROBLEM 4
Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement
'''

'''
PROBLEM 4 ANSWER
'yield' is good for memory management.  If you're not going to call a list, use yield instead of putting the list to memory.  
For example, if you need to iterate through a large range of numbers, not worth having it in memory.
'''


'''
EXTRA CREDIT
Can you explain what the gencomp is in the code below?
'''

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

'''
I believe this iterates through the items in the list and prints out items greater than 3
'''