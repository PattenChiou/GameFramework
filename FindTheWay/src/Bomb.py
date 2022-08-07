from enum import auto
from os import path

import pygame
from mlgame.utils.enum import StringEnum
from mlgame.view.view_model import create_asset_init_data, create_image_view_data

import env

BOMB_PATH=path.join(path.dirname(__file__),"..","asset","image","bomb.png")

class Bomb(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.rect=pygame.Rect(*pos,*size)

    @property
    def game_object_data(self):
        return create_image_view_data(image_id="bomb", x=self.rect.x, y=self.rect.y,
                                      width=self.rect.width, height=self.rect.height, angle=0)

    @property
    def game_init_object_data(self):
        return create_asset_init_data(image_id="bomb",
                                      width=self.rect.width, height=self.rect.height,
                                      file_path=BOMB_PATH,
                                      github_raw_url="")