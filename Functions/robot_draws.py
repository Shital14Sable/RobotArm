#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/pi/ArmPi/')
import cv2
import time
import Camera
from ArmIK.ArmMoveIK import *
import HiwonderSDK.Board as Board
from draw_letter import Draw
import user_input
import gui

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt


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
#             print(new_dict[key][0], row)
            # move
            result = AK.setPitchRangeMoving(tuple(row), -90, -90, -35, 80)
            if result == False:
                print(result)
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
    app = QApplication([])

    interface = gui.GUI()

    interface.show()

    app.exec_()

    word_to_draw = interface.save_text #user_input.take_user_input()
    workspace_limits = [interface.ws_point1,  interface.ws_point2]
    letter_bounding_box = (interface.font_width, interface.font_len_wid_ratio, (0, 20, 8))
    gap_btw_letters = interface.gap
    distance_from_boundaries = (interface.start_right, interface.start_up)
    
    segments = 10

    draw_robot = Draw(word_to_draw, workspace_limits, letter_bounding_box, gap_btw_letters, distance_from_boundaries, segments)

    final_dict = draw_robot.transform_coords_to_start_pos()
#     print("REPAIRED:", final_dict)

 
    
    loop_through_letters(final_dict)
    
    
    
    

