import pygame
import sys
import math
from pytmx.util_pygame import load_pygame

pygame.init()

pygame.display.set_caption("Revenge's Peak")

pygame.mixer.music.load(r"Assets\Misc\Music\BeepBox-Song.wav")
pygame.mixer.music.play(-1)

from Game_Asset_Code import *
from Game_Code import Menu,LevelOne,LevelTwo,LevelThree,LevelFour,Player,EnemyOne,EnemyTwo,EnemyThree,Dialouge,People,Objectives,Lose,Tutorial,Win,FrostBoss,GeneralBoss,FinalBoss,HealingPlayer


while run:
    level_1_tile_set_rect.clear()
    level_2_tile_set_rect.clear()
    level_3_tile_set_rect.clear()
    level_4_tile_set_rect.clear()
    object_rect.clear()
    key=pygame.key.get_pressed()
    event_list=pygame.event.get()
    

    menu=Menu(level_screen,music_state,level_1,level_2)
    levelone=LevelOne(camera_x_y,level_1,level_screen,level_1_wizard_talk,talk_to_abyss_level_one,investigate_object_level_one)
    leveltwo=LevelTwo(level_2,level_screen)
    levelthree=LevelThree(level_3,level_3_player_talk_3,level_3_player_talk_4)
    levelfour=LevelFour(level_4,level_screen)

    player=Player(player_x,player_y,player_width,player_height,player_rect,level_1,
                  player_control,dialogue_condition,dialogue_story_condition,
                  reset_locations,tutorial_one,tutorial_two,level_1_wizard_talk,talk_to_abyss_level_one,investigate_object_level_one,level_2,level_3,level_4)
    
    enemy_one=EnemyOne(level_1,enemy_1_level_1_rect,reset_locations,player_control,level_2,level_3,level_4,level_4_player_talk_2)
    enemy_two=EnemyTwo(level_1,enemy_2_rects,reset_locations,player_control,level_2,level_3,level_4)
    enemy_three=EnemyThree(level_3,player_control,reset_locations,level_4)
    
    people=People(level_1,level_1_wizard_talk,reset_locations,level_2)
    
    frostboss=FrostBoss(level_2,level_2_boss_talk,reset_locations)
    generalboss=GeneralBoss(level_3,level_3_player_talk_4,level_3_player_talk_3,reset_locations)
    finalboss=FinalBoss(level_4,reset_locations,level_4_player_talk_2)
    
    healingplayer=HealingPlayer(level_1,level_2,reset_locations,level_3,level_4)
    
    dialogue=Dialouge(level_1,dialogue_condition,dialogue_story_condition,level_1_wizard_talk,level_2,level_2_guard_talk,level_2_boss_talk,level_2_player_talk,level_2_enemy_talk,
                      level_3,level_3_player_talk_1,level_3_player_talk_2,level_3_player_talk_3,level_3_player_talk_4,level_3_player_lose,level_3_player_win,level_4,level_4_player_talk_1,level_4_player_talk_2,level_4_player_lose,level_4_player_win)
    
    lose=Lose(level_1,player_lose_condition,reset_locations,level_2,level_3,level_4)
    tutorial=Tutorial(level_1,tutorial_one,tutorial_two)
    win=Win(level_1,level_2,level_1_wizard_talk,talk_to_abyss_level_one,investigate_object_level_one,level_3,level_3_player_talk_4,level_4)

    for event in event_list:

        if dialogue.level_dialogue_condition(event,event_list):
            dialogue_condition=True ; dialogue_story_condition=False
            if event.type==pygame.MOUSEBUTTONDOWN : dialogue_click_list[0]+=1 ; text_position[0]=0
        
        if dialogue.level_dialogue_story(event,event_list) or dialogue.beginning_condition():
            mouse_button_blit_list.clear() ; dialogue_story_condition=True ; dialogue_condition=False
            if event.type==pygame.MOUSEBUTTONDOWN: dialogue_click_list[0]+=1 ; text_position[0]=0
        
        if (dialogue_condition or dialogue_story_condition) and dialogue.end_dialouge(event,event_list): 
            mouse_button_blit_list.clear() ; dialogue_condition=False ; dialogue_story_condition=False
            
            if level_1:
                if dialogue_objective_list[0]==1: level_1_wizard_talk=False
                if dialogue_objective_list[0]==2: talk_to_abyss_level_one=False
                if dialogue_objective_list[0]==3: investigate_object_level_one=False
            if level_2:
                if dialogue_objective_list[0]==0: level_2_player_talk=False
                if dialogue_objective_list[0]==1: level_2_guard_talk=False
                if dialogue_objective_list[0]==2: level_2_enemy_talk=False
                if dialogue_objective_list[0]==3: level_2_boss_talk=False
            if level_3:
                if dialogue_objective_list[0]==0: level_3_player_talk_1=False
                if dialogue_objective_list[0]==1: level_3_player_talk_2=False
                if dialogue_objective_list[0]==2: level_3_player_talk_3=False
                if dialogue_objective_list[0]==3: level_3_player_talk_4=False
                if dialogue_objective_list[0]==4: level_3_player_lose=True
                if dialogue_objective_list[0]==5: level_3_player_win=True
            if level_4:
                if dialogue_objective_list[0]==1: level_4_player_talk_1=False
                if dialogue_objective_list[0]==4: level_4_player_talk_2=False
                if dialogue_objective_list[0]==5: level_4_player_lose=True
                if dialogue_objective_list[0]==6: level_4_player_win=True
            
        if event.type==pygame.QUIT:
            pygame.quit() ; sys.exit()
        
        if not level_screen and not any([level_1,level_2]):
            if event.type==pygame.MOUSEBUTTONDOWN and menu.main_menu_buttons()[0].collidepoint(event.pos):
                level_screen= not level_screen
            if event.type==pygame.MOUSEBUTTONDOWN and menu.main_menu_buttons()[1].collidepoint(event.pos):
                music_state = not music_state
        
        if level_screen:
            if key[pygame.K_q]:level_screen=False
            if menu.level_screen_blit_background() is not None:
                if event.type==pygame.MOUSEBUTTONDOWN and menu.level_screen_blit_background()[0].collidepoint(event.pos):
                    level_screen=False ; level_1=True
                if event.type==pygame.MOUSEBUTTONDOWN and menu.level_screen_blit_background()[1].collidepoint(event.pos):
                    level_screen=False ; level_2=True
                if event.type==pygame.MOUSEBUTTONDOWN and menu.level_screen_blit_background()[2].collidepoint(event.pos):
                    level_screen=False ; level_3=True
                if event.type==pygame.MOUSEBUTTONDOWN and menu.level_screen_blit_background()[3].collidepoint(event.pos):
                    level_screen=False ; level_4=True
        
        if any([level_1,level_2,level_3,level_4]):
            if key[pygame.K_q]:
                level_1=False  ; level_2=False ; level_3=False ; level_4=False ; level_screen=True
            if tutorial.skip(event,event_list):
                text_position[0]=0
                if tutorial_one: tutorial_one=False
                if tutorial_two: tutorial_two=False
            if tutorial.begin_tutorial(event,event_list): tutorial_two=True

            if level_2 or level_3 or level_4:
                tutorial_one=False ; tutorial_two=False

            if key[pygame.K_f] and player_control_cooldown[0]==1:
                for idx,distance in enumerate(enemy_one.distance()):
                    if distance<100:
                        player_control_index.clear() ; player_control_index.append((idx,"Enemy_1"))  ; player_control=True                
                for idx,distance in enumerate(enemy_two.distance()):
                    if distance<100:
                        player_control_index.clear() ; player_control_index.append((idx,"Enemy_2")) ; player_control=True
                for idx,distance in enumerate(enemy_three.distance()):
                    if distance<100:
                        player_control_index.clear() ; player_control_index.append((idx,"Enemy_3")) ; player_control=True

    
            if key[pygame.K_v] and player_control: player_control_cooldown[0]=-0.05

        if lose.retry(event):
            if level_2:
                level_2_player_talk=True ; level_2_guard_talk=True ;level_2_enemy_talk=True ; level_2_boss_talk=True
            if level_3:
                camera_x_y[0]=0 ; camera_x_y[1]=0 ; level_3_player_talk_1=True ; level_3_player_talk_2=True ; level_3_player_talk_3=True ; level_3_player_talk_4=True
            if level_4:
                camera_x_y[0]=0 ; camera_x_y[1]=0 ; level_4_player_talk_1=True ; level_4_player_talk_2=True ; level_4_player_lose=False ; level_4_player_win=False

            player_lose_condition=False ; reset_locations=True ;dialogue_objective_list[0]=0 

        if lose.back_to_menu(event):
            player_lose_condition=False ; reset_locations=True ; level_1=False ; level_2=False ; level_3=False ; level_4=False
            if level_2:
                level_2_player_talk=True ; level_2_guard_talk=True ;level_2_enemy_talk=True ; level_2_boss_talk=True
            if level_3:
               level_3_player_talk_1=True ; level_3_player_talk_2=True ; level_3_player_talk_3=True ; level_3_player_talk_4=True
            if level_4:
                camera_x_y[0]=0 ; camera_x_y[1]=0 ; level_4_player_talk_1=True ; level_4_player_talk_2=True ; level_4_player_lose=False ; level_4_player_win=False
        
        if win.back_to_menu(event):
            level_1_wizard_talk=True ; talk_to_abyss_level_one=True ; investigate_object_level_one=True
            reset_locations=True
            if level_2:
                level_2_player_talk=True ; level_2_guard_talk=True ;level_2_enemy_talk=True ; level_2_boss_talk=True 
            if level_3:
                camera_x_y[0]=0 ; camera_x_y[1]=0  ; level_3_player_talk_1=True ; level_3_player_talk_2=True ; level_3_player_talk_3=True ; level_3_player_talk_4=True ; level_3_player_lose=False ; level_3_player_win=False
            if level_4:
                camera_x_y[0]=0 ; camera_x_y[1]=0 ; level_4_player_talk_1=True ; level_4_player_talk_2=True ; level_4_player_lose=False ; level_4_player_win=False
            level_1=False ; level_2=False ; level_3=False ; level_4=False
        
        if win.next_level(event):
            if level_1:
                level_1=False ; level_2=True
            if level_2:
                level_2=False ; level_3=True
                camera_x_y[0]=0 ; camera_x_y[1]=0 ; level_2_player_talk=True ; level_2_guard_talk=True ;level_2_enemy_talk=True ; level_2_boss_talk=True 
            if level_3:
                level_3=False; level_4=True
                camera_x_y[0]=0 ; camera_x_y[1]=0  ; level_3_player_talk_1=True ; level_3_player_talk_2=True ; level_3_player_talk_3=True ; level_3_player_talk_4=True ; level_3_player_lose=False ; level_3_player_win=False
            if level_4:
                camera_x_y[0]=0 ; camera_x_y[1]=0 ; level_4_player_talk_1=True ; level_4_player_talk_2=True ; level_4_player_lose=False ; level_4_player_win=False
            reset_locations=True

        if healingplayer.healing_condition(event):
            if player_health[0]<=1000:
                player_health[0]+=100
                if player_health[0]>1000: player_health[0]=1000
                                     
    if lose.condition():
        player_lose_condition=True
              
    if player_control_cooldown[0]<=0:
        player_control=False
        player_control_index[0]="placeholder"

    if level_1:
        if player.reset_position() and enemy_one.reset_position() and enemy_two.reset_position() and people.reset_position():
            level_1_wizard_talk=True
            reset_locations=False
    if level_2:
        if player.reset_position() and  enemy_one.reset_position() and enemy_two.reset_position() and people.reset_position() and frostboss.reset_position() and healingplayer.reset_position():
            camera_x_y[0]=0 ; camera_x_y[1]=0 
            reset_locations=False
    if level_3:
        if player.reset_position() and enemy_one.reset_position() and enemy_two.reset_position() and enemy_three.reset_position() and generalboss.reset_position():
            general_boss_player_slow_down_number[0]=0
            camera_x_y[0]=0 ; camera_x_y[1]=0
            reset_locations=False
    if level_4:
        if player.reset_position() and enemy_one.reset_position() and enemy_two.reset_position()  and enemy_three.reset_position() and finalboss.reset_position():
            print("DONE")
            camera_x_y[0]=0 ; camera_x_y[1]=0
            reset_locations=False

    if level_3:
        if all(i<=0 for i in enemy_1_health) and all(i<=0 for i in enemy_2_health) and all(i<=0 for i in enemy_3_health):
            level_3_all_enemies=True
        
    menu.main_menu()
    menu.main_menu_buttons()
    menu.level_screen_blit_background()
    menu.level_screen_blit()

    levelone.border()
    levelone.tile_set_level_direction()
    levelone.tile_set()
    levelone.win_condition()

    leveltwo.border()
    leveltwo.tile_layer_flooring()
    leveltwo.tile_layer_plants()
    leveltwo.tile_layer_dialogue_objects()
    leveltwo.tile_layer_collision()

    levelthree.background()
    levelthree.collision_tiles()
    levelthree.filler_tiles()
    levelthree.ground_tiles()
    levelthree.object_tiles()

    levelfour.border()
    levelfour.ground_layer()
    levelfour.collision_layer()
    levelfour.object_layer()

    player.move(key)
    player.attack(key)
    player.control(key)
    player.dialouge_state(key)
    player.fall()
    player.player_speed_changes()
    player.reset_position()
    player.collision_with_object()
    player.collision_with_object_logic()

    enemy_one.distance()
    enemy_one.idle(key)
    enemy_one.run(key)
    enemy_one.attack(key)
    enemy_one.player_hit()
    enemy_one.reset_position()
    enemy_one.fall()
    enemy_one.collision_with_object()
    enemy_one.collision_with_object_logic()
    enemy_one.enemy_index()
    enemy_one.control_run(key)
    enemy_one.control_attack(key)
    enemy_one.control_collision()
    enemy_one.control_collision_object_logic()

    enemy_two.distance()
    enemy_two.idle()
    enemy_two.run()
    enemy_two.attack()
    enemy_two.player_hit()
    enemy_two.fall()
    enemy_two.reset_position()
    enemy_two.collision_with_object()
    enemy_two.collision_with_object_logic()
    enemy_two.enemy_index()
    enemy_two.control_run(key)
    enemy_two.control_attack(key)
    enemy_two.control_collision()
    enemy_two.control_collision_object_logic()

    enemy_three.distance()
    enemy_three.idle()
    enemy_three.move()
    enemy_three.attack()
    enemy_three.player_hit()
    enemy_three.arrow_total_logic()
    enemy_three.fall()
    enemy_three.reset_position()
    enemy_three.collision_with_object()
    enemy_three.collision_with_object_logic()
    enemy_three.enemy_index()
    enemy_three.control_run(key)
    enemy_three.control_attack(key)
    enemy_three.control_collision()
    enemy_three.control_collision_object_logic()

    people.idle()
    people.run()

    frostboss.idle()
    frostboss.move()
    frostboss.attack()
    frostboss.player_hit()
    frostboss.fall()
    frostboss.fast_mode()
    frostboss.slow_down()
    frostboss.collision_with_object()
    frostboss.collision_with_object_logic()

    generalboss.walk_up_condition()
    generalboss.idle()
    generalboss.move()
    generalboss.attack()
    generalboss.fall()
    generalboss.reset_position()
    generalboss.player_hit(key)
    generalboss.collision_with_object()
    generalboss.collision_with_object_logic()

    finalboss.distance()
    finalboss.initial_state()
    finalboss.idle()
    finalboss.move()
    finalboss.attack_logic()
    finalboss.attack()
    finalboss.reset_position()
    finalboss.player_hit(key)
    finalboss.fall()
    finalboss.poison_effect()
    finalboss.collision_with_object()
    finalboss.collision_with_object_logic()

    healingplayer.blit()
    healingplayer.interaction()

    tutorial.player_idle_show()

    levelone.tile_set_tree_top()
    leveltwo.tile_layer_tree_tops()
    levelthree.tree_top_tiles()
    levelfour.tree_top_layer()

    player.health_power_cooldown_icons()
    frostboss.health()
    generalboss.health()
    finalboss.health()
    objectives=Objectives(level_1,level_1_wizard_talk,talk_to_abyss_level_one,investigate_object_level_one,
                          dialogue_objective_list,level_2_guard_talk,level_2_boss_talk,level_2,level_2_player_talk,level_2_enemy_talk,
                          level_3_player_talk_1,level_3_player_talk_2,level_3_player_talk_3,level_3_player_talk_4,level_3,
                          level_4,level_4_player_talk_1,level_4_player_talk_2,level_4_player_lose,level_4_player_win)
    objectives.define_level()
    objectives.level_one_objectives()
    objectives.level_two_objectives()
    objectives.level_three_objectives()
    objectives.level_four_objectives()
    objectives.show_objectives()
    
    dialogue.level_object_interaction()
    dialogue.text_type()
    dialogue.text_type_story()
    dialogue.show()

    tutorial.show()

    win.condition() 
    win.blit()

    lose.show_loss()

    pygame.display.update()