'''
            This function will return when player stroke 'space' key
            '''
            '''
            Event will include mouse position and key stroke(UP and DOWN) together with some value 
            e.g. mouse X,Y position and key name.
            ##########################################################################################
                                            windows active event

                <Event(1-ActiveEvent {'gain': 1, 'state': 1})> focus on screen mouse move in
                <Event(1-ActiveEvent {'gain': 0, 'state': 1})> focus on screen mouse move out
                <Event(1-ActiveEvent {'gain': 0, 'state': 2})> unfocus on screen app not running
                <Event(1-ActiveEvent {'gain': 1, 'state': 6})> call back from unfocus
                -----------------------------------------------------------------------------------
                                            mouse moving event =              
                            {
                                pos: position
                                rel: relative position 
                                buttons: {
                                    element: {
                                        x:left,
                                        y:middle,
                                        z:right
                                    }
                                    value: {
                                        1: active,
                                        0: inactive
                                    }
                                }
                            }
                <Event(4-MouseMotion {'pos': (287, 405), 'rel': (20, -106), 'buttons': (0, 0, 0)})> 
                <Event(4-MouseMotion {'pos': (271, 403), 'rel': (-16, -2), 'buttons': (0, 0, 0)})>
                -----------------------------------------------------------------------------------
                                            holding mouse event
                <Event(4-MouseMotion {'pos': (248, 401), 'rel': (10, 0), 'buttons': (1, 0, 0)})>
                <Event(4-MouseMotion {'pos': (268, 401), 'rel': (20, 0), 'buttons': (1, 0, 0)})>
                <Event(4-MouseMotion {'pos': (286, 400), 'rel': (18, -1), 'buttons': (1, 0, 0)})>
                -----------------------------------------------------------------------------------
                                            stroke keyboard event = 
                            {
                                mod: {
                                meaning: existing key stroke
                                value:{
                                    1:  left-shift,
                                    2:  right-shift,
                                    256:    left-alt
                                    257: left-shift + left-alt
                                    }
                                }   
                                unicode: value of the key e.g. a,b,c,d
                                key: unicode number       e.g. 97,98,99,100
                                scancode: key position on the keyboard
                            }
                <Event(2-KeyDown {'unicode': '', 'key': 304, 'mod': 0, 'scancode': 42})>
                <Event(3-KeyUp {'key': 304, 'mod': 0, 'scancode': 42})>
                -----------------------------------------------------------------------------------
                                            left mouse click event

                <Event(5-MouseButtonDown {'pos': (194, 417), 'button': 1})> 
                <Event(4-MouseMotion {'pos': (199, 417), 'rel': (5, 0), 'buttons': (1, 0, 0)})>
                <Event(4-MouseMotion {'pos': (204, 416), 'rel': (5, -1), 'buttons': (1, 0, 0)})>
                <Event(6-MouseButtonUp {'pos': (204, 416), 'button': 1})>
                -----------------------------------------------------------------------------------
                                           
            ##########################################################################################
            pygame.event.get will update repeatedly when the game is running
            '''


import pygame
#import the library

pygame.init()
# initialization
display_width, display_height = 800, 240
gameDisplay = pygame.display.set_mode((display_width, display_height))

# pygame.display.set_caption('Racey Rat')

clock = pygame.time.Clock()

exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == 2:
            if event.key == 27:
                exit = True
        print(event)  # print the events that have occurred
        if event.type == 4:
                print((int(event.pos[0]/display_height*255), int(event.pos[1] /
                                                                 display_width*255), int(event.pos[0]/display_height*255)))
                gameDisplay.fill((int(event.pos[0]/display_width*255), int(
                    event.pos[1]/display_height*255), int(event.pos[0]/display_width*255)))
                pygame.display.update()
    pygame.display.update()

    clock.tick(60)  # frame per second, here 60fps

pygame.quit()

quit()
