import pygame
import random
import sys

# Constants
WIDTH, HEIGHT = 400, 600
WHITE = (255, 255, 255)
LIGHT_PINK = (255, 192, 203)
HOT_PINK = (255, 105, 180)
DEEP_PINK = (199, 21, 133)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Love on the Line 💗")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)
big_font = pygame.font.SysFont("Arial", 36)

# Splash screen
def splash_screen():
    screen.fill(LIGHT_PINK)
    title = big_font.render("LOVE ON THE LINE 💗", True, HOT_PINK)
    name = font.render("By Chrissy Johnson", True, BLACK)
    prompt = font.render("Press any key to continue", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 200))
    screen.blit(name, (WIDTH // 2 - name.get_width() // 2, 250))
    screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, 320))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return

# Instructions screen
def instructions_screen():
    screen.fill(LIGHT_PINK)
    lines = [
        "HOW TO PLAY 💕",
        "← → : Move left and right",
        "Spacebar: Jump (land on bricks)",
        "Avoid broken hearts 💔",
        "Survive 5 minutes to win LOVE 💍",
        "Press any key to start"
    ]
    for i, text in enumerate(lines):
        line = font.render(text, True, BLACK)
        screen.blit(line, (WIDTH // 2 - line.get_width() // 2, 140 + i * 40))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return

# Drawing functions
def draw_heart(surface, x, y):
    heart = pygame.Surface((40, 40), pygame.SRCALPHA)
    pygame.draw.polygon(heart, RED, [(20, 40), (0, 20), (10, 0), (20, 10), (30, 0), (40, 20)])
    surface.blit(heart, (x, y))

def draw_broken_heart(surface, x, y):
    heart = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.polygon(heart, DEEP_PINK, [(15, 25), (0, 10), (7, 0), (15, 8), (23, 0), (30, 10)])
    pygame.draw.line(heart, BLACK, (15, 8), (15, 25), 2)
    surface.blit(heart, (x, y))

# Generator functions
def get_platform(level):
    width = 100
    x = random.randint(0, WIDTH - width)
    y = random.randint(-100, -40)
    return pygame.Rect(x, y, width, 10)

def get_bug():
    x = random.randint(0, WIDTH - 30)
    y = random.randint(-200, -50)
    speed = random.choice([-2, 2])
    return {"rect": pygame.Rect(x, y, 30, 30), "speed": speed}

# Main game loop
def main_game():
    player = pygame.Rect(200, 500, 40, 40)
    vel_y = 0
    gravity = 1
    jump_power = -20
    score = 0
    level = 1
    camera_scroll = 0

    platforms = [pygame.Rect(random.randint(0, WIDTH - 100), 100 * i, 100, 10) for i in range(6)]
    bugs = []
    start_time = pygame.time.get_ticks()
    grace_period = 10000

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(LIGHT_PINK)
        elapsed = pygame.time.get_ticks() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= 5
        if keys[pygame.K_RIGHT]:
            player.x += 5
        if keys[pygame.K_SPACE] and vel_y == 0:
            vel_y = jump_power

        vel_y += gravity
        player.y += vel_y

        for plat in platforms:
            if player.colliderect(plat) and vel_y > 0:
                player.bottom = plat.top
                vel_y = 0
                score += 1

        if player.y < HEIGHT // 3:
            scroll = HEIGHT // 3 - player.y
            player.y = HEIGHT // 3
            for plat in platforms:
                plat.y += scroll
            for bug in bugs:
                bug["rect"].y += scroll
            camera_scroll += scroll

        for i in range(len(platforms)):
            if platforms[i].y > HEIGHT:
                platforms[i] = get_platform(level)

        if score % 10 == 0 and len(bugs) < 3:
            bugs.append(get_bug())

        for bug in bugs:
            bug["rect"].x += bug["speed"]
            if bug["rect"].left < 0 or bug["rect"].right > WIDTH:
                bug["speed"] *= -1

        if elapsed > grace_period and len(bugs) >= 3:
            screen.blit(font.render("Too many heartbreaks 💔", True, RED), (WIDTH // 4, HEIGHT // 2))
            pygame.display.update()
            pygame.time.wait(2000)
            break

        for bug in bugs:
            if player.colliderect(bug["rect"]):
                screen.blit(font.render("Heartbroken 💔", True, RED), (WIDTH // 3, HEIGHT // 2))
                pygame.display.update()
                pygame.time.wait(2000)
                return

        if player.top > HEIGHT:
            screen.blit(font.render("You fell for the wrong one 💔", True, RED), (WIDTH // 4, HEIGHT // 2))
            pygame.display.update()
            pygame.time.wait(2000)
            return

        if elapsed >= 5 * 60 * 1000:
            screen.fill(WHITE)
            pygame.draw.circle(screen, GOLD, (WIDTH // 2, HEIGHT // 2), 40)
            pygame.draw.circle(screen, LIGHT_PINK, (WIDTH // 2, HEIGHT // 2), 20)
            pygame.draw.polygon(screen, WHITE, [(WIDTH // 2 - 10, HEIGHT // 2 - 40),
                                                 (WIDTH // 2, HEIGHT // 2 - 60),
                                                 (WIDTH // 2 + 10, HEIGHT // 2 - 40)])
            screen.blit(font.render("You won love 💍", True, HOT_PINK), (WIDTH // 2 - 60, HEIGHT // 2 + 60))
            pygame.display.update()
            pygame.time.wait(4000)
            return

        level = 1 + score // 20

        for plat in platforms:
            color = WHITE if level < 3 else HOT_PINK if level == 3 else RED
            pygame.draw.rect(screen, color, plat)

        for bug in bugs:
            draw_broken_heart(screen, bug["rect"].x, bug["rect"].y)

        draw_heart(screen, player.x, player.y)

        screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
        screen.blit(font.render(f"Level: {level}", True, BLACK), (WIDTH - 100, 10))
        minutes = (300000 - elapsed) // 60000
        seconds = ((300000 - elapsed) // 1000) % 60
        screen.blit(font.render(f"Time: {minutes}:{str(seconds).zfill(2)}", True, BLACK), (WIDTH // 2 - 40, 10))

        pygame.display.update()

# 🎮 Start it up
splash_screen()
instructions_screen()
main_game()

