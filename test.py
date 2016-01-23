import pygame.mixer
from pygame.mixer import Sound

pygame.mixer.init()

drum = Sound("samples/dance116.wav")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:                                                    
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key==K_ESCAPE:
                 pygame.quit()
            elif event.key==K_UP:
            	drum.play()