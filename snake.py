import pygame
import random
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("SNAKE by vinayak")
pygame.display.update()
icon = pygame.image.load('snake (1).png')
pygame.display.set_icon(icon)
size1 = 15
size2 = 15
black = (0, 0, 0)
fps = 600

clock = pygame.time.Clock()

#background
mixer.music.load('background.wav')
mixer.music.play(-1)


# font
font = pygame.font.Font('freesansbold.ttf', 32)


def game(x, y):
    game = font.render("GAME OVER", True, (255, 0, 0))
    real = font.render("PRESS ENTER TO PLAY AGAIN", True, (255, 0, 0))
    screen.blit(game, (x, y))
    screen.blit(real, (8, 260))


def sn_len(screen, black, snake_lst, size1, size2):
    for x, y in snake_lst:
        pygame.draw.rect(screen, black, [x, y, size1, size2])


############# game loop ##########


def loop():
    snakex = 250
    snakey = 250
    snake_changex = 0
    snake_changey = 0
    size1 = 15
    size2 = 15
    black = (0, 0, 0)
    fps = 600
    foodx = random.randint(0, 400)
    foody = random.randint(0, 400)
    color = (0, 0, 255)

    snake_lst = []
    snake_len = 1
    sc = 0
    textx = 10
    texty = 10

    def score_val(x, y):
        score = font.render("Score:" + str(sc * 10), True, (255, 120, 0))
        screen.blit(score, (x, y))

    running = True
    gameover = True
    while running:
        if not gameover:
            screen.fill((0, 0, 0))
            game(160, 220)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        loop()



        else:

            screen.fill((0, 150, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        snake_changex = 0.8
                        snake_changey = 0

                    if event.key == pygame.K_LEFT:
                        snake_changex = -0.8
                        snake_changey = 0

                    if event.key == pygame.K_UP:
                        snake_changey = -0.8
                        snake_changex = 0

                    if event.key == pygame.K_DOWN:
                        snake_changey = 0.8
                        snake_changex = 0
            snakex = snakex + snake_changex
            snakey = snakey + snake_changey
            if snakex >= 480 or snakex <= 0 or snakey >= 480 or snakey <= 0:
                gameover = False

            pygame.draw.rect(screen, color, [foodx, foody, 15, 15])

            if abs(foodx - snakex) < 10 and abs(foody - snakey) < 10:
                sou=mixer.Sound('laser.wav')
                sou.play()
                foodx = random.randint(0, 400)
                foody = random.randint(0, 400)
                snake_len += 20
                sc += 1
                pygame.display.update()
                clock.tick(120)

            score_val(textx, texty)

            head = []
            head.append(snakex)
            head.append(snakey)
            snake_lst.append(head)

            if len(snake_lst) > snake_len:
                del snake_lst[0]

            if head in snake_lst[:-1]:
                gameover = False

            sn_len(screen, black, snake_lst, size1, size2)

        pygame.display.update()
    clock.tick(fps)


loop()
