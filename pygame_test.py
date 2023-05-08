import pygame
import os

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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(button_a):
                    print("button a !")
                if joystick.get_button(button_b):
                    print("button b !")
                if joystick.get_button(button_x):
                    print("button x !")
                if joystick.get_button(button_y):
                    print("button y !")
                if joystick.get_button(button_RB):
                    print("button RB !")
                if joystick.get_button(button_LB):
                    print("button LB !")
                if joystick.get_button(button_start):
                    print("button start !")
                if joystick.get_button(button_back):
                    print("button back !")
        elif event.type == pygame.JOYAXISMOTION:
                if toggle_axis(joy_left_h):
                    if toggle_axis_dict[joy_left_h] == 1:
                        print("joyL right !")
                    elif toggle_axis_dict[joy_left_h] == -1:
                        print("joyL left !")
                if toggle_axis(joy_left_v):
                    if toggle_axis_dict[joy_left_v] == 1:
                        print("joyL down !")
                    elif toggle_axis_dict[joy_left_v] == -1:
                        print("joyL up !")
                if toggle_axis(joy_right_h):
                    if toggle_axis_dict[joy_right_h] == 1:
                        print("joyR right !")
                    elif toggle_axis_dict[joy_right_h] == -1:
                        print("joyR left !")
                if toggle_axis(joy_right_v):
                    if toggle_axis_dict[joy_right_v] == 1:
                        print("joyR down !")
                    elif toggle_axis_dict[joy_right_v] == -1:
                        print("joyR up !")
                if toggle_axis(button_LT):
                    if toggle_axis_dict[button_LT] == 1:
                        print("button LT !")
                if toggle_axis(button_RT):
                    if toggle_axis_dict[button_RT] == 1:
                        print("button RT !")
        elif event.type == pygame.JOYHATMOTION:
                if joystick.get_hat(0) == cross_key_down:
                    print("crosskey_down !")
                if joystick.get_hat(0) == cross_key_up:
                    print("crosskey_up !")
                if joystick.get_hat(0) == cross_key_left:
                    print("crosskey_left !")
                if joystick.get_hat(0) == cross_key_right:
                    print("crosskey_right !")
        elif event.type == pygame.QUIT:
            running = False
