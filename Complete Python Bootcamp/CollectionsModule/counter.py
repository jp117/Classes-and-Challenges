from collections import Counter

l = [1,1,1,1,1,2,2,3,4,5,6,7,5,4]

print(Counter(l))
'''
Returns as a tuple the thing in the counter + the number of times it is in the list
for example:     x:y where x is the thing being counted and y is the number of times that thing is present
'''


'''
Common patterns when using Counter() object

sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts

'''