import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (152, 251, 152)
BLACK = (0, 0, 0)
bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs","bg.png")).convert_alpha(), (600, 900))

# Font
font = pygame.font.Font(None, 50)

# Start Button
start_button_width = 200
start_button_height = 50
start_button_x = (screen_width - start_button_width) // 2
start_button_y = (screen_height - start_button_height) // 2

start_button = pygame.Rect(start_button_x, start_button_y, start_button_width, start_button_height)

# Game Loop
running = True
game_started = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    game_started = True

    # Clear the screen
    screen.fill(WHITE)

    if not game_started:
        # Draw the start button
        pygame.draw.rect(screen, BLACK, start_button)
        start_text = font.render("Start", True, WHITE)
        start_text_rect = start_text.get_rect(center=start_button.center)
        screen.blit(start_text, start_text_rect)
    else:
        # Execute the self-playing AI bird game using NEAT Python
        #os.system("flappy_bird.py")
        os.system("python ./flappy_bird.py")
        running = False

    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()