import pygame

from Game_Asset_Code import *
from .levels import LevelOne
from .levels import LevelTwo
from .levels import LevelThree
from .levels import LevelFour


class Win:
    def __init__(self,level_1,level_2,level_1_wizard_talk,talk_to_abyss_level_one,investigate_object_level_one,level_3,level_3_player_talk_4,level_4):
        LevelOne.__init__(self,camera_x_y,level_1,level_screen,level_1_wizard_talk,talk_to_abyss_level_one,investigate_object_level_one)
        LevelTwo.__init__(self,level_2,level_screen)
        LevelThree.__init__(self,level_3,level_3_player_talk_3,level_3_player_talk_4)
        LevelFour.__init__(self,level_4,level_screen)
        self.level_1=level_1 ; self.screen_fade_number=screen_fade_number ; self.WHITE=(255,255,255) ; self.RED=(220,20,60)
        self.font=r"Assets\Misc\Fonts\Pixellari.ttf" ; self.player_health=player_health
        self.level_1_wizard_talk=level_1_wizard_talk
        self.talk_to_abyss_level_one=talk_to_abyss_level_one
        self.investigate_object_level_one=investigate_object_level_one
        self.player_x_movment=player_x_movement
        self.player_y_movement=player_y_movement
        self.level_2=level_2
        self.level_3=level_3
        self.level_4=level_4
        self.level_3_player_talk_4=level_3_player_talk_4
        self.general_boss_health=general_boss_health
        self.dialogue_objective_list=dialogue_objective_list

    def condition(self):
        if any([self.level_1,self.level_2,self.level_3,self.level_4]):
            if LevelOne.win_condition(self) or LevelTwo.win_condition(self) or LevelThree.win_condition(self) or LevelFour.win_condition(self):
                print("HERERERERERERERE")
                self.player_x_movment[0]=0 ; self.player_y_movement[0]=0 ; self.dialogue_objective_list[0]=0
                return True

    def screen_fade(self):
        self.screen_fade=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))  ; self.screen_fade.set_alpha(self.screen_fade_number[0]) 
        self.screen_fade.fill((0,0,0))  ; SCREEN.blit(self.screen_fade,(0,0))
     
    def text(self):
        self.font_title=pygame.font.Font(self.font,52) 
        self.font_title_render=self.font_title.render("YOU WIN",True,self.RED) ; SCREEN.blit(self.font_title_render,(SCREEN_WIDTH//2-150,SCREEN_HEIGHT-700))  
    
        self.font_main_menu=pygame.font.Font(self.font,34) 
        self.font_main_menu_render=self.font_main_menu.render("Main Menu",True,self.RED)

        self.font_next_level=pygame.font.Font(self.font,34) 
        self.font_next_level_render=self.font_next_level.render("Next Level",True,self.RED)


    def buttons(self):
        Win.text(self)
        if not self.level_4:
            self.font_menu_surface=pygame.Surface((170,50))  ; self.font_menu_surface.set_alpha(0)  ; self.font_menu_surface.fill(self.WHITE)
            self.font_menu_surface_blit=SCREEN.blit(self.font_menu_surface,(SCREEN_WIDTH//2-310,SCREEN_HEIGHT-407)) 
            self.main_menu_blit=SCREEN.blit(self.font_main_menu_render,(SCREEN_WIDTH//2-300,SCREEN_HEIGHT-400))

            self.font_next_level_surface=pygame.Surface((180,50))  ; self.font_next_level_surface.set_alpha(0)  ; self.font_next_level_surface.fill(self.WHITE)
            self.font_next_level_surface_blit=SCREEN.blit(self.font_next_level_surface,(SCREEN_WIDTH//2+90,SCREEN_HEIGHT-407)) 
            self.next_level_blit=SCREEN.blit(self.font_next_level_render,(SCREEN_WIDTH//2+100,SCREEN_HEIGHT-400))
        
        if self.level_4:
            self.font_menu_surface=pygame.Surface((170,50))  ; self.font_menu_surface.set_alpha(0)  ; self.font_menu_surface.fill(self.WHITE)
        
            self.font_menu_surface_blit=SCREEN.blit(self.font_menu_surface,(SCREEN_WIDTH//2-110,SCREEN_HEIGHT-407)) 
            self.main_menu_blit=SCREEN.blit(self.font_main_menu_render,(SCREEN_WIDTH//2-100,SCREEN_HEIGHT-400))


    def blit(self):
        if Win.condition(self):
            self.screen_fade_number[0]+=2
            if self.screen_fade_number[0]>100:
                self.screen_fade_number[0]=100
            Win.screen_fade(self)
            Win.buttons(self)
            Win.text(self)

    def back_to_menu(self,event):
        if Win.condition(self):
            Win.text(self)
            Win.buttons(self)
            if event.type==pygame.MOUSEBUTTONDOWN and self.main_menu_blit.collidepoint(pygame.mouse.get_pos()):
                self.player_health[0]=1000
                return True
            
    def next_level(self,event):
        if Win.condition(self):
            Win.text(self)
            Win.buttons(self)
            if not self.level_4:
                if event.type==pygame.MOUSEBUTTONDOWN and self.next_level_blit.collidepoint(pygame.mouse.get_pos()):
                    self.player_health[0]=1000
                    return True