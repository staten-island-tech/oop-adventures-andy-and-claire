import pygame

pygame.init()

#Plan: start by making a background
# What is the theme?
# Add gameplay: make an rpg(what should the rpg be? Decide later)
# Add way to win: (world domination? beat the bbeg?)

# Start on theme and background

pygame.display.set_caption("Welcome to a random pygame") #This is the app's name

screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode((screen_width,screen_height)) #You need to use this to activate the screen, adjust later

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 55, 200)) #Change the background to most likey a sky with clouds

    pygame.display.flip()

pygame.quit()