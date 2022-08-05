from enum import auto
from os import path

import pygame
from mlgame.utils.enum import StringEnum
from mlgame.view.view_model import create_asset_init_data, create_image_view_data

import env

PLAYER_PATH = path.join(path.dirname(__file__), "..", "asset", "image", "player.png")
BULLET_PATH=path.join(path.dirname(__file__),"..","asset","image","treasure.png")


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, size: tuple, play_area_rect: pygame.Rect):
        super().__init__()
        self._play_area_rect = play_area_rect
        self._speed = 5
        self._init_pos = pos
        self.rect = pygame.Rect(*pos, *size)
        self._score = 0
        self.bullet=[Bullet((self.rect.centerx,self.rect.centery),(5,5))]

    def update(self, action: str) -> None:
        if action == "UP" and self.rect.top > self._play_area_rect.top:
            self.rect.centery -= self._speed
        elif action == "DOWN" and self.rect.bottom < self._play_area_rect.bottom:
            self.rect.centery += self._speed
        elif action == "LEFT" and self.rect.left > self._play_area_rect.left:
            self.rect.centerx -= self._speed
        elif action == "RIGHT" and self.rect.right < self._play_area_rect.right:
            self.rect.centerx += self._speed
        elif action=="F":
            self.bullet.append(Bullet((self.rect.centerx,self.rect.centery),(5,5)))
        elif action=="SHOOT":
            if(self.bullet[-1].rect.centery<0):
                self.bullet=[(Bullet((self.rect.centerx,self.rect.centery),(5,5)))]
            else:
                for i in range(0,len(self.bullet)):
                    self.bullet[i].shoot()

    @property
    def score(self):
        return self._score

    @property
    def xy(self):
        return self.rect.topleft

    def reset(self):
        self.rect.topleft = self._init_pos

    def collide_with_walls(self):
        self._score+=1
        pass

    def collide_with_mobs(self):
        self._score+=1
        pass

    @property
    def game_object_data(self):
        return create_image_view_data(image_id="player", x=self.rect.x, y=self.rect.y,
                                      width=self.rect.width, height=self.rect.height, angle=0)

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
        pass
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
