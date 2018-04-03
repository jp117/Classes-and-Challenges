import random

def display_board(board):
	print(' | |')
	print(board[7] + "|" + board[8] + '|' + board[9])
	print(' | |')
	print('-----')
	print(' | |')
	print(board[4] + "|" + board[5] + '|' + board[6])
	print(' | |')
	print('-----')
	print(board[1] + "|" + board[2] + '|' + board[3])
	print(' | |')

def player_input():
	marker = ''
	while marker.upper() != 'X' and marker.upper() != 'O':
		marker = input('Player 1, choose X or O')
	marker = marker.upper()

	if marker == 'X':
		return('X', 'O')
	else:
		return('O', 'X')

def take_turn(board, marker, spot):
	board[spot] = marker

def choose_first():
	flip = random.randint(0,1)

	if flip == 0:
		return 'Player 1'
	else:
		return 'Player 2'

def checkifempty(board, position):
	#Checks if the space has an X or O
	return board[position] == ' '

def full_board_check(board):
	for i in range (1,10):
		if checkifempty(board,i):
			return False
		#Board is full if we return true
	return True

def player_choice(board):
	position = 0

	while position not in [1,2,3,4,5,6,7,8,9] or not checkifempty(board, position):
		position = int(input('Choose a position (1-9'))
	return position

def win_logic(board,mark):
	## Check rows if all the same marker
	return ((board[1] == mark and board[2] == mark and board[3] == mark) or
	(board[4] == mark and board[5] == mark and board[6] == mark) or 
	(board[7] == mark and board[8] == mark and board[9] == mark) or
	(board[7] == mark and board[4] == mark and board[1] == mark) or
	(board[8] == mark and board[5] == mark and board[2] == mark) or
	(board[9] == mark and board[6] == mark and board[3] == mark) or
	(board[7] == mark and board[5] == mark and board[3] == mark) or
	(board[9] == mark and board[5] == mark and board[1] == mark))

print('Welcome to Tic Tac Toe')

def play_game():
	while True:
		#Play the game
		#Setup Board and who's first and who is X or O
		the_board = [' ']*10
		player1_marker, player2_marker = player_input()
		turn = choose_first()
		print(turn + ' will go first')
		play_game = input('Ready to play? y/n')
		if play_game.lower() == 'y':
			game_on = True
		else: game_on = False

		#Game play
		while game_on:
			if turn == 'Player 1':
				#show the board
				display_board(the_board)
				#choose position
				position = player_choice(the_board)
				#place the marker
				take_turn(the_board, player1_marker, position)
				#check if they won
				if win_logic(the_board, player1_marker):
					display_board(the_board)
					print('Player 1 has won!')
					game_on = False
					break
				else:
					if full_board_check(the_board):
						display_board(the_board)
						print('Full board.  Tie.  No one wins')
						game_on = False
						break
					else:
						turn = 'Player 2'
			else: #Player 2's turn
				#show the board
				display_board(the_board)
				#choose position
				position = player_choice(the_board)
				#place the marker
				take_turn(the_board, player2_marker, position)
				#check if they won
				if win_logic(the_board, player2_marker):
					display_board(the_board)
					print('Player 2 has won!')
					game_on = False
					break
				else:
					if full_board_check(the_board):
						display_board(the_board)
						print('Full board.  Tie.  No one wins')
						game_on = False
						break
					else:
						turn = 'Player 1'

		rematch = input('Would you like to play again? y/n')
		if rematch.lower() == 'y':
			pass
		else:
			print('Thanks for playing')
			break

play_game()