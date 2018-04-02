def display_board(board):
	print(board[7] + "|" + board[8] + '|' + board[9])
	print('-----')
	print(board[4] + "|" + board[5] + '|' + board[6])
	print('-----')
	print(board[1] + "|" + board[2] + '|' + board[3])

def player_input():
	marker = ''
	while marker.upper() != 'X' and marker.upper() != 'O':
		marker = input('Player 1, choose X or O')
	player1 = marker.upper()

	if player1 == 'X':
		player2 = 'O'
		print('Player1 is X')
		print('Player2 is O')
	else:
		player2 = 'X'
		print('Player1 is O')
		print('Player2 is X')
	return(player1, player2)

def new_game():
	new_board = [' ']*10
	display_board(new_board)
	player_input()

new_game()