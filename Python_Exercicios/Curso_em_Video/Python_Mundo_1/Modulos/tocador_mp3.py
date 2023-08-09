'''
Faça um rpograma em python que abra e reproduza
o áudio de um arquivo mp3
'''

import pygame
pygame.mixer.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
pygame.event.wait()
