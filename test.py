import pygame, sys
from pygame.locals import *
from pygame.mixer import Channel, Sound, get_init, pre_init
from array import array
from time import sleep
import RPi.GPIO as GPIO

# class Note(Sound):

    # def __init__(self, frequency, volume=.01):
    #     self.frequency = frequency
    #     Sound.__init__(self, buffer=self.build_samples())
    #     self.set_volume(volume)

    # def build_samples(self):
    #     period = int(round(get_init()[0] / self.frequency))
    #     samples = array("h", [0] * period)
    #     amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
    #     for time in xrange(period):
    #         if time < period / 2:
    #             samples[time] = amplitude
    #         else:
    #             samples[time] = -amplitude
    #     return samples

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)


pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('SubZero')

pygame.mixer.pre_init(44100, -16, 5, 1024)
pygame.mixer.init()

drum = Sound('samples/dance116.wav')
C1 = Sound('samples/C1.ogg')
C2 = Sound('samples/C2.ogg')
C3 = Sound('samples/C3.ogg')
C4 = Sound('samples/C4.ogg')

pygame.mixer.Sound.set_volume(drum, 0.5)

while True:
    pygame.mixer.Channel(0).queue(drum)

    pressed = pygame.key.get_pressed()
    
    if (pressed[pygame.K_q] or not(GPIO.input(2))):
        pygame.mixer.Channel(1).queue(C1)
    else:
    	pygame.mixer.Channel(1).fadeout(500)

    if (pressed[pygame.K_w] or not(GPIO.input(3))):
        pygame.mixer.Channel(2).queue(C2)
    else:
    	pygame.mixer.Channel(2).fadeout(500)

    if (pressed[pygame.K_e] or not(GPIO.input(4))):
        pygame.mixer.Channel(3).queue(C3)
    else:
    	pygame.mixer.Channel(3).fadeout(500)

    if (pressed[pygame.K_r] or not(GPIO.input(14))):
        pygame.mixer.Channel(4).queue(C4)
    else:
    	pygame.mixer.Channel(4).fadeout(500)

    for event in pygame.event.get():
        if event.type == QUIT:
            GPIO.cleanup()
            pygame.quit()
            sys.exit()
    pygame.display.update()
