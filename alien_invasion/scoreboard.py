# -*- coding:utf-8 -*-
import pygame.font

class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        # self.score_image = self.font.render(score_str, True, self.text_color,self.sc_color)
        # self.score_rect = self.score_image.get_rect()
        # # self.score_rect.right = self.screen_rect.right - 200
        # # self.score_rect.top = 200
        # self.score_rect.center = self.rect.center

        self.score_image = self.font.render(score_str, True, self.text_color,
                                          self.button_color)
        self.score_rect = self.score_image.get_rect()
        # self.msg_image_rect.center = self.rect.center
        self.score_rect.right = self.screen_rect.right - 15
        self.score_rect.top = 15

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)