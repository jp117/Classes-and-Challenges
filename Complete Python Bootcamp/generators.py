'''
Yield is more memory efficient when you don't need to actually call a list.  To do the below function, 
we would have made a blank list and appended to it then called the values in the list one by one.  
Doing this steps through one at a time but only stores one answer in memory at a time.  If you don't
need the full list, you are better off just stepping through one at a time.  

Use yield instead of return and don't make a blank list and append to it
'''

def create_cubes(n):
    for x in range (n):
        yield x**3

for x in create_cubes(10):
    print(x)


def gen_fibon(n):
    a = 1
    b = 1
    for i in range (n):
        yield a
        a,b = b,a+b

for number in gen_fibon(10):
    print(num)


def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

#Setting g to the generator function
g = simple_gen()

#finding the next iteration of simple gen and printing it.  In this case, we are at index '0'
print(next(g))

#finding the iteration after the one above.  In this case, like index '1'
print(next(g))

#If you call next too often, you can get a stop iteration error for going too far

s = 'hello'
#Cannot use 'next' for strings.  must use iter to make a string iterator
s_iter= iter(s)

#Goes to the next from the iteration of the string, or string index 0 essentially
print(next(s_iter))