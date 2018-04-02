def up_low(s):
	myList = []
	Up = 0
	Down = 0
	for x in range (0,len(s)):
		myList.append(s[x])
	for x in range (0,len(s)):
		if myList[x].isupper() == True:
			Up += 1
		else:
			Down += 1
	return f'No of Upper case characters : {Up} \n No of Lower case characters : {Down}'

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))