#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame import *
from parcube.Entity import *
from parcube.Constants import *

class Block(Entity):
    def __init__(self, x, y, color, num):
        Entity.__init__(self)
        if num == DEAD_SPIKE:
            self.image = pygame.image.load(RES_DIR + "dead_spike.png")
        elif num >= FIXED_BLOCK_MIN and num <= FIXED_BLOCK_MAX:
            color = FIXED_BLOCKS[num][1]
            self.image = Surface((BLOCK_SIZE, BLOCK_SIZE))
            self.image.fill(color)
            if FIXED_BLOCKS[num][0] != "":
                img = pygame.image.load(RES_DIR + FIXED_BLOCKS[num][0])
                self.image.blit(img)
        else:
            self.image = Surface((BLOCK_SIZE, BLOCK_SIZE), SRCALPHA)
            self.image.fill(color)
        self.image.convert()
        self.rect = Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        self.num = num
        self.x, self.y = x, y
        self.visible = True

    def update(self, x, y):
        self.x, self.y = x, y
        self.rect = Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        
    def update_color(self, color):
        self.image.fill(color)
        self.image.convert()

class KeyBlock(Entity):
    def __init__(self, x, y, num):
        Entity.__init__(self)
        img = pygame.image.load(RES_DIR + KEYBLOCKS[num - 100][0])
        color = KEYBLOCKS[num - 100][1]
        self.image = Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(color)
        self.image.blit(img, Rect(7, 8, 50, 48))
        self.image.convert()
        self.rect = Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        self.num = num
        self.x, self.y = x, y
        self.visible = True
