import pygame
import time

pygame.init()

display_width = 800
display_height = 400

car_width = 100
car_height = 150

# black=(0,0,0)
# white=(255,255,255)
# red=(255,0,0)
# green=(0,255,0)
# blue=(0,0,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Rucy Car')

clock = pygame.time.Clock()
carImg = pygame.image.load('car.png')
#load the image of car in the folder


def car(x, y):
    gameDisplay.blit(carImg, (x, y))  # display car


def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def message_display(text):
    # C:\Users\Zayn Leo\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\pygame
    myText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, myText)
    TextRect.center = ((display_width/2), (display_height/4))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_Loop()  # start game again reset


def crash():
    message_display('YOU CRASHED!')


def game_Loop():
    x = (display_width*0.45)
    y = (display_height*0.5)
    x_change = 0
    y_change = 0
    #keep in mind that the origin of computer frame is upright
    #adding y means moving the car down vertically
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LEFT:
                     x_change = -5
                 elif event.key == pygame.K_RIGHT:
                     x_change = 5
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_UP:
                     y_change = -5
                 elif event.key == pygame.K_DOWN:
                     y_change = 5
             if event.type == pygame.KEYUP:
                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                     x_change = 0
                     print(event.key)
                 elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                     y_change = 0
             if event.type == 4:
                print((int(event.pos[0]/display_height*255), int(event.pos[1] /
                                                                 display_width*255), int(event.pos[0]/display_height*255)))
                gameDisplay.fill((int(event.pos[0]/display_width*255), int(
                    event.pos[1]/display_height*255), int(event.pos[0]/display_width*255)))
                # gameDisplay.fill((12,34,56))
                pygame.display.update()
             # print(event)
                #essential step, rewrite change of x back to zero after releasing
        x += x_change
        y += y_change
        # gameDisplay.fill((255,255,255))#set background as white
        car(x, y)
        if x > display_width-car_width or x < 0 or y > display_height-car_height or y < 0:
            crash()
        pygame.display.update()
        clock.tick(60)


game_Loop()
pygame.quit()
quit()
