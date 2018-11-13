# -*- coding:utf-8 -*-
import sys
import pygame

import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_height, ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")
    """创建飞船"""
    ship = Ship(ai_settings,screen)
    alien = Alien(ai_settings,screen)
    #存储子弹的编组
    bullets = Group()
    aliens = Group()
    #外星人群
    stats = GameStats(ai_settings)
    #创建开始按钮
    play_button = Button(ai_settings, screen, "Play")
    sb = Scoreboard(ai_settings, screen, stats)
    while True:
        gf.check_events(ai_settings,screen,ship,aliens,bullets,play_button,stats)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship,aliens,bullets,stats,sb)
            gf.update_aliens(ai_settings,stats,screen,ship, aliens,bullets)
        if len(aliens) < ai_settings.alien_number_limit:
            gf.create_fleet(ai_settings, screen, ship,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,sb)
run_game()

