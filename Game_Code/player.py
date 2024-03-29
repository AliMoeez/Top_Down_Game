import pygame
import math

from Game_Asset_Code import *
from .lose import Lose
from .win import Win

class Player:
    def __init__(self,player_x,player_y,player_width,player_height,player_rect,level_1,player_control,dialogue_condition,
                 dialogue_story_condition,reset_locations,tutorial_one,tutorial_two,
                 level_1_wizard_talk,talk_to_abyss_level_one,investigate_object_level_one,level_2,level_3,level_4):
        Lose.__init__(self,level_1,player_lose_condition,reset_locations,level_2,level_3,level_4)
        Win.__init__(self,level_1,level_2,level_1_wizard_talk,talk_to_abyss_level_one,investigate_object_level_one,level_3,level_3_player_talk_4,level_4)
        self.player_x=player_x ; self.player_y=player_y ; self.player_width=player_width ; self.player_height=player_height ; self.player_rect=player_rect ; self.player_x_movement=player_x_movement ; self.player_y_movement=player_y_movement
        self.camera_x_y=camera_x_y  ; self.level_1=level_1 ;  self.level_screen=level_screen ; self.player_key=player_key ; self.player_attack_cooldown=player_attack_cooldown ; self.level_1_tile_set_rect=level_1_tile_set_rect ; self.player_health=player_health
        self.player_control_cooldown=player_control_cooldown ; self.player_control=player_control ; self.object_rect=object_rect ; self.dialogue_condition=dialogue_condition ; self.elder_attack_poison_effect=elder_attack_poison_effect
        self.dialogue_story_condition=dialogue_story_condition ; self.reset_locations=reset_locations ; self.tutorial_one=tutorial_one ; self.tutorial_two=tutorial_two ; self.level_4=level_4 ; self.final_boss_player_stop=final_boss_player_stop
        self.level_1_wizard_talk=level_1_wizard_talk ; self.talk_to_abyss_level_one=talk_to_abyss_level_one ; self.investigate_object_level_one=investigate_object_level_one ; self.level_4_tile_set_rect=level_4_tile_set_rect
        self.level_2=level_2 ; self.level_2_tile_set_rect=level_2_tile_set_rect ; self.level_3=level_3 ; self.level_3_tile_set_rect=level_3_tile_set_rect ; self.general_boss_player_slow_down_number=general_boss_player_slow_down_number

        if self.level_1:
            self.tile_set_rect=self.level_1_tile_set_rect

        if self.level_2:
            self.tile_set_rect=self.level_2_tile_set_rect
            
        if self.level_3:
            self.tile_set_rect=self.level_3_tile_set_rect

        if self.level_4:
            self.tile_set_rect=self.level_4_tile_set_rect


    def idle(self,key):
        self.player_idle_list=player_idle_list ; self.player_idle_list_flip=player_idle_list_flip ; self.player_idle_number=player_idle_number

        if self.player_key[-1]=="d": SCREEN.blit(self.player_idle_list[int(self.player_idle_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
        else: SCREEN.blit(self.player_idle_list_flip[int(self.player_idle_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-60,self.player_rect.y-self.camera_x_y[1]-40))

        self.player_x_movement[0]=0 ; self.player_y_movement[0]=0

        if len(self.player_key)>5: del self.player_key[0]
        
        self.player_idle_number[0]+=0.15
        if self.player_idle_number[0]>7: self.player_idle_number[0]=0

        self.player_attack_cooldown[0]+=0.02/2
        if self.player_attack_cooldown[0]>4: self.player_attack_cooldown[0]=4

    def move(self,key):
        self.player_run_list=player_run_list ; self.player_run_list_flip=player_run_list_flip ; self.player_run_number=player_run_number
        if (any([self.level_1,self.level_2,self.level_3,self.level_4]) and not (self.tutorial_one or self.tutorial_two) and not Win.condition(self) and not key[pygame.K_e] and not self.dialogue_condition and not self.dialogue_story_condition
             and not self.player_health[0]<=0 or self.player_attack_cooldown[0]<=0)  :
            if key[pygame.K_d] and not key[pygame.K_a]:
                SCREEN.blit(self.player_run_list[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
                self.player_x_movement[0]=30 ; self.player_key.append("d")
                if key[pygame.K_w]:
                    self.player_x_movement[0]=math.sqrt(300) ; self.player_y_movement[0]=-math.sqrt(300)
                elif key[pygame.K_s]:
                    self.player_x_movement[0]=math.sqrt(300) ; self.player_y_movement[0]=math.sqrt(300)

            elif key[pygame.K_w] and not key[pygame.K_s] : 
                self.player_y_movement[0]=-30
                if self.player_key[-1]=="d": SCREEN.blit(self.player_run_list[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
                else: SCREEN.blit(self.player_run_list_flip[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-60,self.player_rect.y-self.camera_x_y[1]-40))

            elif key[pygame.K_a] and not key[pygame.K_d]:
                SCREEN.blit(self.player_run_list_flip[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-60,self.player_rect.y-self.camera_x_y[1]-40))
                self.player_x_movement[0]=-30 ; self.player_key.append("a")
                if key[pygame.K_w]:
                    self.player_x_movement[0]=-math.sqrt(300); self.player_y_movement[0]=-math.sqrt(300)
                elif key[pygame.K_s]:
                    self.player_x_movement[0]=-math.sqrt(300) ; self.player_y_movement[0]=math.sqrt(300)

            elif key[pygame.K_s] and not key[pygame.K_w]: 
                self.player_y_movement[0]=30 #3
                if self.player_key[-1]=="d": SCREEN.blit(self.player_run_list[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
                else: SCREEN.blit(self.player_run_list_flip[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-60,self.player_rect.y-self.camera_x_y[1]-40))
            
            else: 
                Player.idle(self,key) ; self.player_x_movement[0]=0 ; self.player_y_movement[0]=0

            self.player_run_number[0]+=0.15
            if self.player_run_number[0]>7:self.player_run_number[0]=0

            self.player_attack_cooldown[0]+=0.01/2
            if self.player_attack_cooldown[0]>4: self.player_attack_cooldown[0]=4

        if Win.condition(self):
            self.player_x_movment[0]=0
            self.player_y_movement[0]=0
            Player.idle(self,key)

    def attack(self,key):
        self.player_attack_list=player_attack_list ; self.player_attack_list_flip=player_attack_list_flip ; self.player_attack_number=player_attack_number
        if any([self.level_1,self.level_2,self.level_3,self.level_4]) and not (self.tutorial_one or self.tutorial_two) and key[pygame.K_e]  and not Win.condition(self)  and self.player_attack_cooldown[0]>0 and not self.dialogue_condition and not self.dialogue_story_condition and not self.player_health[0]<=0 :
            self.player_x_movement[0]=0 ; self.player_y_movement[0]=0

            if self.player_key[-1]=="d":
                SCREEN.blit(self.player_attack_list[int(self.player_attack_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
            else:
                SCREEN.blit(self.player_attack_list_flip[int(self.player_attack_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-60,self.player_rect.y-self.camera_x_y[1]-40))
            self.player_attack_number[0]+=0.15
            if self.player_attack_number[0]>7: 
                self.player_attack_number[0]=0
                self.player_attack_cooldown[0]-=1
        if not key[pygame.K_e]: self.player_attack_number[0]=0

    def control(self,key):
        if any([self.level_1,self.level_2,self.level_3,self.level_4]):
            if self.player_control and self.player_control_cooldown[0]>0:
                self.player_control_cooldown[0]-=0.01/2 #0.01/2
                self.player_x_movement[0]=0 ; self.player_y_movement[0]=0

            if not self.player_control:
               self.player_control_cooldown[0]+=0.1/2 #0.001/2

            if self.player_control_cooldown[0]<=0: self.player_control_cooldown[0]=0
            if self.player_control_cooldown[0]>=1: self.player_control_cooldown[0]=1

    def dialouge_state(self,key):
        if any([self.level_1,self.level_2,self.level_3,self.level_4]) and (self.dialogue_condition or self.dialogue_story_condition) and self.player_health[0]>0:
            Player.idle(self,key)

    def health_power_cooldown_icons(self):
        self.maximum_health=1000 ; self.health_bar_length=500 ; self.health_bar_ratio=self.maximum_health/self.health_bar_length ; self.health_icon=health_icon
        self.sword_icon=sword_icon ; self.potion_icon=potion_icon ; self.final_boss_poison_colour=(88,136,0)
        if any([self.level_1,self.level_2,self.level_3,self.level_4]):

            if self.level_4 and self.elder_attack_poison_effect[0]<10: self.colour_health_bar=self.final_boss_poison_colour
            else: self.colour_health_bar=(178,34,34)

            
            self.health_icons=pygame.draw.rect(SCREEN,self.colour_health_bar,pygame.Rect(20,10,self.player_health[0]/self.health_bar_ratio,25))
            SCREEN.blit(self.health_icon,(32,14)) ; self.health_border=pygame.draw.rect(SCREEN,(220,220,220),pygame.Rect(20,10,self.health_bar_length,25),4) 

            self.attack_cool_down_icon=pygame.draw.rect(SCREEN,(30,144,255),pygame.Rect(20,40,((self.player_attack_cooldown[0]*100)/2)*2.5,25))
            SCREEN.blit(self.sword_icon,(32,44)) ; self.attack_cool_down_border=pygame.draw.rect(SCREEN,(220,220,220),pygame.Rect(20,40,500,25),4)

            self.control_icon=pygame.draw.rect(SCREEN,(148,0,211),pygame.Rect(20,70,(self.player_control_cooldown[0]*1000/2),25))
            SCREEN.blit(self.potion_icon,(32,74)) ; self.control_border=pygame.draw.rect(SCREEN,(220,220,220),pygame.Rect(20,70,500,25),4)

    def fall(self):
        self.player_fall_list=player_fall_list ; self.player_fall_list_flip=player_fall_list_flip ; self.player_fall_number=player_fall_number
        if any([self.level_1,self.level_2,self.level_3,self.level_4]): 
            if self.player_health[0]<=0:
                self.player_x_movement[0]=0 ; self.player_y_movement[0]=0
                if self.player_key[-1]=='d':
                    SCREEN.blit(self.player_fall_list[int(self.player_fall_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
                else:
                    SCREEN.blit(self.player_fall_list_flip[int(self.player_fall_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-60,self.player_rect.y-self.camera_x_y[1]-40))
                self.player_fall_number[0]+=0.15
                if self.player_fall_number[0]>7:
                    self.player_fall_number[0]=7

    def reset_position(self):
        if self.reset_locations:
            if self.level_1 or self.level_2 or self.level_3 or self.level_4:
                self.general_boss_player_slow_down_number[0]=0
             #   print("PLAYER RESET")
                Lose.reset_positions(self,player_rect,self.player_x,self.player_y)
                return True

    def collision_with_object(self):
        if any([self.level_1,self.level_2,self.level_3,self.level_4]):
            self.tile_hit=[]
            for tiles in self.tile_set_rect:
                if self.player_rect.colliderect(tiles):
                    self.tile_hit.append(tiles)
            return self.tile_hit
        
    def player_speed_changes(self):
        if self.level_3:
            if self.general_boss_player_slow_down_number[0]>0:
                self.general_boss_player_slow_down_number[0]-=5
                self.player_x_movement[0]=self.player_x_movement[0]//35
                self.player_y_movement[0]=self.player_y_movement[0]//35
            else:
                self.general_boss_player_slow_down_number[0]=0
        if self.level_4:
            if self.final_boss_player_stop[0]==1:
                self.player_x_movement[0]=0
                self.player_y_movement[0]=0
                    
    def collision_with_object_logic(self):
        if any([self.level_1,self.level_2,self.level_3,self.level_4]):
            self.player_rect.x+=self.player_x_movement[0]
            collision=Player.collision_with_object(self)
            for tile in collision:
                if self.player_x_movement[0]>0:
                    self.player_rect.right=tile.left
                if self.player_x_movement[0]<0:
                    self.player_rect.left=tile.right
            self.player_rect.y+=self.player_y_movement[0]
            collision=Player.collision_with_object(self)
            for tile in collision:
                if self.player_y_movement[0]>0:
                    self.player_rect.bottom=tile.top
                if self.player_y_movement[0]<0:
                    self.player_rect.top=tile.bottom


