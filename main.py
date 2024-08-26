import pygame
import random

pygame.init()

# Kích thước màn hình
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout")

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Thông số trò chơi
paddle_width, paddle_height = 100, 10
ball_radius = 10
paddle_speed = 15
ball_speed_x, ball_speed_y = 7, -7
brick_width, brick_height = 60, 20
rows, cols = 5, 10

# Tọa độ ban đầu
paddle_x, paddle_y = width // 2 - paddle_width // 2, height - 50
ball_x, ball_y = width // 2, height - 60

# Gạch
bricks = []
for row in range(rows):
    for col in range(cols):
        bricks.append(pygame.Rect(col * (brick_width + 10) + 10, row * (brick_height + 5) + 10, brick_width, brick_height))

def draw():
    win.fill(black)
    pygame.draw.rect(win, white, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(win, white, (ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2))
    for brick in bricks:
        pygame.draw.rect(win, red, brick)
    pygame.display.update()

def ball_movement():
    global ball_x, ball_y, ball_speed_x, ball_speed_y

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= width:
        ball_speed_x *= -1

    if ball_y - ball_radius <= 0:
        ball_speed_y *= -1

    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

    if ball_rect.colliderect(paddle_rect):
        ball_speed_y *= -1
        ball_y = paddle_y - ball_radius

    global bricks
    for brick in bricks[:]:
        if ball_rect.colliderect(brick):
            ball_speed_y *= -1
            bricks.remove(brick)

    if ball_y + ball_radius >= height:
        return True  # Ball fell down
    return False

def player_movement(keys):
    global paddle_x
    if keys[pygame.K_LEFT] and paddle_x - paddle_speed > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x + paddle_speed < width - paddle_width:
        paddle_x += paddle_speed

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        player_movement(keys)
        if ball_movement():
            print("Game Over")
            run = False
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
