#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Constants
"""
import pygame
from pygame import *

PLAYER_X = 41
PLAYER_Y = 8

TEXT_FONT = "liberation Mono"
TEXT_SIZE = 30

SCORE_FILE = "scores.txt"
BACKGROUND_SONG = "music/nomina_777.mp3"
DIE_SONG = "music/lol_u_died.mp3"
RES_DIR = "ressources/"
MAP_PATH = "ressources/map"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
BLOCK_SIZE = 64
PLAYER_SIZE = BLOCK_SIZE * 3 / 4

MAP = [[int(i) for i in line] for line in [line.rstrip('\n').split("\t") for line in open(MAP_PATH) ]]
LEVEL_WIDTH = len(MAP[0]) * BLOCK_SIZE
LEVEL_HEIGHT = len(MAP) * BLOCK_SIZE

MV_SPEED = BLOCK_SIZE / 4

VIT_BLOCK = BLOCK_SIZE / 16

END_BLOCK = -2
DEAD_SPIKE = -1
PLAYER = 0
FIXED_BLOCK_MIN = 1
FIXED_BLOCK_MAX = 6

UP_MOVE_BLOCK = 99
DOWN_MOVE_BLOCK = 98
RIGHT_MOVE_BLOCK = 97
LEFT_MOVE_BLOCK = 96
UP_RIGHT_MOVE_BLOCK = 95
UP_LEFT_MOVE_BLOCK = 94
DOWN_RIGHT_MOVE_BLOCK = 93
DOWN_LEFT_MOVE_BLOCK = 92
APPEAR_BLOCK_1 = 91
APPEAR_BLOCK_2 = 90
UP_DEGRADE_BLOCK = 89
DOWN_DEGRADE_BLOCK = 88
RIGHT_DEGRADE_BLOCK = 87
LEFT_DEGRADE_BLOCK = 86

BLACK = 0, 0, 0
GREY = 122, 122, 122
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 20, 205, 20
BLUE = 0, 0, 255
YELLOW = 160, 160, 0
ORANGE = 255, 160, 0
CYAN = 0, 190, 160
PINK = 255, 64, 129, 100

UP_DOWN_MOVE = 200, 200, 200
LEFT_RIGHT_MOVE = 150, 150, 150
OTHER_MOVE_BLOCK = 100, 100, 100
APPEAR_BLOCK_COLOR = 50, 50, 50
DEGRADE_BLOCK_COLOR = 225, 225, 225

FIXED_BLOCKS = [["", WHITE],    \
                ["", RED],      \
                ["", GREEN],    \
                ["", BLUE],     \
                ["", YELLOW],   \
                ["", ORANGE],   \
                ["", CYAN]]     \
          

KEYBLOCKS = [["right_arrow.png", RED],\
             ["up_arrow.png", GREEN],\
             ["left_arrow.png", YELLOW],\
             ["up_arrow.png", YELLOW],\
             ["a_key.png", CYAN],\
             ["p_key.png", ORANGE],\
             ["left_arrow.png", RED],\
             ["right_arrow.png", RED],\
             ["s_key.png", RED],\
             ["left_arrow.png", GREEN],\
             ["p_key.png", GREEN],\
             ["s_key.png", BLUE],\
             ["b_key.png", YELLOW],\
             ["up_arrow.png", YELLOW],\
             ["e_key.png", ORANGE],\
             ["z_key.png", ORANGE],\
             ["g_key.png", CYAN],\
             ["m_key.png", ORANGE],\
             ["down_arrow.png", RED],\
             ["up_arrow.png", CYAN],\
             ["right_arrow.png", GREEN],\
             ["left_arrow.png", RED],\
             ["j_key.png", BLUE],\
             ["f_key.png", BLUE],\
             ["left_arrow.png", BLUE],\
             ["right_arrow.png", BLUE],\
             ["z_key.png", BLUE],\
             ["w_key.png", BLUE],\
             ["p_key.png", RED],\
             ["right_arrow.png", RED],\
             ["p_key.png", BLUE],\
             ["m_key.png", BLUE],\
             ["w_key.png", RED],\
             ["p_key.png", GREEN],\
             ["up_arrow.png", CYAN],\
             ["right_arrow.png", CYAN],\
             ["left_arrow.png", YELLOW],\
             ["down_arrow.png", YELLOW],\
             ["f4_key.png", YELLOW],\
             ["alt_key.png", RED],\
             ["z_key.png", GREEN],\
             ["a_key.png", GREEN],\
             ["f5_key.png", BLUE],\
             ["p_key.png", BLUE],\
             ["ctrl_key.png", BLUE],\
             ["w_key.png", BLUE],\
             ["f4_key.png", BLUE],\
             ["f5_key.png", YELLOW]]

NONE = -1
STEPS = [[K_LEFT, K_RIGHT, NONE],       \
         [NONE, K_RIGHT, K_UP],         \
         [K_LEFT, NONE, K_UP],          \
         [K_a, K_p, NONE],              \
         [K_LEFT, K_RIGHT, NONE],       \
         [NONE, K_s, K_LEFT],           \
         [K_p, K_s, NONE],              \
         [K_b, K_UP, NONE],             \
         [K_e, NONE, K_z],              \
         [K_g, K_m, NONE],              \
         [K_UP, NONE, K_DOWN],          \
         [K_RIGHT, K_LEFT, NONE],       \
         [NONE, K_f, K_j],              \
         [K_LEFT, K_RIGHT, NONE],       \
         [NONE, K_z, K_w],              \
         [K_RIGHT, NONE, K_p],          \
         [NONE, K_p, K_m],              \
         [NONE, K_p, K_w],              \
         [NONE, K_RIGHT, K_UP],         \
         [NONE, K_DOWN, K_LEFT],        \
         [NONE, K_LALT, K_F4],          \
         [K_a, K_z, NONE],              \
         [K_F5, NONE, K_p],             \
         [NONE, K_w, K_LCTRL],          \
         [K_F5, K_F4, NONE]]
