#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from parcube.Entity import *
from parcube.Constants import *

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(WHITE)
        self.image.convert()
        self.rect = Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.x, self.y = x, y
        self.num = self.step = self.old_step = self.jump_height = 0
        self.left = self.top = self.right = self.dead = self.win = False
        self.fall = self.visible = True

    def update(self, x, y):
        self.x, self.y = x, y
        self.rect = Rect(self.x, self.y, PLAYER_SIZE, PLAYER_SIZE)

    def move(self, entities):
        if (self.left):
            self.update(self.x - MV_SPEED, self.y)
        if (self.right):
            self.update(self.x + MV_SPEED, self.y)
        self.collide(self.left, self.right, False, False, entities)
        
        self.fall = True
        if (self.top):
            self.jump_height += 1
            self.update(self.x, self.y - BLOCK_SIZE / self.jump_height)
            if (self.jump_height == 20):
                self.jump_height = 0
                self.top = False
        elif (self.fall):
            self.update(self.x, self.y + BLOCK_SIZE / 4)
        self.jump_height = self.collide(False, False, self.top, self.fall, entities)
        if (self.jump_height == 20):
            self.jump_height = 0
            self.top = False
        if (self.jump_height == -1):
            self.jump_height = 0
            self.top = self.fall = False
        elif (self.jump_height < -2):
            self.step = self.jump_height * -1 - 2

    def collide(self, left, right, top, fall, entities):
        blocks_list = []
        for e in entities:
            if (e.visible):
                blocks_list.append(e)
        
        blocks_hit_list = pygame.sprite.spritecollide(self, blocks_list, False)
        if (len(blocks_hit_list) > 1):
            right_collisions = []
            left_collisions = []
            bottom_collisions = []
            top_collisions = []
            check = False
            for e in blocks_hit_list:
                if (e.num == DEAD_SPIKE):
                    self.dead = True
                    return (-2)
                if (e.num == END_BLOCK):
                    self.win = True
                    return (100)
                if (e.num < END_BLOCK):
                    self.step = e.num * -1 - 2
                elif (e.num > 0):
                    right_collisions.append(e.rect.left)
                    left_collisions.append(e.rect.right)
                    bottom_collisions.append(e.rect.top)
                    top_collisions.append(e.rect.bottom)
                    check = True

            if check:
                left_collision = max(left_collisions)
                top_collision = max(top_collisions)
                right_collision = min(right_collisions)
                bottom_collision = min(bottom_collisions)
                
                if left:
                    self.update(left_collision, self.y)
                if right:
                    self.update(right_collision - PLAYER_SIZE, self.y)
                if top:
                    self.update(self.x, top_collision)
                    return (20)
                if fall:
                    self.update(self.x, self.y - BLOCK_SIZE / 4)
                    blocks_hit_list_after = []
                    blocks_hit_list_after = pygame.sprite.spritecollide(self, blocks_hit_list, False)
                    i = 0
                    for b in blocks_hit_list_after:
                        if (b.num > 0):
                            i += 1
                    if i > 0:
                        self.dead = True
                        return (-2)
                    self.update(self.x, bottom_collision - PLAYER_SIZE)
                    return (-1)
        return (self.jump_height)

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target_rect):
        self.state = self.camera_func(self.state, target_rect)
