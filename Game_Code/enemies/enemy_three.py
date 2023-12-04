import pygame

from Game_Asset_Code import * 
from .enemy_general_functions import EnemyGeneralFunctions
from Game_Code.control_test import ControlTest

class EnemyThree:
    def __init__(self,level_3,player_control) -> None:
        self.enemy_three_idle_number=enemy_three_idle_number ; self.enemy_three_move_number=enemy_three_move_number ; self.enemy_three_fall_number=enemy_three_fall_number ; self.enemy_three_attack_number=enemy_three_attack_number ; self.player_control_index=player_control_index
        self.level_3=level_3 ; self.enemy_3_health=enemy_3_health ; self.enemy_3_x_movement=enemy_3_x_movement ; self.enemy_3_y_movement=enemy_3_y_movement ; self.player_control_cooldown=player_control_cooldown
        self.player_control=player_control ; self.player_rect=player_rect ; self.camera_x_y=camera_x_y ; self.enemy_three_fall_type=enemy_three_fall_type ; self.player_health=player_health ; self.enemy_3_x_movement_control=enemy_3_x_movement_control
        self.enemy_3_y_movement_control=enemy_3_y_movement_control

        if self.level_3:
            self.tile_rect=level_3_tile_set_rect
            self.enemy_rect=enemy_3_level_3_rect
        
        if self.level_3:
            for idx,enemy in enumerate(self.enemy_rect):
                self.enemy_three_idle_number.append(0) ; self.enemy_three_move_number.append(0) ; self.enemy_three_fall_number.append(0) ; self.enemy_three_attack_number.append(0) ; self.enemy_3_health.append(100) ; self.enemy_3_x_movement.append(0) 
                self.enemy_3_y_movement.append(0) ; self.enemy_three_fall_type.append(0)
                if len(self.enemy_3_x_movement)>len(self.enemy_rect):
                    del self.enemy_three_idle_number[-1],self.enemy_3_health[1],self.enemy_3_x_movement[-1],self.enemy_3_y_movement[-1], self.enemy_three_move_number[-1]
                    del self.enemy_three_fall_number[-1],self.enemy_three_attack_number[-1],self.enemy_three_fall_type[-1]

    def distance(self):
        if any([self.level_3]):
            self.distance=EnemyGeneralFunctions.distance(self,self.enemy_rect)
            return self.distance
        
    def iscontrolled(self):
        if any([self.level_3]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_1":
            return self.player_control_index[0][0]
    
    def enemy_index(self):
        if any([self.level_3]):
            for idx,range_attacker in enumerate(self.enemy_rect):
                  if idx==self.player_control_index[0][0] and self.player_control_index[0][1]=="Enemy_3":
                      return range_attacker

    def idle(self):
        self.enemy_three_idle_list=enemy_three_idle_list ; self.enemy_three_idle_list_flip=enemy_three_idle_list_flip
        if any([self.level_3]):
            self.distance=EnemyThree.distance(self)
            
            if EnemyThree.enemy_index(self) not in self.enemy_rect:
                self.enemy_3_rects_control=self.enemy_rect
                self.enemy_3_distance_control=self.distance
            
                EnemyGeneralFunctions.idle(self,self.distance,self.player_control_index,self.enemy_3_health,self.enemy_3_x_movement,self.enemy_3_y_movement,
                                        self.enemy_three_idle_list,self.enemy_three_idle_list_flip,self.enemy_three_idle_number,self.enemy_rect,0.75,11)
            
            if EnemyThree.enemy_index(self) in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i!=EnemyThree.enemy_index(self)]
                self.enemy_3_distance_control=[i for idx, i in enumerate(self.distance) if idx!=self.player_control_index[0][0]]

                EnemyGeneralFunctions.idle_control(self,self.enemy_3_distance_control,self.player_control_index,self.enemy_3_health,self.enemy_3_x_movement,self.enemy_3_y_movement,
                                                   self.enemy_three_idle_list,self.enemy_three_idle_list_flip,self.enemy_three_idle_number,self.enemy_3_rects_control,0.75,11)
                           
    def move(self):
        self.enemy_three_move_list=enemy_three_move_list ; self.enemy_three_move_list_flip=enemy_three_move_list_flip
        if any([self.level_3]):
            self.distance=EnemyThree.distance(self)
            
            if EnemyThree.enemy_index(self) not in self.enemy_rect:
                self.enemy_3_rects_control=self.enemy_rect
                self.enemy_3_distance_control=self.distance

                EnemyGeneralFunctions.move(self,self.distance,self.player_control_index,self.enemy_3_health,self.enemy_rect,self.enemy_three_move_list,self.enemy_three_move_list_flip,
                                           self.enemy_three_move_number,self.enemy_3_x_movement,self.enemy_3_y_movement,0.75,9)

            if EnemyThree.enemy_index(self) in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i!=EnemyThree.enemy_index(self)]
                self.enemy_3_distance_control=[i for idx, i in enumerate(self.distance) if idx!=self.player_control_index[0][0]]

                EnemyGeneralFunctions.move_control(self,self.enemy_3_distance_control,self.player_control_index,self.enemy_3_health,self.enemy_3_rects_control,self.enemy_three_move_list,self.enemy_three_move_list_flip,
                                           self.enemy_three_move_number,self.enemy_3_x_movement,self.enemy_3_y_movement,0.75,9)



    def attack(self):
        self.enemy_three_attack_list=enemy_three_attack_list ; self.enemy_three_attack_list_flip=enemy_three_attack_list_flip
        if any([self.level_3]):
            self.distance=EnemyThree.distance(self)
            
            if EnemyThree.enemy_index(self) not in self.enemy_rect:
                self.enemy_3_rects_control=self.enemy_rect
                self.enemy_3_distance_control=self.distance

                EnemyGeneralFunctions.attack(self,self.distance,self.enemy_3_health,self.player_control_index,self.enemy_3_x_movement,self.enemy_3_y_movement,self.enemy_three_attack_list,
                                             self.enemy_three_attack_list_flip,self.enemy_three_attack_number,self.enemy_rect,self.enemy_three_fall_type,0.25,7,0,0,0,0,self.player_health,0)

            if EnemyThree.enemy_index(self) in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i!=EnemyThree.enemy_index(self)]
                self.enemy_3_distance_control=[i for idx, i in enumerate(self.distance) if idx!=self.player_control_index[0][0]]

                EnemyGeneralFunctions.attack_control(self,self.enemy_3_distance_control,self.enemy_3_health,self.player_control_index,self.enemy_3_x_movement,self.enemy_3_y_movement,self.enemy_three_attack_list,
                                             self.enemy_three_attack_list_flip,self.enemy_three_attack_number,self.enemy_3_rects_control,self.enemy_three_fall_type,0.75,7,0,0,0,0,self.player_health,25)

    def fall(self):
        self.enemy_three_fall_list=enemy_three_fall_list ; self.enemy_three_fall_list_flip=enemy_three_fall_list_flip
        if any([self.level_3]):
            self.distance=EnemyThree.distance(self)
            EnemyGeneralFunctions.fall(self,self.enemy_rect,self.enemy_three_fall_type,self.enemy_three_fall_list,self.enemy_three_fall_list_flip,self.enemy_three_fall_number,
                                       self.enemy_3_health,0.50,11,0,0,self.enemy_3_x_movement,self.enemy_3_y_movement)

    def collision_with_object(self):
        if any([self.level_3]):
            if EnemyThree.enemy_index(self) not in self.enemy_rect:
                return EnemyGeneralFunctions.collision_with_object(self,self.tile_rect,self.enemy_rect)
            if not EnemyThree.enemy_index(self) not in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i!=EnemyThree.enemy_index(self)]
                return EnemyGeneralFunctions.collision_with_object_control(self,self.tile_rect,self.enemy_3_rects_control)


    def collision_with_object_logic(self):
        if any([self.level_3]):
            if EnemyThree.enemy_index(self) not in self.enemy_rect:
                self.collision=EnemyThree.collision_with_object(self)
                EnemyGeneralFunctions.collision_with_object_logic(self,self.enemy_rect,self.enemy_3_x_movement,self.enemy_3_y_movement,self.collision)
            if EnemyThree.enemy_index(self) in self.enemy_rect:
                self.collision=EnemyThree.collision_with_object(self)
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i!=EnemyThree.enemy_index(self)]
                EnemyGeneralFunctions.collision_with_object_logic_control(self,self.enemy_3_rects_control,self.enemy_3_x_movement_control,self.enemy_3_control_y_movement,self.collision)      
            

    def control_run(self,key):
        if any([self.level_3]) and self.player_control and self.player_control_cooldown[0]>0 and not key[pygame.K_e] and self.player_control_index[0][1]=="Enemy_3":
            if EnemyThree.enemy_index(self)  in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i==EnemyThree.enemy_index(self)]
                ControlTest.mechanic_walk(self,key,self.enemy_three_move_list,self.enemy_3_rects_control[0],self.enemy_3_x_movement_control,self.enemy_3_y_movement_control,
                        self.enemy_three_move_list_flip,self.enemy_three_move_number,self.enemy_three_idle_list,self.enemy_three_idle_number,self.enemy_three_idle_list_flip)

    def control_attack(self,key):
        if any([self.level_3]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_3":
            if EnemyThree.enemy_index(self) in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i==EnemyThree.enemy_index(self)]
                ControlTest.mechanic_attack(self,key,self.enemy_three_attack_list,self.enemy_3_rects_control[0],self.enemy_three_attack_list_flip,
                                        self.enemy_three_attack_number,self.enemy_3_x_movement_control,self.enemy_3_y_movement_control)

    def control_collision(self):
        if any([self.level_3]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_3":
            if EnemyThree.enemy_index(self) in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i==EnemyThree.enemy_index(self)]
                ControlTest.mechanic_collision(self,self.tile_rect,self.enemy_3_rects_control[0])

    def control_collision_object_logic(self):
        if any([self.level_1,self.level_2]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_3":
            if EnemyThree.enemy_index(self)  in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_1_rects if i==EnemyThree.enemy_index(self)]
                ControlTest.mechanic_collision_logic(self,self.tile_rect,self.enemy_3_rects_control[0],self.enemy_3_x_movement_control,self.enemy_3_y_movement_control,)       