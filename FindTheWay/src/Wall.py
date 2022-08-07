import pygame
from mlgame.view.view_model import create_image_view_data,create_asset_init_data
import random
from os import path

WALL_PATH=path.join(path.dirname(__file__),"..","asset","image","stone_wall_3_reshape.png")

class Wall(pygame.sprite.Sprite):
    def __init__(self, construction:dict,**kwargs):
        super().__init__()
        self.init_pos=(construction["x"],construction["y"])
        self.init_size=(construction["width"],construction["height"])
        self.rect = pygame.Rect(self.init_pos,self.init_size)
        self.colorList=["#000000","#ffffff","#ff0000","#ffff00","#00ff00","#8c8c8c","#0000ff","#21A1F1","#00FFFF","#FF00FF","#282828","#646464","#643705","#22390A","#FF00FF","#4B4B4B","#FFA500"]
        #self.color = random.choice(self.colorList)
        self.color=kwargs["color"]

    @property
    def xy(self):
        return self.rect.topleft

    @property
    def game_object_data(self):
        return create_image_view_data(image_id="wall", x=self.rect.x, y=self.rect.y,
                                      width=self.rect.width, height=self.rect.height, angle=0)
    """def game_object_data(self):
        return create_rect_view_data(
            name="wall"
            , x=self.rect.x
            , y=self.rect.y
            , width=self.rect.width
            , height=self.rect.height
            , color=self.color
            , angle=0)"""
    @property
    def game_init_object_data(self):
        return create_asset_init_data(image_id="wall",
                                      width=self.rect.width, height=self.rect.height,
                                      file_path=WALL_PATH,
                                      github_raw_url="")









