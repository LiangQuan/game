# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_settings,screen):
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.alien_speed_factor = 5
        self.fleet_direction = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # self.x += self.ai_settings.alien_speed_factor
        # self.rect.x = self.x
        self.x += (self.ai_settings.alien_speed_factor * self.fleet_direction)
        self.rect.x = self.x
        self.rect.y += self.ai_settings.fleet_drop_speed

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            print 'left'
            return True