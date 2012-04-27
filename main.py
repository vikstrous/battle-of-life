import random
import pygame
import sys
import time

grid_h = 100
grid_w = 100
tile_size = 10

w = grid_w * tile_size
h = grid_h * tile_size


neighbors = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [1, -1],
            [0, -1],
            [0, 1],
            [1, 0],
            [1, 1]]


def show_fight(board, screen):
    draw(screen, board)
    pygame.display.flip()
    c = 0
    while c < 200:
        board = update(board)
        draw(screen, board)
        pygame.display.flip()
        c += 1
    return board


def run_fight(board):
    c = 0
    while c < 200:
        board = update(board)
        c += 1
    return board


def main():
    pygame.init()
    screen = pygame.display.set_mode((w, h))

    #initialize two players
    global grid_h
    global grid_w
    global player1
    global player2
    global player3
    global player4
    global player5
    global board

    player1 = 0
    player2 = 0
    player3 = 0
    player4 = 0
    player5 = 0
    board = 0

    def init():
        # global player1
        # global player2
        # global player3
        # global player4
        # global player5
        global board
        # player1 = [[random.randint(0, 1) for col in range(50)] for row in range(10)]
        # player2 = [[random.randint(0, 1)*2 for col in range(50)] for row in range(10)]
        # player3 = [[random.randint(0, 1)*3 for col in range(50)] for row in range(10)]
        # player4 = [[random.randint(0, 1)*4 for col in range(50)] for row in range(10)]
        # player5 = [[0 for col in range(50)] for row in range(10)]
        # board = player1 + player2 + player3 + player4 + player5
        board = [[
         random.randint(0, 1) if col < grid_w / 2 and row < grid_h / 2 else (
         random.randint(0, 1) * 2 if col < grid_w / 2
            and row > grid_h / 2 else (
         random.randint(0, 1) * 3 if col > grid_w / 2
            and row < grid_h / 2 else (
         random.randint(0, 1) * 4 if col > grid_w / 2
            and row > grid_h / 2 else 0)))
            for col in range(grid_w)] for row in range(grid_h)]

    init()
    #clock = pygame.time.Clock()
    show = True
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
        # new_player1 = player1 if winner == 1 else [[random.randint(0, 1) for col in range(50)] for row in range(25)]
        # new_player2 = player2 if winner == 2 else [[random.randint(0, 1)*2 for col in range(50)] for row in range(25)]
        # board = new_player1 + new_player2
        init()
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
    counts = [0, 0, 0, 0]
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != 0:
                counts[board[row][col] - 1] += 1
    return counts.index(max(counts))


def update(board):
    global grid_h
    global grid_w
    new_board = []
    for row in range(len(board)):
        new_board_row = []
        for col in range(len(board[0])):
            sums = [0, 0, 0, 0]
            for n in neighbors:
                new_row = (row + n[0]) % grid_h
                new_col = (col + n[1]) % grid_w
                if board[new_row][new_col] != 0:
                    player = board[new_row][new_col] - 1
                    sums[player] += 1

            #decide what color this tile will become!
            my_max = max(sums)
            #if it's not a tie we change!
            if sums.count(my_max) == 1:
                biggest = sums.index(my_max)
                new_player = biggest + 1
            else:
                new_player = board[row][col]
            total = sum(sums)
            if board[row][col] == 0:
                if total == 3:
                    new_board_row.append(new_player)
                else:
                    new_board_row.append(0)
            else:
                if total != 2 and total != 3:
                    new_board_row.append(0)
                else:
                    new_board_row.append(new_player)
        new_board.append(new_board_row)
    return new_board


def draw(screen, board):
    global tile_size
    #pygame.draw.line(screen, (255, 0, 0), (0, 0), (w, h))
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 1:
                pygame.draw.rect(screen, (20, 180, 250),
                    (col * tile_size, row * tile_size, tile_size, tile_size))
            elif board[row][col] == 2:
                pygame.draw.rect(screen, (250, 180, 20),
                    (col * tile_size, row * tile_size, tile_size, tile_size))
            elif board[row][col] == 3:
                pygame.draw.rect(screen, (200, 200, 200),
                    (col * tile_size, row * tile_size, tile_size, tile_size))
            elif board[row][col] == 4:
                pygame.draw.rect(screen, (50, 200, 50),
                    (col * tile_size, row * tile_size, tile_size, tile_size))
            else:
                pygame.draw.rect(screen, (0, 0, 0),
                    (col * tile_size, row * tile_size, tile_size, tile_size))


if __name__ == '__main__':
    main()
