def unique_list(lst):
	ul = [lst[0]]
	for x in range (0,len(lst)-1):
		if lst[x] != lst[x+1]:
			ul.append(lst[x+1])
	return ul

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))