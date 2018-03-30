def old_macdonald(name):
	mylist = []
	for x in range (0,len(name)):
		mylist.append(name[x])
	mylist[0] = mylist[0].upper()
	mylist[3] = mylist[3].upper()
	sol = ''.join(mylist)
	return sol

print(old_macdonald('macdonald'))