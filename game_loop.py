import pygame
import os

from game_state import GameState

pygame.init()

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.display.init()

pygame.mixer.init()

joystick = pygame.joystick.Joystick(0)

flowdot_snd_path = "/home/elie/Bureau/Livecoding/flowdot/FoxDot/snd/1/"
sound = pygame.mixer.Sound(flowdot_snd_path + "v/lower/000_BassLow_Default.wav")
# sound.play()

# Button
button_a = 0
button_b = 1
button_x = 2
button_y = 3
button_LB = 4
button_RB = 5
button_back = 6
button_start = 7

# Axis
joy_left_h = 0
joy_left_v = 1
joy_right_h = 3
joy_right_v = 4
button_LT = 2
button_RT = 5

# Hat
cross_key_left = (-1,0)
cross_key_right = (1,0)
cross_key_up = (0,1)
cross_key_down = (0,-1)

toggle_axis_dict = { axis_number: 0 for axis_number in range(6)}
def toggle_axis(axis_number, threshold_up = .7, threshold_down = .5):
    axis_value = joystick.get_axis(axis_number)
    # print(toggle_axis_dict)
    # print(joystick.get_axis(axis_number))
    if axis_value > threshold_up and toggle_axis_dict[axis_number] != 1:
        toggle_axis_dict[axis_number] = 1
        return True
    if axis_value < threshold_down and axis_value >= 0 and toggle_axis_dict[axis_number] != 0:
        toggle_axis_dict[axis_number] = 0
        return False
    if axis_value < -threshold_up and toggle_axis_dict[axis_number] != -1:
        toggle_axis_dict[axis_number] = -1
        return True
    if axis_value > -threshold_down and axis_value <= 0 and toggle_axis_dict[axis_number] != 0:
        toggle_axis_dict[axis_number] = 0
        return False
    return False

game_state = GameState()

running = True
while running:
    for event in pygame.event.get():
        # try:
            if event.type == pygame.JOYBUTTONDOWN:
                # game_state.update_players()
                if joystick.get_button(button_a):
                    game_state.last_push("button a !")
                    game_state.load_pattern("degree")
                if joystick.get_button(button_b):
                    game_state.last_push("button b !")
                    game_state.load_pattern("dur")
                if joystick.get_button(button_x):
                    game_state.last_push("button x !")
                    game_state.load_pattern("sus")
                if joystick.get_button(button_y):
                    game_state.last_push("button y !")
                    game_state.load_pattern("oct")
                if joystick.get_button(button_RB):
                    game_state.last_push("button RB !")
                if joystick.get_button(button_LB):
                    game_state.last_push("button LB !")
                if joystick.get_button(button_start):
                    game_state.last_push("button start !")
                    game_state.pause_music()
                if joystick.get_button(button_back):
                    game_state.last_push("button back !")
                    if game_state.paused:
                        game_state=GameState()
                        game_state.clock.clear()
                        game_state.update_players()
                    game_state.play_text_once("roooommm")
            elif event.type == pygame.JOYAXISMOTION:
                if toggle_axis(joy_left_h):
                    if toggle_axis_dict[joy_left_h] == 1:
                        game_state.last_push("joyL right !")
                    elif toggle_axis_dict[joy_left_h] == -1:
                        game_state.last_push("joyL left !")
                if toggle_axis(joy_left_v):
                    if toggle_axis_dict[joy_left_v] == 1:
                        game_state.last_push("joyL down !")
                    elif toggle_axis_dict[joy_left_v] == -1:
                        game_state.last_push("joyL up !")
                        game_state.update_players()
                if toggle_axis(joy_right_h):
                    if toggle_axis_dict[joy_right_h] == 1:
                        game_state.last_push("joyR right !")
                        print("player3 selected")
                        game_state.selected_player = game_state.player3
                    elif toggle_axis_dict[joy_right_h] == -1:
                        game_state.last_push("joyR left !")
                        print("player1 selected")
                        game_state.selected_player = game_state.player1
                if toggle_axis(joy_right_v):
                    if toggle_axis_dict[joy_right_v] == 1:
                        game_state.last_push("joyR down !")
                        print("player4 selected")
                        game_state.selected_player = game_state.player4
                    elif toggle_axis_dict[joy_right_v] == -1:
                        game_state.last_push("joyR up !")
                        print("player2 selected")
                        game_state.selected_player = game_state.player2
                if toggle_axis(button_LT):
                    if toggle_axis_dict[button_LT] == 1:
                        game_state.last_push("button LT !")
                        game_state.lt_pushed = True
                    if toggle_axis_dict[button_LT] == -1:
                        game_state.lt_pushed = False
                        print("LT up !!")
                if toggle_axis(button_RT):
                    if toggle_axis_dict[button_RT] == 1:
                        game_state.toggle_player()
                        game_state.last_push("button RT !")
            elif event.type == pygame.JOYHATMOTION:
                if joystick.get_hat(0) == cross_key_left:
                    game_state.last_push("crosskey_left !")
                    game_state.pos_x = (game_state.pos_x - 1) % game_state.size
                    game_state.move_sound()
                    print(f"pos_x {game_state.pos_x}")
                    game_state.display_pattern()
                if joystick.get_hat(0) == cross_key_up:
                    game_state.last_push("crosskey_up !")
                    game_state.pos_y = (game_state.pos_y + 1) % game_state.size
                    game_state.move_sound()
                    print(f"pos_y {game_state.pos_y}")
                    game_state.display_pattern()
                if joystick.get_hat(0) == cross_key_right:
                    game_state.last_push("crosskey_right !")
                    game_state.pos_x = (game_state.pos_x + 1) % game_state.size
                    game_state.move_sound()
                    print(f"pos_x {game_state.pos_x}")
                    game_state.display_pattern()
                if joystick.get_hat(0) == cross_key_down:
                    game_state.last_push("crosskey_down !")
                    game_state.pos_y = (game_state.pos_y - 1) % game_state.size
                    game_state.move_sound()
                    print(f"pos_y {game_state.pos_y}")
                    game_state.display_pattern()
            elif event.type == pygame.QUIT:
                running = False
        # except:
        #     game_state = GameState()
        #     game_state.clock.clear()
        #     game_state.update_players()
        #     print("Error catched")
