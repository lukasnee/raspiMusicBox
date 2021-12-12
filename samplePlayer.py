import random
import board
import busio
import pygame
import adafruit_mpr121

class SamplesPlayer:
    previousState = False

    def __init__(self, mpr121Pin, sampleFileNameList):
        self.mpr121Pin = mpr121Pin
        self.samples = []
        for sampleFileName in sampleFileNameList:
            self.samples.append(pygame.mixer.Sound(sampleFileName))
            print('loaded [%d] \"%s\"' % (len(self.samples), sampleFileName))

    def trigger(self):
        if not self.previousState and mpr121[self.mpr121Pin].value:
            self.previousState = True
            return True
        elif self.previousState and not mpr121[self.mpr121Pin].value:
            self.previousState = False
            return False

    def play(self):
        print("playing %d" % (random.randrange(0, len(self.samples))))
        self.samples[random.randrange(0, len(self.samples))].play()

    def playRoutine(self):
        if self.trigger():
            self.play()

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.set_num_channels(10)

class Mpr121Dummy:
    class Pin:
        def __init__(self, value):
            self.value = bool(value)

    pins = [Pin(False)] * 12

    def __getitem__(self, i):
        return self.pins[i]

if False:
    i2c = busio.I2C(board.SCL, board.SDA)
    mpr121 = adafruit_mpr121.MPR121(i2c)
else:
    mpr121 = Mpr121Dummy()
