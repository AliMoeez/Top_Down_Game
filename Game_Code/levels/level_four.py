import pygame

from Game_Asset_Code import *

class LevelFour:
    def __init__(self,level_4,level_screen) -> None:
        self.level_4=level_4
        self.level_4_tile_set=level_4_tile_set
        self.level_4_tile_set_rect=level_4_tile_set_rect
        self.player_rect=player_rect
        self.camera_x_y=camera_x_y
        self.level_screen=level_screen
        self.object_rect=object_rect
        self.final_boss_health=final_boss_health

    def border(self):
        self.player_control=player_control ; self.player_control_cooldown=player_control_cooldown ; self.enemy_rects=enemy_1_level_1_rect+enemy_2_rects  ; self.player_control_index=player_control_index
      #  self.enemy_rects_camera=Control.enemy_camera(self) 
        self.max_x_border=4000 ; self.max_y_border=2000 ; self.min_x_border=530 ; self.min_y_border=300
        self.max_x_player=4590 ; self.max_y_player=2415; self.min_x_player=50 ; self.min_y_player=25
      
        if self.player_control and self.player_control_cooldown[0]>0: self.rect_camera=self.enemy_rects_camera
        else: self.rect_camera=self.player_rect

        if self.level_4: 
            self.level_screen=False
            SCREEN.fill((131,164,72))
            if self.rect_camera.x>self.min_x_border and self.rect_camera.x<self.max_x_border and self.rect_camera.y>self.min_y_border and self.rect_camera.y<self.max_y_border:
                 LevelFour.border_logic_total(self)
            if (self.rect_camera.x<self.min_x_border or self.rect_camera.x>self.max_x_border) and not self.rect_camera.y<self.min_y_border and not self.rect_camera.y>self.max_y_border:
                LevelFour.border_logic_y_axis(self)
            if (self.rect_camera.y<self.min_y_border or self.rect_camera.y>self.max_y_border) and not self.rect_camera.x<self.min_x_border and not self.rect_camera.x>self.max_x_border:
                LevelFour.border_logic_x_axis(self)
            if (self.rect_camera.y<self.min_y_border or self.rect_camera.y>self.max_y_border) and (self.rect_camera.x<self.min_x_border or self.rect_camera.x>self.max_x_border):
                LevelFour.border_logic_x_y_axis(self)

    
    def tile_general_function(self,layers:str):
        if self.level_4:
            for layer in self.level_4_tile_set:
                if layer.name in [layers]:
                    for tile in layer.tiles():
                        x_val=tile[0]*32 ; y_val=tile[1]*32
                        SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))

    def tile_general_collision_functions(self,layers:str,append_list:list):
        if self.level_4:
            for layer in self.level_4_tile_set:
                if layer.name in [layers]:
                    for tile in layer.tiles():
                        x_val=tile[0]*32 ; y_val=tile[1]*32
                        SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))
                        append_list.append(pygame.Rect(x_val,y_val,32,32))

    
    def win_condition(self):
        if self.level_4 and self.final_boss_health[0]<=0:
            return True
        return False
    
    def ground_layer(self):
        LevelFour.tile_general_function(self,"Tile Layer 1")

    def tree_top_layer(self):
        LevelFour.tile_general_function(self,"Tile Layer 2")

    def collision_layer(self):
        LevelFour.tile_general_collision_functions(self,"Tile Layer 3",self.level_4_tile_set_rect)

    def object_layer(self):
        LevelFour.tile_general_collision_functions(self,"Tile Layer 4",self.object_rect)
        
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