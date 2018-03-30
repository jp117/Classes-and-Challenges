def summer_69(arr):
	newlist = []
	for x in range (0,len(arr)):
		if arr[x]!=6 and arr[x]!=7 and arr[x]!=8 and arr[x]!=9:
			newlist.append(arr[x])
	return sum(newlist)

print(summer_69([4,5,6,7]))