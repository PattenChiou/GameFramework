from enum import auto
from os import path

import pygame
from mlgame.utils.enum import StringEnum
from mlgame.view.view_model import create_asset_init_data, create_image_view_data

import env
import math
from .Bomb import Bomb
from .SoundController import SoundController

PLAYER_PATH = path.join(path.dirname(__file__), "..", "asset", "image", "player.png")
BULLET_PATH=path.join(path.dirname(__file__),"..","asset","image","treasure.png")
ASSET_PATH = path.join(path.dirname(__file__), "../asset")


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, size: tuple, play_area_rect: pygame.Rect):
        super().__init__()
        self._play_area_rect = play_area_rect
        self._speed = 4
        self._init_pos = pos
        self.rect = pygame.Rect(*pos, *size)
        self._score = 0
        self.bullets=[Bullet((-2.5,-2.5),(5,5))]
        self.bombs=pygame.sprite.Group()
        self.bombs.add(Bomb((-25,-25),(50,50)))
        self._angle=0
        self.last_x=self.rect.x
        self.last_y=self.rect.y
        self.used_frame=0
        self.last_shoot=0
        self.sound_controller=SoundController()

    def update(self, action) -> None:
        self.last_x=self.rect.x
        self.last_y=self.rect.y  
        print(action)
        while(self._angle<0):
            self._angle+=360
        for i in range(0,len(action)):
            if action[i] == "UP":
                if(self._angle%360==0 and self.rect.top > self._play_area_rect.top):
                        self.rect.centery-=self._speed
                elif(self._angle%360==90 and self.rect.left > self._play_area_rect.left):
                    self.rect.centerx -= self._speed
                elif(self._angle%360==180 and self.rect.bottom < self._play_area_rect.bottom):
                        self.rect.centery+=self._speed
                elif (self._angle%360==270 and self.rect.right < self._play_area_rect.right):
                        self.rect.centerx+=self._speed
            elif action[i] == "DOWN" :
                if(self._angle%360==0 and self.rect.bottom < self._play_area_rect.bottom):
                        self.rect.centery+=self._speed
                elif(self._angle%360==90 and self.rect.right < self._play_area_rect.right):
                    self.rect.centerx += self._speed
                elif(self._angle%360==180 and self.rect.top > self._play_area_rect.top):
                        self.rect.centery-=self._speed
                elif (self._angle%360==270 and self.rect.left > self._play_area_rect.left):
                        self.rect.centerx-=self._speed
            elif action[i] == "LEFT":
                #self.rect.centerx -= self._speed
                self._angle+=90
            elif action[i] == "RIGHT":
                #self.rect.centerx += self._speed
                self._angle-=90
            elif action[i]=="F":
                if((self.used_frame-self.last_shoot)>5):
                    self.bullets.append(Bullet((self.rect.centerx,self.rect.centery),(5,5)))
                    self.sound_controller.play_sound(music_path=path.join(ASSET_PATH,"sound","shoot.wav"),volume=0.4,maz_time=100)
                    self.last_shoot=self.used_frame
            elif action[i]=="SHOOT":
                for i in range(0,len(self.bullets)):
                    self.bullets[i].shoot()
            elif action[i]=="LAY_BOMB":
                self.bombs.add(Bomb((self.rect.left,self.rect.top),(50,50)))
        if(self.bullets[-1].rect.centery<0):
            self.bullets=[(Bullet((-2.5,-2.5),(5,5)))]
        self.used_frame+=1

    @property
    def score(self):
        return self._score

    @property
    def xy(self):
        return self.rect.topleft

    def reset(self):
        self.rect.topleft = self._init_pos

    def collide_with_walls(self):
        #self._score+=1
        """delta_x=self.rect.x-self.last_x
        delta_y=self.rect.y-self.last_y
        self.rect.x-=delta_x
        self.rect.y-=delta_y"""
        self.rect.x=self.last_x
        self.rect.y=self.last_y
        #print("a")
        pass

    def collide_with_mobs(self):
        self._score+=1
        pass
    def shoot_success(self):
        self._score+=10
    def collide_with_treasures(self):
        self._score+=100

    @property
    def game_object_data(self):
        return create_image_view_data(image_id="player", x=self.rect.x, y=self.rect.y,
                                      width=self.rect.width, height=self.rect.height, angle=self._angle*math.pi/180)

    @property
    def game_init_object_data(self):
        return create_asset_init_data(image_id="player",
                                      width=self.rect.width, height=self.rect.height,
                                      file_path=PLAYER_PATH,
                                      github_raw_url="https://raw.githubusercontent.com/Jesse-Jumbo/GameFramework/main/MyGame/asset/image/player.png")

class Bullet:
    def __init__(self,pos,size):
        self.rect=pygame.Rect(*pos,*size)
        self._speed=5
    def shoot(self):
        self.rect.centery-=self._speed
    @property
    def game_object_data(self):
        return create_image_view_data(image_id="bullet", x=self.rect.x, y=self.rect.y,
                                      width=self.rect.width, height=self.rect.height, angle=0)
    @property
    def game_init_object_data(self):
        return create_asset_init_data(image_id="bullet",
                                      width=self.rect.width, height=self.rect.height,
                                      file_path=BULLET_PATH,
                                      github_raw_url="")
    
