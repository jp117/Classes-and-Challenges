def myfunc(mystring):
	mylist = list(mystring)
	for x in range (0, len(mylist)):
		if x % 2 == 0:
			mylist[x] = mylist[x].upper()
		else:
			mylist[x] = mylist[x].lower()
	mystring = ''.join(mylist)
	return mystring