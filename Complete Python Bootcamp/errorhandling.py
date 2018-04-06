def add(n1, n2):
	print(n1+n2)

number1 = 10
number2 = input('Please provide a number')

#add(number1, number2)

print('i want to see this line')

#If you run this, number2 is a string bc its in input
#this will cause an error.  

'''
fix with try block
'''

try: 
	#want to attempt this code
	add(number1, number2)
except:
	#if it fails, attempt this
	print('Hey it looks like you aren\'t adding correctly')
else:
	#if it doesn't fail, do this
	print('Add went well!')
finally:
	#If pass or fail, do this code after regardless
	print('Rest of the app')

def ask_for_int():
	while True:
		try:
			result = int(input('Please provide a number: '))
		except:
			print('Whoops that\'s not a number')
			continue
		else:
			print('Yes thank you')
		finally:
			print('End of try / except / finally')

ask_for_int()
'''
Running this will ask for a number.  
if you input a number, it will print stuff with no error
if you don't, it will error and ask you to enter again
'''