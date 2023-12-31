import pygame
import math

from Game_Asset_Code import *


class LevelTwo:
    def __init__(self,level_2,level_screen):
        self.level_2=level_2
        self.level_screen=level_screen
        self.level_2_tile_set=level_2_tile_set 
        self.level_2_tile_set_rect=level_2_tile_set_rect
        self.camera_x_y=camera_x_y
        self.player_rect=player_rect
        self.object_rect=object_rect
        self.frost_boss_health=frost_boss_health

    def object_player_distance(self,x_val,y_val):
        self.object_player_distance_list=[]
        self.distance=math.hypot(self.player_rect.x-x_val,self.player_rect.y-y_val)
        self.object_player_distance_list.append(self.distance)
        return self.object_player_distance_list

    def border(self):
        self.player_control=player_control ; self.player_control_cooldown=player_control_cooldown ; self.enemy_rects=enemy_1_level_1_rect+enemy_2_rects  ; self.player_control_index=player_control_index
      #  self.enemy_rects_camera=Control.enemy_camera(self) 
        self.max_x_border=2482 ; self.max_y_border=2000 ; self.min_x_border=530 ; self.min_y_border=300
        self.max_x_player=3072 ; self.max_y_player=2415; self.min_x_player=50 ; self.min_y_player=25
      
      #  if self.player_control and self.player_control_cooldown[0]>0: self.rect_camera=self.enemy_rects_camera
      #else
        self.rect_camera=self.player_rect

        if self.level_2: 
            SCREEN.fill((132,145,65))
            if self.rect_camera.x>self.min_x_border and self.rect_camera.x<self.max_x_border and self.rect_camera.y>self.min_y_border and self.rect_camera.y<self.max_y_border:
                LevelTwo.border_logic_total(self)
            if (self.rect_camera.x<self.min_x_border or self.rect_camera.x>self.max_x_border) and not self.rect_camera.y<self.min_y_border and not self.rect_camera.y>self.max_y_border:
                LevelTwo.border_logic_y_axis(self)
            if (self.rect_camera.y<self.min_y_border or self.rect_camera.y>self.max_y_border) and not self.rect_camera.x<self.min_x_border and not self.rect_camera.x>self.max_x_border:
                LevelTwo.border_logic_x_axis(self)
            if (self.rect_camera.y<self.min_y_border or self.rect_camera.y>self.max_y_border) and (self.rect_camera.x<self.min_x_border or self.rect_camera.x>self.max_x_border):
                LevelTwo.border_logic_x_y_axis(self)

    def win_condition(self):
        if self.level_2 and self.frost_boss_health[0]<=0:
            return True

    def tile_set_general_function(self,layers:str):
        if self.level_2:
            for layer in self.level_2_tile_set:
                if layer.name in [layers]:
                    for tile in layer.tiles():
                        x_val=tile[0]*16 ; y_val=tile[1]*16
                        for distance in LevelTwo.object_player_distance(self,x_val,y_val):
                            if distance<1000:
                                SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))
                 
    def tile_layer_flooring(self): 
        LevelTwo.tile_set_general_function(self,"Tile Layer 1")

    def tile_layer_plants(self):
        LevelTwo.tile_set_general_function(self,"Tile Layer 2")

    def tile_layer_collision(self):
        if self.level_2:
            for layer in self.level_2_tile_set:
                if layer.name in ["Tile Layer 3"]:
                    for tile in layer.tiles():
                        x_val=tile[0]*16 ; y_val=tile[1]*16
                        for distance in LevelTwo.object_player_distance(self,x_val,y_val):
                            if distance<1000:
                                SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))
                            if distance<100:
                                self.level_2_tile_set_rect.append(pygame.Rect(x_val,y_val,16,16))

    def tile_layer_tree_tops(self):
        if self.level_2:
            for layer in self.level_2_tile_set:
                if layer.name in ["Tile Layer 4"]:
                    for tile in layer.tiles():
                        x_val=tile[0]*16 ; y_val=tile[1]*16
                        for distance in LevelTwo.object_player_distance(self,x_val,y_val):
                            if distance<1000:
                                SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))

    def tile_layer_dialogue_objects(self):
        if self.level_2:
            for layer in self.level_2_tile_set:
                if layer.name in ["Tile Layer 5"]:
                    for tile in layer.tiles():
                        x_val=tile[0]*16 ; y_val=tile[1]*16
                        for distance in LevelTwo.object_player_distance(self,x_val,y_val):
                            if distance<1000:
                                SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))
                            if distance<100:
                                self.object_rect.append(pygame.Rect(x_val,y_val,16,16))

    def border_logic_total(self):
        self.camera_x_y[0]+=self.rect_camera.x-self.camera_x_y[0]-525
        self.camera_x_y[1]+=self.rect_camera.y-self.camera_x_y[1]-self.min_y_border

    def border_logic_y_axis(self):
        self.camera_x_y[0]+=0
        self.camera_x_y[1]+=self.rect_camera.y-self.camera_x_y[1]-self.min_y_border
        if self.rect_camera.x<self.min_x_player: self.rect_camera.x=self.min_x_player
        if self.rect_camera.x>self.max_x_player: self.rect_camera.x=self.max_x_player

    def border_logic_x_axis(self):
        self.camera_x_y[0]+=self.rect_camera.x-self.camera_x_y[0]-525
        self.camera_x_y[1]+=0
        if self.rect_camera.y<self.min_y_player: self.rect_camera.y=self.min_y_player
        if self.rect_camera.y>self.max_y_player:self.rect_camera.y=self.max_y_player
            
    def border_logic_x_y_axis(self):
        self.camera_x_y[0]+=0 ; self.camera_x_y[1]+=0
        if self.rect_camera.y<self.min_y_player: self.rect_camera.y=self.min_y_player
        if self.rect_camera.x<self.min_x_player: self.rect_camera.x=self.min_x_player
        if self.rect_camera.x>self.max_x_player: self.rect_camera.x=self.max_x_player
        if self.rect_camera.y>self.max_y_player:self.rect_camera.y=self.max_y_player
