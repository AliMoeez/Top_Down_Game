import pygame
import math

from Game_Asset_Code import *
from .people import People
from .player import Player
from .dialogue import Dialouge

class Objectives:
    def __init__(self,level_1,level_1_wizard_talk,talk_to_abyss_level_one,investigate_obeject_level_one):
        People.__init__(self,level_1,level_1_wizard_talk)
        Player.__init__(self,player_x,player_y,player_width,player_height,player_rect,level_1,player_control,dialogue_condition,dialogue_story_condition)
        Dialouge.__init__(self,level_1,dialogue_condition,dialogue_story_condition,level_1_wizard_talk)
        self.level_1=level_1 ; self.font=r"Assets\Misc\Fonts\Pixellari.ttf"  ; self.RED=(255,55,55) ; self.level_1_wizard_talk=level_1_wizard_talk
        self.player_rect=player_rect ; self.people_level_1_rect=people_level_1_rect ; self.camera_x_y=camera_x_y ; self.red_arrow_icon=red_arrow_icon
        self.WHITE=(255,255,255) ; self.talk_to_abyss_level_one=talk_to_abyss_level_one ; self.investigate_obeject_level_one=investigate_obeject_level_one
    
    def distance(self,place_x:int,place_y:int):
        if any([self.level_1]):
            self.player_objective_distance_list=[]
            self.player_objective_distance=math.hypot(self.player_rect.x-place_x,self.player_rect.y-place_y)
            self.player_objective_distance_list.append(self.player_objective_distance)
            return self.player_objective_distance_list
    
    def level_one_objectives(self):
        #first meet with the wizard #then meet with the abyss #then defeat all enemies and then proceed to top-left corner
        if any([self.level_1]):
            
            if self.level_1_wizard_talk:
                self.objectives_distance=Objectives.distance(self,self.people_level_1_rect[0].x,self.people_level_1_rect[0].y)
                return self.objectives_distance[0],self.people_level_1_rect[0].x,self.people_level_1_rect[0].y
           
            if self.talk_to_abyss_level_one and not self.level_1_wizard_talk:
                self.objectives_distance=Objectives.distance(self,384,384)
                return self.objectives_distance[0],384,384
            
            if self.investigate_obeject_level_one and not self.talk_to_abyss_level_one:
                print("HERE")
            
    def rotation_angle(self):
        if any([self.level_1]):
            if Objectives.level_one_objectives(self) is not None:
                self.interact_x,self.interact_y=Objectives.level_one_objectives(self)[1],Objectives.level_one_objectives(self)[2]
                self.dx,self.dy=self.interact_x-self.player_rect.x, self.interact_y-self.player_rect.y            
                self.angle=math.degrees(math.atan2(-self.dy,self.dx))-90
                return self.angle
        
    def background(self):
        self.objectives_backgruond=pygame.Surface((115,100))  ; self.objectives_backgruond.set_alpha(85)  ; self.objectives_backgruond.fill(self.WHITE) 
        self.objectives_backgruond=SCREEN.blit(self.objectives_backgruond,(SCREEN_WIDTH//2-30,SCREEN_HEIGHT-790))

    def show_objectives(self):
        if any([self.level_1]):
            if Objectives.level_one_objectives(self) is not None:
                Objectives.background(self)
                self.font_title=pygame.font.Font(self.font,24) 
                self.font_title_render=self.font_title.render(f"{round(Objectives.level_one_objectives(self)[0],1)}m",True,self.RED) 
                self.arrow_icon=pygame.transform.rotate(self.red_arrow_icon,Objectives.rotation_angle(self))
                self.objective_icon=self.font_title.render(f"Objectives",True,self.RED)
                SCREEN.blit(self.objective_icon,(SCREEN_WIDTH//2-30,SCREEN_HEIGHT-790)) ; SCREEN.blit(self.arrow_icon,(SCREEN_WIDTH//2-5,SCREEN_HEIGHT-770)) ; SCREEN.blit(self.font_title_render,(SCREEN_WIDTH//2-15,SCREEN_HEIGHT-715))  