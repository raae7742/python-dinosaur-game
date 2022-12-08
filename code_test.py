import pygame
import os
import random

pygame.init()

# 전역 변수
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

START_X = 80
START_Y = 310
DUCK_Y = 340
JUMP_VEL = 8.5

# 게임 이미지
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]

JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))


# 공룡 클래스
class Dinosaur:

    def __init__(self):
        print("initialize Dinosaur")

    def update(self, userInput):
        print("update Dinosaur")

    def run(self):
        print("run Dinosaur")

    def jump(self):
        print("jump Dinosaur")

    def draw(self, SCREEN):
        print("draw Dinosaur")

# 선인장 클래스
class SmallCactus:
    def __init__(self, image):
        print("initialize SmallCactus")

    def update(self):
        print("update SmallCactus")

    def draw(self, SCREEN):
        print("draw SmallCactus")


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles

    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 20)

    x_pos_bg = 0
    y_pos_bg = 380
    game_speed = 20
    points = 0
    obstacles = []
    run = True

    # 점수를 계산하는 함수
    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    # 배경화면을 그리는 함수
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))

        # TODO: 게임 기능 구현하기

        clock.tick(30)

        pygame.display.update()


# 메뉴를 보여주는 함수
def menu(isAlive):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if isAlive:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        else:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(isAlive=True)
