'''
For this challenge, create a bank account class that has two attributes:
	1. Owner
	2. Balance

and 2 methods:
	1. Deposit
	2. Withdraw

As an added requirement, withdrawlas may not exceed the available blanace.  

Instantiate your class, make serveral deposits and withdrawals and test to make sure the account can't be overdrawn
'''

class Account:

	def __init__(self,owner,balance=0):

		self.owner = owner
		self.balance = balance

	def deposit(self,amount):
		
		self.balance = self.balance + amount
		print('Deposit accepted')
		print('New balance is {bal}'.format(bal=self.balance))
		

	def withdraw(self,amount):

		if amount > self.balance:
			print('Funds unavailable')
		else:
			self.balance = self.balance - amount
			print('Withdrawal accepted')
			print('{amount} was withdrawn'.format(amount=amount))

	def __str__(self):
		return('Account Owner: {owner} \nAccount Balance: {balance}'.
			format(owner = self.owner, balance = self.balance))


acc1 = Account('Jose', 100)

print(acc1)
#Should print 2 lines with __str__ function

print(acc1.owner)
#should print 'Jose'

print(acc1.balance)
#Should print 100

acc1.deposit(50)
#should add 50 dollars to the account and print out deposit accepted and new balance 150

acc1.withdraw(75)
#should print out withdrawal accepted and 75 was withdrawn

acc1.withdraw(500)
#should print out funds unavailable 