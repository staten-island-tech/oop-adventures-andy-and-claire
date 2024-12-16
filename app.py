import pygame

pygame.init()

#Plan: Make a background
#What is the theme?
#Work on gameplay
#Add way to win

#Start on background

pygame.display.set_caption("Random Pygame") #This is the name of the window

screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode((screen_width,screen_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,55,200)) #Adds color(Plan to change background)

    pygame.display.flip()

pygame.quit()