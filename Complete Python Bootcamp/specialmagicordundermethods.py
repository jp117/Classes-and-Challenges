class Book():

	def __init__(self,title,author,pages):

		self.title = title
		self.author = author
		self.pages = pages

	'''
	In order to call python main functions like "print()", you need to input a __main__ function
	to return a string with print, use below.  Now print(mybook) will print the title and author.
	'''
	def __str__(self):
		return f'{self.title} by {self.author}'

	''' 
	and now for length of book
	'''
	def __len__(self):
		return: self.pages

	'''
	If you want a message while deleting an instance of the book
	'''
	def __del__(self):
		print('A book object has been deleted')
