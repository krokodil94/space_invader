import pygame
import random
import math

# Initialize the pygame
pygame.init()
# Create the screen
screen = pygame.display.set_mode((800, 600))
# background
background = pygame.image.load('background.png')
# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
EnemyImg = pygame.image.load('alien.png')
EnemyX = random.randint(0, 800)
EnemyY = random.randint(50, 150)
EnemyX_change = 4
EnemyY_change = 10

# Bullet
# "ready- you can't see the bullet on the screen
BulletImg = pygame.image.load('bullet.png')
BulletX = 0
BulletY = 480
BulletX_change = 0
BulletY_change = 20
Bullet_state = "ready"
score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(EnemyImg, (x, y))


def fire_bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletImg, (x + 16, y + 16))


def is_collision(EnemyX, EnemyY, BulletX, BulletY):
    distance = math.sqrt((math.pow(EnemyX - BulletX, 2)) + (math.pow(EnemyY - BulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    # Screen color
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed, check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if Bullet_state == "ready":
                    # Get the current x coordinate of the spaceship
                    BulletX = playerX
                    fire_bullet(BulletX, BulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # Checking for boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # Enemy movement
    EnemyX += EnemyX_change

    if EnemyX <= 0:
        EnemyX_change = 4
        EnemyY += EnemyY_change
    elif EnemyX >= 736:
        EnemyX_change = -4
        EnemyY += EnemyY_change

    # bullet movement
    if BulletY <= 0:
        BulletY = 480
        Bullet_state = "ready"
    if Bullet_state == "fire":
        fire_bullet(BulletX, BulletY)
        BulletY -= BulletY_change

    # Collision
    collision = is_collision(EnemyX, EnemyY, BulletX, BulletY)
    if collision:
        BulletY = 480
        Bullet_state = "ready"
        score += 1
        print(score)

    player(playerX, playerY)
    enemy(EnemyX, EnemyY)
    pygame.display.update()
