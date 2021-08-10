import pygame
import random
import time

pygame.init()

# 색상 정하기
BLACK = (0, 0, 0)
RED = (245, 22, 22)
YELLOW = (255, 252, 69)
large_font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))  # 화면 설정

done = False
clock = pygame.time.Clock()


def runGame():
    global done
    score = 0
    start_time = int(time.time())
    remain_time = 0
    game_over = 0

    bug_image = pygame.image.load('bug.png')  # 이미지 갖고오기
    bug_image = pygame.transform.scale(bug_image, (60, 80))
    bugs = []
    for i in range(3):  # 벌레 움직임 좌표
        bug = pygame.Rect(bug_image.get_rect())
        bug.left = random.randint(0, screen_width)
        bug.top = random.randint(0, screen_height)
        dx = random.randint(-9, 9)
        dy = random.randint(-9, 9)
        bugs.append((bug, dx, dy))

    while not done:
        clock.tick(30)  # 시간 설정
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # [X] 종료키가 누르면, 게임 종료
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and game_over == 0:
                print(event.pos[0], event.pos[1])
                for (bug, dx, dy) in bugs:
                    if bug.collidepoint(event.pos):  # 벌레를 잡으면 점수가 올라감
                        print(bug)
                        bugs.remove((bug, dx, dy))
                        bug = pygame.Rect(bug_image.get_rect())
                        bug.left = random.randint(0, screen_width)
                        bug.top = random.randint(0, screen_height)
                        dx = random.randint(-9, 9)
                        dy = random.randint(-9, 9)
                        bugs.append((bug, dx, dy))
                        score += 1

        if game_over == 0:
            for (bug, dx, dy) in bugs:
                bug.left += dx
                bug.top += dy

            remain_time = 60 - (int(time.time()) - start_time)

            if remain_time <= 0:
                game_over = 1

        for (bug, dx, dy) in bugs:
            screen.blit(bug_image, bug)

        for (bug, dx, dy) in bugs:
            if not bug.colliderect(screen.get_rect()):
                bugs.remove((bug, dx, dy))
                bug = pygame.Rect(bug_image.get_rect())
                bug.left = random.randint(0, screen_width)
                bug.top = random.randint(0, screen_height)
                dx = random.randint(-9, 9)
                dy = random.randint(-9, 9)
                bugs.append((bug, dx, dy))

        score_image = small_font.render(
            'Point {}'.format(score), True, YELLOW)  # 점수
        screen.blit(score_image, (10, 10))

        remain_time_image = small_font.render(
            'Time {}'.format(remain_time), True, YELLOW)  # 시간
        screen.blit(remain_time_image, (screen_width -
                                        10 - remain_time_image.get_width(), 10))

        if game_over == 1:
            game_over_image = large_font.render(
                'GameOver', True, RED)  # 시간종료알림
            screen.blit(game_over_image, (screen_width // 2 - game_over_image.get_width() //
                                          2, screen_height // 2 - game_over_image.get_height() // 2))

        pygame.display.update()


runGame()
pygame.quit()
