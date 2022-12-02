
import pygame
import os
# TODO: random 라이브러리 불러오기

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

START_X = 80
START_Y = 310
JUMP_VEL = 8.5

# 게임을 보여줄 스크린
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 공룡, 선인장, 배경 이미지
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
        # TODO: 필요한 속성 추가하기
        self.image_run = RUNNING
        self.image_jump = JUMPING
        self.image = self.image_run[0]
        self.step = 0

        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = START_X
        self.dino_rect.y = START_Y

    def update(self, userInput):
        # TODO: 1. run(), jump() 실행하기
        # TODO: 2. ↑ 버튼을 누를 때마다 점프하기

        if self.step >= 10:
            self.step = 0

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
        self.type = 0          # TODO: type 값을 바꿔 랜덤으로 선인장이 나오도록 만들기
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 325

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        # TODO: 화면에 선인장 그리기
        print("SmallCactus draw!")


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

    # TODO: Dinosaur 클래스 변수 만들기

    def score():
        global points, game_speed
        # TODO: 게임 점수 증가시키기
        # TODO: 게임 점수가 100 늘어날 때마다 게임 속도 증가시키기

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

        # TODO: 화면에 공룡 그리기
        # TODO: 플레이어에게 ↑ 입력받기
        # TODO: 공룡 이미지 바꾸기

        if len(obstacles) == 0:
            obstacles.append(SmallCactus(SMALL_CACTUS))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()

            # TODO: 공룡이 선인장과 충돌하면 게임 종료


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
