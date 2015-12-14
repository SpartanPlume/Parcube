#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, pygame
import time as t
from pygame import *
from parcube.Constants import *
from parcube.Player import *
from parcube.Block import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def camera_func(camera, target_rect):
    x, y, _, _ = target_rect
    _, _, width, height = camera
    x, y = -x + SCREEN_WIDTH / 2, -y + SCREEN_HEIGHT / 2

    x = min(0, x)
    x = max(-(camera.width - SCREEN_WIDTH), x)
    y = max (-(camera.height - SCREEN_HEIGHT), y)
    y = min(0, y)

    return Rect(x, y, width, height)

def check_event(key, player, LEVEL_WIDTH, LEVEL_HEIGHT):
    return player

def move_block(entities, player):
    players = pygame.sprite.Group()
    players.add(player)
    if (move_block.move != -1):
        move_block.move += 1
    else:
        move_block.wait += 1
    
    for e in entities:
        player_collide = []
        if (e.num == UP_MOVE_BLOCK and move_block.move != -1):
            e.update(e.x, e.y - VIT_BLOCK * move_block.direction)
        if (e.num == DOWN_MOVE_BLOCK and move_block.move != -1):
            e.update(e.x, e.y + VIT_BLOCK * move_block.direction)
        if (e.num == RIGHT_MOVE_BLOCK and move_block.move != -1):
            e.update(e.x + VIT_BLOCK * move_block.direction, e.y)
        if (e.num == LEFT_MOVE_BLOCK and move_block.move != -1):
            e.update(e.x - VIT_BLOCK * move_block.direction, e.y)
        if (e.num == UP_RIGHT_MOVE_BLOCK and move_block.move != -1):
            e.update(e.x + VIT_BLOCK * move_block.direction, e.y - VIT_BLOCK * move_block.direction)
        if (e.num == UP_LEFT_MOVE_BLOCK and move_block.move != -1):
            e.update(e.x - VIT_BLOCK * move_block.direction, e.y - VIT_BLOCK * move_block.direction)
        if (e.num == DOWN_RIGHT_MOVE_BLOCK and move_block.move != -1):
            e.update(e.x + VIT_BLOCK * move_block.direction, e.y + VIT_BLOCK * move_block.direction)
        if (e.num == DOWN_LEFT_MOVE_BLOCK and move_block.move != -1):
            e.update(e.x - VIT_BLOCK * move_block.direction, e.y + VIT_BLOCK * move_block.direction)
        if (e.num == UP_MOVE_BLOCK or e.num == UP_RIGHT_MOVE_BLOCK or e.num == UP_LEFT_MOVE_BLOCK):
            if (-1 * VIT_BLOCK * move_block.direction < 0):
                player_collide = pygame.sprite.spritecollide(e, players, False)
                if (len(player_collide) > 0):
                    player.fall = False
                    player.update(player.x, e.rect.top - PLAYER_SIZE)
        elif (e.num == DOWN_MOVE_BLOCK or e.num == DOWN_RIGHT_MOVE_BLOCK or e.num == DOWN_LEFT_MOVE_BLOCK):
            if (VIT_BLOCK * move_block.direction < 0):
                player_collide = pygame.sprite.spritecollide(e, players, False)
                if (len(player_collide) > 0):
                    player.fall = False
                    player.update(player.x, e.rect.top - PLAYER_SIZE)
        if (e.num == LEFT_MOVE_BLOCK or e.num == UP_LEFT_MOVE_BLOCK or e.num == DOWN_LEFT_MOVE_BLOCK):
            if (-1 * VIT_BLOCK * move_block.direction < 0):
                player_collide = pygame.sprite.spritecollide(e, players, False)
                if (len(player_collide) > 0):
                    player.update(e.rect.left - PLAYER_SIZE, player.y)
            if (VIT_BLOCK * move_block.direction < 0):
                player_collide = pygame.sprite.spritecollide(e, players, False)
                if (len(player_collide) > 0):
                    player.update(e.rect.right, player.y)
        elif (e.num == RIGHT_MOVE_BLOCK or e.num == UP_RIGHT_MOVE_BLOCK or e.num == DOWN_RIGHT_MOVE_BLOCK):
            if (VIT_BLOCK * move_block.direction < 0):
                player_collide = pygame.sprite.spritecollide(e, players, False)
                if (len(player_collide) > 0):
                    player.update(e.rect.left - PLAYER_SIZE, player.y)
            if (-1 * VIT_BLOCK * move_block.direction < 0):
                player_collide = pygame.sprite.spritecollide(e, players, False)
                if (len(player_collide) > 0):
                    player.update(e.rect.right, player.y)

        if (move_block.long_wait == 32):
            if ((e.num == APPEAR_BLOCK_1 or e.num == APPEAR_BLOCK_2) and e.visible):
                e.visible = False
                e.update_color(BLACK)
            elif e.num == APPEAR_BLOCK_1 or e.num == APPEAR_BLOCK_2:
                e.visible = True
                e.update_color(APPEAR_BLOCK_COLOR)
                collision = []
                collision = pygame.sprite.spritecollide(e, players, False)
                if len(collision) > 0:
                    player.dead = True
            elif e.num <= UP_DEGRADE_BLOCK and e.num >= LEFT_DEGRADE_BLOCK:
                if e.num == UP_DEGRADE_BLOCK:
                    if (move_block.step < 4):
                        e.update(e.x, e.y - BLOCK_SIZE)
                    else:
                        e.update(e.x, e.y + 3 * BLOCK_SIZE)
                elif e.num == DOWN_DEGRADE_BLOCK:
                    if (move_block.step < 4):
                        e.update(e.x, e.y + BLOCK_SIZE)
                    else:
                        e.update(e.x, e.y - 3 * BLOCK_SIZE)
                elif e.num == RIGHT_DEGRADE_BLOCK:
                    if (move_block.step < 4):
                        e.update(e.x + BLOCK_SIZE, e.y)
                    else:
                        e.update(e.x - 3 * BLOCK_SIZE, e.y)
                elif e.num == LEFT_DEGRADE_BLOCK:
                    if (move_block.step < 4):
                        e.update(e.x - BLOCK_SIZE, e.y)
                    else:
                        e.update(e.x + 3 * BLOCK_SIZE, e.y)
                collision = []
                collision = pygame.sprite.spritecollide(e, players, False)
                if len(collision) > 0:
                    player.dead = True

    if (move_block.wait == 16):
        move_block.move = 0
        move_block.wait = 0
    if (move_block.move == BLOCK_SIZE):
        move_block.move = -1
        move_block.direction *= -1

    if (move_block.long_wait < 32):
        move_block.long_wait += 1
    else:
        move_block.long_wait = 1
        if move_block.step < 4:
            move_block.step += 1
        else:
            move_block.step = 1

    move_block.player = player
        
    return (entities)

def initialize_entities():
    entities = pygame.sprite.Group()
    row = col = 0
    while row < len(MAP):
        while col < len(MAP[0]):
            if MAP[row][col] == END_BLOCK:
                b = Block(col * BLOCK_SIZE, row * BLOCK_SIZE, PINK, MAP[row][col])
                entities.add(b)
            if MAP[row][col] == DEAD_SPIKE:
                b = Block(col * BLOCK_SIZE, row * BLOCK_SIZE, GREY, MAP[row][col])
                entities.add(b)
            if MAP[row][col] >= FIXED_BLOCK_MIN and MAP[row][col] <= FIXED_BLOCK_MAX:
                b = Block(col * BLOCK_SIZE, row * BLOCK_SIZE, BLACK, MAP[row][col])
                entities.add(b)
            if MAP[row][col] == UP_MOVE_BLOCK or MAP[row][col] == DOWN_MOVE_BLOCK:
                b = Block(col * BLOCK_SIZE, row * BLOCK_SIZE, UP_DOWN_MOVE, MAP[row][col])
                entities.add(b)
            if MAP[row][col] == LEFT_MOVE_BLOCK or MAP[row][col] == RIGHT_MOVE_BLOCK:
                b = Block(col * BLOCK_SIZE, row * BLOCK_SIZE, LEFT_RIGHT_MOVE, MAP[row][col])
                entities.add(b)
            if MAP[row][col] >= DOWN_LEFT_MOVE_BLOCK and MAP[row][col] <= UP_RIGHT_MOVE_BLOCK:
                b = Block(col * BLOCK_SIZE, row * BLOCK_SIZE, OTHER_MOVE_BLOCK, MAP[row][col])
                entities.add(b)
            if MAP[row][col] == APPEAR_BLOCK_1:
                b = Block(col * BLOCK_SIZE, row * BLOCK_SIZE, APPEAR_BLOCK_COLOR, MAP[row][col])
                b.visible = True
                entities.add(b)
            if MAP[row][col] == APPEAR_BLOCK_2:
                b = Block(col * BLOCK_SIZE, row * BLOCK_SIZE, BLACK, MAP[row][col])
                b.visible = False
                entities.add(b)
            if MAP[row][col] >= LEFT_DEGRADE_BLOCK and MAP[row][col] <= UP_DEGRADE_BLOCK:
                b = Block(col * BLOCK_SIZE, row * BLOCK_SIZE, DEGRADE_BLOCK_COLOR, MAP[row][col])
                entities.add(b)
            if MAP[row][col] < END_BLOCK:
                b = Block(col * BLOCK_SIZE, row * BLOCK_SIZE, PINK, MAP[row][col])
                entities.add(b)
            if MAP[row][col] >= 100:
                b = KeyBlock(col * BLOCK_SIZE, row * BLOCK_SIZE, MAP[row][col])
                entities.add(b)
            col += 1
        row += 1
        col = 0
    return (entities)

def key_event(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return (0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                return (0)
            if event.key == K_LALT or event.key == K_RALT:
                key_event.altkey = True
            if event.key == K_F4:
                key_event.f4key = True
            if event.key == STEPS[player.step][2] and player.fall == False:
                player.top = True
            if event.key == STEPS[player.step][0]:
                player.left = True
            if event.key == STEPS[player.step][1]:
                player.right = True
        if event.type == pygame.KEYUP:
            if event.key == STEPS[player.step][0]:
                player.left = False
            if event.key == STEPS[player.step][1]:
                player.right = False
            if event.key == K_LALT or event.key == K_RALT:
                key_event.altkey = False
            if event.key == K_F4:
                key_event.f4key = False

    if key_event.altkey and key_event.f4key:
        return (0)

    return (player)

def dead_screen():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(DIE_SONG)
    pygame.mixer.music.play(-1, 2.3)
    
    font1 = pygame.font.SysFont(TEXT_FONT, TEXT_SIZE + 15)
    font2 = pygame.font.SysFont(TEXT_FONT, TEXT_SIZE - 5)
    text = font1.render("LOL U DIED", 1, WHITE)
    text2 = font2.render("Press any key to retry", 1, WHITE)
    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_rect().width / 2, SCREEN_HEIGHT / 2 - text.get_rect().height / 2))
    screen.blit(text2, (SCREEN_WIDTH / 2 - text2.get_rect().width / 2, SCREEN_HEIGHT / 2 + 100))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return (0)
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return (0)
                else:
                    pygame.mixer.music.stop()
                    return (game())

def write_score_in_file(now_min, now_sec, now_time):
    nline = 0
    tmp_nline = -1
    f = open(SCORE_FILE, "r+")
    for line in f:
        if nline != tmp_nline:
            tmp_score = line.split("\t")[1]
            score = []
            score = tmp_score.split(":")
            if (now_min < int(score[0]) or (now_min == int(score[0]) and now_sec < int(score[1]))):
                f.close()
                f = open(SCORE_FILE, "r")
                tmp_nline = 0
                lines = []
                for line in f:
                    if (tmp_nline == nline):
                        lines.append("PLAYER :\t" + now_time + "\n")
                    lines.append(line)
                    tmp_nline += 1
                f.close()
                f = open(SCORE_FILE, "w")
                for line in lines:
                    f.write(line)
                f.close()
                nline = tmp_nline
        if nline == tmp_nline:
            break
        nline += 1
    if (tmp_nline != nline):
        f.write("PLAYER :\t" + now_time + "\n")
        f.close()

def score_screen(now_min, now_sec, now_time):
    write_score_in_file(now_min, now_sec, now_time)
    screen.fill(BLACK)
    y = 40
    nline = 0
    f = open(SCORE_FILE, "r")
    for line in f:
        if nline < 5:
            score_font = pygame.font.SysFont(TEXT_FONT, TEXT_SIZE)
            score_text = score_font.render(line.replace("\t", " ").replace("\n", ""), 1, WHITE)
            screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_rect().width / 2, y))
            y += score_text.get_rect().height + 40
        nline += 1
    f.close()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return (0)
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return (0)
                
def game():
    timer = pygame.time.Clock()
    
    camera = Camera(camera_func, LEVEL_WIDTH, LEVEL_HEIGHT)
    player = Player((1 + PLAYER_X) * BLOCK_SIZE, (1 + PLAYER_Y) * BLOCK_SIZE)

    entities = initialize_entities()
    entities.add(player)
    
    move_block.move = 0
    move_block.wait = 0
    move_block.direction = 1
    move_block.long_wait = 1
    move_block.step = 1
    old_time = new_time = t.time()

    key_event.altkey = key_event.f4key = False
    
    font = pygame.font.SysFont(TEXT_FONT, TEXT_SIZE)

    pygame.mixer.music.load(BACKGROUND_SONG)
    pygame.mixer.music.play(-1)

    while True:
        if player.dead == False:
            entities = move_block(entities, player)
            player = move_block.player

            player = key_event(player)
            if (player == 0):
                return (0)

            player.move(entities)

            if player.old_step != player.step:
                if STEPS[player.old_step][0] != STEPS[player.step][0]:
                    player.left = False
                if STEPS[player.old_step][1] != STEPS[player.step][1]:
                    player.right = False
                player.old_step = player.step

            camera.update(player.rect)
        
            screen.fill(BLACK)
            for e in entities:
                if (e.num != 0 and e.visible):
                    screen.blit(e.image, camera.apply(e))
            screen.blit(player.image, camera.apply(player))

            new_time = t.time()
            now_min = int((new_time - old_time) / 60)
            now_sec = int((new_time - old_time) % 60)
            now_time = ""
            if (now_min < 10):
                now_time = "0"
            now_time += str(now_min) + ":"
            if (now_sec < 10):
                now_time += "0"
            now_time += str(now_sec)
            text = font.render(now_time, 1, WHITE)
            screen.blit(text, (SCREEN_WIDTH / 2 - text.get_rect().width / 2, 20))

            pygame.display.update()
            timer.tick(33)

        if (player.dead):
            return (dead_screen())
        elif (player.win):
            return (score_screen(now_min, now_sec, now_time))

def launch_pygame():
    pygame.init()

def close_pygame():
    pygame.quit()

def main(argv):
    launch_pygame()
    return_value = game()
    close_pygame()
    return (return_value)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
