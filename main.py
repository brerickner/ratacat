#Imports
import pygame

pygame.init()

display_width = 500
display_height = 300

'''define colors'''
black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))

'''title of window'''
pygame.display.set_caption('Ratacat')

clock = pygame.time.Clock()
userIcon = pygame.image.load('user.png')
userIcon2 = pygame.image.load('user.png')
 
'''position of user'''
x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
y_change = 0

'''location of original user'''
def user(x,y):
   gameDisplay.blit(userIcon,(x,y))

'''game loop'''
death = False

while not death:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            death = True
        '''movement of user'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_UP:
                y_change = -5
            if event.key == pygame.K_DOWN:
                y_change = 5
            if event.key == pygame.K_RIGHT:
                x_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
    '''changes position'''            
    x += x_change
    y += y_change
    
    '''updates screen'''
    gameDisplay.fill(white)
    user(x,y)
    pygame.display.update()

    '''frames per second fast but smooth increase frames per second'''
    clock.tick(60)

'''uninitiate pygame'''
pygame.quit()
quit()

'''meow'''