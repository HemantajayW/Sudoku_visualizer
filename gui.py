import pygame
import requests
import sudoko_solve as solve
import time


Width = 550
background_clr = (0, 0, 0)
buffer = 3

colors = [(255, 237, 111), (132, 213, 164), (192, 89, 203), (208, 83, 61),
          (206, 169, 83), (145, 212, 75), (205, 91, 137), (121, 126, 203), (251, 128, 114)]
colors1 = [(186, 0, 191), (186, 0, 255), (124, 0, 255), (0, 0, 255), (0,
                                                                      92, 255), (0, 146, 255), (141, 212, 255), (62, 161, 204), (190, 128, 255)]


def solveBoard(board, win):
    time.sleep(0.05)
    empty = solve.find_empty(board)
    if(empty is None):
        return True

    x, y = empty[0], empty[1]
    print("solviing", x, y)
    for ele in range(1, len(board)+1):
        if(solve.isSafe(board, x, y, ele)):
            board[x][y] = ele
            forward(win, (x+1, y+1), ele)
            if(solveBoard(board, win)):
                return True
            backward(win, (x+1, y+1), ele)
            board[x][y] = 0
    return False


def forward(win, position, ele):
    i, k = position[1], position[0]
    myfont = pygame.font.SysFont('Poppins', 35)
    pygame.draw.rect(win, (0, 255, 0), (i*50, k*50, 50, 50), 2)
    value = myfont.render(
        str(ele), True, colors1[ele-1])
    win.blit(value, ((i)*50+15, (k)*50+15))

    pygame.display.update()


def backward(win, position, ele):
    i, k = position[1], position[0]
    myfont = pygame.font.SysFont('Poppins', 35)
    pygame.draw.rect(win, (0, 0, 0), (i*50 +
                                      buffer, k*50+buffer, 50-buffer, 50-buffer))
    pygame.draw.rect(win, (255, 0, 0), (i*50, k*50, 50, 50), 2)
    value = myfont.render(
        str(" "), True, colors1[ele-1])
    win.blit(value, ((i)*50+15, (k)*50+15))

    pygame.display.update()


def insert(win, position,grid):
    i, k = position[1], position[0]
    myfont = pygame.font.SysFont('Poppins', 35)

    print(i, k)
    if(0 < i < 10 and 0 < k < 10):
        pygame.draw.rect(win, (255, 255, 255), (k*50 +
                                                buffer, i*50+buffer, 50-buffer, 50-buffer))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:

                    if grid[i-1][k-1] != 0:
                        return
                    if(event.key == 48):
                        grid[i-1][k-1] = 0
                        pygame.draw.rect(win, background_clr, (k*50 +
                                                               buffer, i*50+buffer, 50-buffer, 50-buffer))
                        pygame.display.update()
                    if(0 < event.key-48 < 10):
                        grid[i-1][k-1]=event.key-48
                        print("event : ", event.key-48)
                        pygame.draw.rect(win, background_clr, (k*50 +
                                                               buffer, i*50+buffer, 50-buffer, 50-buffer))
                        value = myfont.render(
                            str(event.key-48), True, colors1[event.key-48-1])
                        win.blit(value, ((k)*50+15, (i)*50+15))
                        pygame.display.update()
                        return
    elif(i == 11 and 4 <= k <= 6):
        pygame.draw.rect(win, (0, 0, 0), [190, 550, 150, 50])
        pygame.draw.rect(win, (255, 255, 255), [190, 550, 150, 50], 3)
        value = myfont.render(
            "SOLVING..", True, (255, 255, 255))
        win.blit(value, (208, 565))
        pygame.display.update()
        solveBoard(grid, win)
        pygame.draw.rect(win, (0, 0, 0), [190, 550, 150, 50])
        pygame.draw.rect(win, (255, 255, 255), [190, 550, 150, 50], 3)
        value = myfont.render(
            "SOLVED", True, (255, 255, 255))
        win.blit(value, (215, 565))
        pygame.display.update()
        return


def main():
    pygame.init()
    win = pygame.display.set_mode((Width, Width+100))
    pygame.display.set_caption("SUDOKU")
    win.fill((0, 0, 0))
    myfont = pygame.font.SysFont('Poppins', 35)
    menu(win)


def menu(win):
    myfont = pygame.font.Font('RussoOne-Regular.ttf', 56)
    myfont1 = pygame.font.Font('Sacramento-Regular.ttf', 68)
    myfont2 = pygame.font.Font('RussoOne-Regular.ttf', 24)

    value = myfont.render(
        str("SUDOKO"), True, colors1[0])
    win.blit(value, (150, 150))
    value = myfont1.render(
        str("Solver"), True, (255, 255, 255
                              ))
    win.blit(value, (180, 165))
    pygame.draw.rect(win, (255, 255, 255), [150, 275, 250, 50], 3)
    value = myfont2.render(
        "1. Easy Board", True, (255, 255, 255))
    win.blit(value, (190, 285))
    pygame.draw.rect(win, (255, 255, 255), [150, 345, 250, 50], 3)
    value = myfont2.render(
        "2. Med Board", True, (255, 255, 255))
    win.blit(value, (190, 355))
    pygame.draw.rect(win, (255, 255, 255), [150, 415, 250, 50], 3)
    value = myfont2.render(
        "3. Hard Board", True, (255, 255, 255))
    win.blit(value, (190, 425))
    pygame.draw.rect(win, (255, 255, 255), [150, 485, 250, 50], 3)
    value = myfont2.render(
        "4. Custom Board", True, (255, 255, 255))
    win.blit(value, (180, 495))
    # pygame.display.update()

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos)
                level = 1
                if(150 <= pos[0] <= 400):
                    if(275 <= pos[1] <= 325):
                        response = requests.get(
                            "https://sugoku.herokuapp.com/board?difficulty=easy")
                        grid_ = response.json()['board']
                        grid = [[grid_[x][y] for y in range(
                            len(grid_))]for x in range(len(grid_))]

                        board(win, grid)
                        return
                    elif(345 <= pos[1] <= 395):
                        response = requests.get(
                            "https://sugoku.herokuapp.com/board?difficulty=medium")
                        grid_ = response.json()['board']
                        grid = [[grid_[x][y] for y in range(
                            len(grid_))]for x in range(len(grid_))]

                        board(win, grid)
                        return

                    elif(415 <= pos[1] <= 465):
                        response = requests.get(
                            "https://sugoku.herokuapp.com/board?difficulty=hard")
                        grid_ = response.json()['board']
                        grid = [[grid_[x][y] for y in range(
                            len(grid_))]for x in range(len(grid_))]

                        board(win, grid)
                        return
                    elif(485 <= pos[1] <= 535):
                        grid = [[0 for y in range(9)]for x in range(9)]
                        board(win, grid)
                        return

            if event.type == pygame.QUIT:
                pygame.quit()
                return


def board(win, grid):
    pygame.draw.rect(win, (0, 0, 0), [0, 0, 550, 650])
    myfont = pygame.font.SysFont('Poppins', 35)

    for i in range(0, 10):
        if(i % 3 == 0):
            pygame.draw.line(win, (255, 255, 255),
                             (50+50*i, 50), (50+50*i, 500), 5)
            pygame.draw.line(win, (255, 255, 255),
                             (50, 50+50*i), (500, 50+50*i), 5)
        else:
            pygame.draw.line(win, (251, 247, 245),
                             (50+50*i, 50), (50+50*i, 500), 2)
            pygame.draw.line(win, (251, 247, 245),
                             (50, 50+50*i), (500, 50+50*i), 2)

    for i in range(len(grid)):
        for k in range(len(grid)):
            if(0 < grid[i][k] < 10):
                value = myfont.render(
                    str(grid[i][k]), True, colors1[grid[i][k]-1])
                win.blit(value, ((k+1)*50+15, (i+1)*50+15))
    pygame.draw.rect(win, (255, 255, 255), [210, 550, 130, 50], 3)
    value = myfont.render(
        "SOLVE", True, (255, 255, 255))
    win.blit(value, (235, 565))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50),grid)

            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()
