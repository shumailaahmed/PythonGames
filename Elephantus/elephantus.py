import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Baby Elephant Game")

# Load images
elephant_image = pygame.image.load("elephant.png")
elephant_width = elephant_image.get_width()
elephant_height = elephant_image.get_height()
peanut_image = pygame.image.load("peanut.png")
peanut_width = peanut_image.get_width()
peanut_height = peanut_image.get_height()

# Define game variables
score = 0
elephant_x = screen_width / 2 - elephant_width / 2
elephant_y = screen_height - elephant_height
elephant_speed = 5
peanut_x = random.randint(0, screen_width - peanut_width)
peanut_y = -peanut_height
peanut_speed = 3

# Main game loop
game_over = False
clock = pygame.time.Clock()
while not game_over:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the baby elephant
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and elephant_x > 0:
        elephant_x -= elephant_speed
    if keys[pygame.K_RIGHT] and elephant_x < screen_width - elephant_width:
        elephant_x += elephant_speed

    # Move the peanut
    peanut_y += peanut_speed
    if peanut_y > screen_height:
        peanut_x = random.randint(0, screen_width - peanut_width)
        peanut_y = -peanut_height
        score += 1

    # Check for collision
    if peanut_y + peanut_height > elephant_y and peanut_y < elephant_y + elephant_height:
        if peanut_x + peanut_width > elephant_x and peanut_x < elephant_x + elephant_width:
            game_over = True

    # Draw everything
    screen.fill((255, 255, 255))
    screen.blit(elephant_image, (elephant_x, elephant_y))
    screen.blit(peanut_image, (peanut_x, peanut_y))
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
