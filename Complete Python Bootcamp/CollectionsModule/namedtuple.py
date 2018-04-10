from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age=2, breed='Lab', name='Sammy')

sam.age

#If you want to call an index but don't want to remember the spot in the index, you can name the spot.  So age is index 0, breed is index 1.  It's like a class