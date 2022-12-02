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
        self.pos_x = START_X
        self.pos_y = START_Y
        self.jump_vel = JUMP_VEL
        
        self.image_run = RUNNING
        self.image_jump = JUMPING

        self.is_running = True
        self.is_jumping = False

        self.step = 0
        self.image = self.image_run[0]

        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = START_X
        self.dino_rect.y = START_Y

    def update(self, userInput):
        if self.is_running:
            self.run()        
        if self.is_jumping:
            self.jump()

        if self.step >= 10:
            self.step = 0

        if userInput[pygame.K_UP] and not self.is_jumping:
            self.is_running = False
            self.is_jumping = True
        elif not self.is_jumping:
            self.is_running = True
            self.is_jumping = False

    def run(self):
        self.image = self.image_run[self.step // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.pos_x
        self.dino_rect.y = self.pos_y
        self.step += 1

    def jump(self):
        self.image = self.image_jump
        if self.is_jumping:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - JUMP_VEL:
            self.is_jumping = False
            self.jump_vel = JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class SmallCactus:
    def __init__(self, image):
        self.image = image
        self.type = random.randint(0, 2)
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 325

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles

    clock = pygame.time.Clock()

    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    font = pygame.font.Font('freesansbold.ttf', 20)

    player = Dinosaur()
    run = True

    obstacles = []
    points = 0
    
    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

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
        pressedKey = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(pressedKey)

        if len(obstacles) == 0:
            obstacles.append(SmallCactus(SMALL_CACTUS))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()

            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                menu(isAlive=False)

        background()

        score()

        clock.tick(30)
        pygame.display.update()


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
