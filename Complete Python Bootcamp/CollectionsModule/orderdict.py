'''
OrderedDict remembers the order that things were added to the dictionary
'''

d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6

for k,v in d.items():
    print(k,v)
#will print the dictionary, but not necessarily in order bc dicitonaries don't store in order



from collections import OrderedDict

d = OrderedDict()

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6

for k,v in d.items():
    print (k,v)
#Will print the dictionary in order bc it was mapped in order