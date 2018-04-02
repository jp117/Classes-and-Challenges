def palindrome(s):
	ps = s[::-1]
	if s == ps:
		return True
	else: 
		return False
print(palindrome('helleh'))