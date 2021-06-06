#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/pi/ArmPi/')
import cv2
import time
import Camera
from ArmIK.ArmMoveIK import *
import HiwonderSDK.Board as Board
from draw_letters import Draw
import user_input


if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)

AK = ArmIK()
# The angle at which the gripper is closed when gripping
servo1 = 500

def loop_through_letters(new_dict):
    """
    This function will loop through the coordinates and move the robot accordingly
    :@param: new_dict: Dictionary of the form {letter_index: ['letter', (startx, starty), nparray(starting_coords)}
    :@return: complete: True (if completed properly) False otherwise
    """
    
    reset()
    gripper_open()
    gripper_close()
    for key in new_dict.keys():
        letter_start_pt = new_dict[key][2][0]
        print(letter_start_pt)
        reset((letter_start_pt[0], letter_start_pt[1], letter_start_pt[2]+4))
        for row in new_dict[key][2]:  
            print(new_dict[key][0], row)
            # move
            AK.setPitchRangeMoving(tuple(row), -90, -90, 0, 100)
            # delay
            time.sleep(0.2)
        #delay
        AK.setPitchRangeMoving((row[0], row[1], 10), -90, -90, 0, 100)
        time.sleep(1)
    reset()
    gripper_open()
    
def reset(start_cords = (0, 20, 10)):
    # move
    AK.setPitchRangeMoving(start_cords, -90, -90, 0, 100)
    # delay
    time.sleep(0.5)
    
def gripper_open():    
    Board.setBusServoPulse(1, servo1 - 200, 500)  # Open the paws and put down $
    time.sleep(2)
    
def gripper_close():
    Board.setBusServoPulse(1, servo1, 00)  # Holder closed
    time.sleep(1)    

if __name__ == '__main__':
    word_to_draw = user_input.take_user_input()
    workspace_limits = [(-15, 12), (15, 28)]
    letter_bounding_box = (3.5, 1.6571, (0, 20, 8))
    gap_btw_letters = 1
    distance_from_boundaries = (4, 5)

    draw_robot = Draw(word_to_draw, workspace_limits, letter_bounding_box, gap_btw_letters, distance_from_boundaries)

    final_dict = draw_robot.transform_coords_to_start_pos()
#     print("REPAIRED:", final_dict)

 
    
    loop_through_letters(final_dict)
    
    
    
    

