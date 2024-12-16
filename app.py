import pygame

pygame.init()

#Plan: start by making a background
# What is the theme?
# Add gameplay: make an rpg(what should the rpg be? Decide later)
# Add way to win: (world domination? beat the bbeg?)

# Start on theme and background

pygame.display.set_caption("Welcome to a random pygame")

screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 55, 200))

    pygame.display.flip()

pygame.quit()