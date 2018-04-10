from collections import defaultdict

d = defaultdict(object)

d['one']
#This inidiates a dictonary and at index one, inserts the value 'one'


for item in d:
    print(item)
#Should print one bc one is the only value that has been added to the dictionary so far

d = defaultdict(lambda: 0)
#This will prevent errors in the dictionary.  If you call a key that has no value, instead of an error, you set the default with lambda: defaultvalue

print(d['one'])
#This will return 0 bc d hasn't declared anything for one, so the value is the default value or 0

d['two'] = 2

print(d)
#Should print two tuples in the dictionary and tell you its a dictionary.  'one' which has the default value 0 and 'two' which has the value set of 2