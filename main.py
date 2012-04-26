import random
import pygame           #load pygame module
import sys
import time

w = 500                 #set width of screen
h = 500                 #set height


neighbors = [[0,-1], [0,1], [-1,-1], [-1,0], [-1,1], [1,-1], [1,0], [1,1]]

def show_fight(board, screen):
	draw(screen, board)
	pygame.display.flip()
	c = 0
	while c < 500:
		board = update(board)
		draw(screen, board)
		pygame.display.flip()
		c += 1
	return board

def run_fight(board):
	c = 0
	while c < 500:
		board = update(board)
		c += 1
	return board


def main():
	pygame.init()
	screen = pygame.display.set_mode((w, h)) #make screen

	#initialize two players
	player1 = [[random.randint(0, 1) for col in range(50)] for row in range(25)]
	player2 = [[random.randint(0, 1)*2 for col in range(50)] for row in range(25)]
	board = player1 + player2

	#clock = pygame.time.Clock()
	show = False
	while True:
		#time_passed = clock.tick(2)#fps

		t = time.time()
		#fight!
		if show:
			board = show_fight(board, screen)
		else:
			board = run_fight(board)
		#based on the winner replace the loser with another random guess
		winner = get_winner(board)
		print winner
		new_player1 = player1 if winner == 1 else [[random.randint(0, 1) for col in range(50)] for row in range(25)]
		new_player2 = player2 if winner == 2 else [[random.randint(0, 1)*2 for col in range(50)] for row in range(25)]
		board = new_player1 + new_player2
		print time.time() - t

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
				elif event.key == pygame.K_SPACE:
					show = False if show else True

def get_winner(board):
	counts = [0, 0]
	for row in range(len(board)):
		for col in range(len(board[0])):
			if board[row][col] != 0:
				counts[board[row][col] - 1] += 1
	return 1 if counts[0] > counts[1] else 2

def update(board):
	new_board = []
	for row in range(len(board)):
		new_board_row = []
		for col in range(len(board[0])):
			sums = [0, 0]
			for n in neighbors:
				new_row = (row + n[0]) % 50
				new_col = (col + n[1]) % 50
				if board[new_row][new_col] != 0:
					player = board[new_row][new_col] - 1
					sums[player] += 1
			comparison = cmp(sums[1], sums[0])
			new_player = board[row][col] - 1 if comparison == 0 else (comparison + 1) / 2 + 1
			total = sums[0] + sums[1]
			if board[row][col] == 0:
				if total == 3:
					new_board_row.append(new_player)
				else:
					new_board_row.append(0)
			else:
				if total != 2 and total !=3:
					new_board_row.append(0)
				else:
					new_board_row.append(new_player)
		new_board.append(new_board_row)
	return new_board

def draw(screen, board):
	tile_size = 10
	#pygame.draw.line(screen, (255, 0, 0), (0, 0), (w, h))
	for row in range(len(board)):
		for col in range(len(board[0])):
			pygame.draw.rect(screen, (0, (board[row][col])*100, 0), (col*tile_size, row*tile_size, tile_size, tile_size))


if __name__ == '__main__': main()
