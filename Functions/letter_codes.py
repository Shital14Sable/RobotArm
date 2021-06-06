#!/usr/bin/python3
# coding=utf8

from Segmentation import Segmentation
from ArmIK.ArmMoveIK import *
import time
import numpy as np
import pickle
import HiwonderSDK.Board as Board

AK = ArmIK()
seg1 = Segmentation()
# The angle at which the gripper is closed when gripping
servo1 = 500


def letter_H(start_point, height=5.8, width=3.5):
    set_pts = []
    #result1 = AK.setPitchRangeMoving(start_point, -90, -90, 0, 100)
    #time.sleep(1)
    set_pts.append(list(start_point))
    end_pt1 = (start_point[0], start_point[1] - height, start_point[2])
    point_list1 = seg1.straight_line(start_point, end_pt1)
    set_pts.extend(point_list1)
    #AK.setPitchRangeMoving((end_pt1[0], end_pt1[1], end_pt[2]+5), -90, -90, 0, 100)
    #time.sleep(0.5)
    #AK.setPitchRangeMoving((end_pt1[0], end_pt1[1], end_pt[2]+5), -90, -90, 0, 100)
    end_pt2 = (end_pt1[0], end_pt1[1] + height/2, end_pt1[2])
    set_pts.append(list(end_pt2))
    AK.setPitchRangeMoving(end_pt2, -90, -90, 0, 100)
    
    end_pt3 = (end_pt2[0] - width, end_pt2[1], end_pt2[2])
    point_list2 = seg1.straight_line(end_pt2, end_pt3)
    set_pts.extend(point_list2)
    
    end_pt4 = (end_pt3[0], end_pt3[1] - height/2, end_pt3[2])
    set_pts.append(list(end_pt4))
    AK.setPitchRangeMoving(end_pt4, -90, -90, 0, 100)
    
    end_pt5 = (end_pt4[0], end_pt4[1] + height, end_pt4[2])
    point_list3 = seg1.straight_line(end_pt4, end_pt5)
    set_pts.extend(point_list3)
    return np.asarray(set_pts)

def letter_B(start_point, height=5.8, width=3.5):
    set_pts = []
    #result1 = AK.setPitchRangeMoving(start_point, -90, -90, 0, 100)
    #time.sleep(1)
    set_pts.append(list(start_point))
    
    end_pt1 = (start_point[0], start_point[1] - height, start_point[2])
    point_list1 = seg1.straight_line(start_point, end_pt1)
    set_pts.extend(point_list1)
    
    end_pt2 = (end_pt1[0] - width, end_pt1[1], end_pt1[2])
    point_list2 = seg1.straight_line(end_pt1, end_pt2)
    set_pts.extend(point_list2)
    
    end_pt3 = (end_pt2[0], end_pt2[1] + height/2, end_pt2[2])
    point_list3 = seg1.straight_line(end_pt2, end_pt3)
    set_pts.extend(point_list3)
    
    end_pt4 = (end_pt3[0] + width, end_pt3[1], end_pt3[2])
    point_list4 = seg1.straight_line(end_pt3, end_pt4)
    set_pts.extend(point_list4)
    
    # AK.setPitchRangeMoving(end_pt3, -90, -90, 0, 100)
    # time.sleep(0.5)
    set_pts.append(list(end_pt3))
    
    end_pt5 = (end_pt3[0], end_pt3[1] + height/2, end_pt3[2])
    point_list5 = seg1.straight_line(end_pt3, end_pt5)
    set_pts.extend(list(point_list5))
    
    point_list6 = seg1.straight_line(end_pt5,start_point)
    set_pts.extend(list(point_list6))
    
    return np.asarray(set_pts)

def letter_A(start_point, height=5.8, width=3.5):
    set_pts = []
    result1 = AK.setPitchRangeMoving(start_point, -90, -90, 0, 100)
    time.sleep(1)
    set_pts.append(list(start_point))
    
    end_pt1 = (start_point[0]-width/2, start_point[1] - height, start_point[2]) 
    point_list1 = seg1.straight_line(start_point, end_pt1)
    set_pts.extend(point_list1)
    
    end_pt2 = (end_pt1[0] - width/2, end_pt1[1]+height, end_pt1[2])
    point_list2 = seg1.straight_line(end_pt1, end_pt2)
    set_pts.extend(point_list2)
    
    pt_move_up = (end_pt2[0], end_pt2[1], end_pt1[2] + 5)
    #AK.setPitchRangeMoving(pt_move_up, -90, -90, 0, 100)
    #time.sleep(1)
    set_pts.append(list(pt_move_up))
    
    start_point2 = (start_point[0] - width/4, start_point[1] - height/2, end_pt1[2])
    set_pts.append(list(start_point2))
    end_pt3 = (start_point2[0] - width/2, start_point2[1], start_point[2])
    point_list3 = seg1.straight_line(start_point2, end_pt3)
    set_pts.extend(point_list3)
    
    return np.asarray(set_pts)

def letter_T(start_point, height=5.8, width=3.5):
    set_pts = []
    start_point =  (start_point[0], start_point[1] - height, start_point[2])
    set_pts.append(list(start_point))
    end_pt1 = (start_point[0] - width, start_point[1], start_point[2])
    point_list1 = seg1.straight_line(start_point, end_pt1)
    set_pts.extend(list(point_list1))
    
    start_pt2 = (start_point[0] - width/2, start_point[1], start_point[2])
    end_pt2 = (start_pt2[0], start_pt2[1] + height, start_pt2[2])
    point_list2 = seg1.straight_line(start_pt2, end_pt2)
    set_pts.extend(list(point_list2))
    return np.asarray(set_pts)

def letter_M(start_point, height=5.8, width=3.5):
    set_pts = []
    set_pts.append(list(start_point))
    
    
    end_pt1 = (start_point[0], start_point[1]-height, start_point[2])
    point_list1 = seg1.straight_line(start_point, end_pt1)
    set_pts.extend(point_list1)
    
    start_pt2 = end_pt1
    end_pt2 = (start_point[0] + width/2, start_point[1], start_point[2])
    point_list2 = seg1.straight_line(start_pt2, end_pt2)
    set_pts.extend(point_list2)
    
    start_pt3 = end_pt2
    end_pt3 = (start_point[0] + width, start_point[1] - height, start_point[2])
    point_list3 = seg1.straight_line(start_pt3, end_pt3)
    set_pts.extend(point_list3)
    
    start_pt4 = end_pt3
    end_pt4 = (start_point[0] + width, start_point[1], start_point[2])
    point_list4 = seg1.straight_line(start_pt4, end_pt4)
    set_pts.extend(point_list4)
    return np.asarray(set_pts)
    
def letter_O(start_point, height, width):
    seg_o = Segmentation()
    set_pts = []
    set_pts.append(list(start_point))
    z = start_point[2]

    end_pt1 = (start_point[0], start_point[1] - height, z)
    end_pt2 = (end_pt1[0] - width, end_pt1[1], z)
    end_pt3 = (end_pt2[0],  end_pt2[1] + height, z)

    line1 = seg_o.straight_line(start_point, end_pt1)
    set_pts.extend(list(line1))

    line2 = seg_o.straight_line(end_pt1, end_pt2)
    set_pts.extend(list(line2))

    line3 = seg_o.straight_line(end_pt2, end_pt3)
    set_pts.extend(list(line3))

    line4 = seg_o.straight_line(end_pt3, start_point)
    set_pts.extend(list(line4))

    return np.asarray(set_pts)

def letter_R(start_point, height, width):
    seg_r = Segmentation()
    set_pts = []
    set_pts.append(list(start_point))
    z = start_point[2]

    end_pt1 = (start_point[0], start_point[1] - height, z)
    end_pt2 = (end_pt1[0] - width, end_pt1[1], z)
    end_pt3 = (end_pt2[0],  end_pt2[1] + height/2, z)
    end_pt4 = (end_pt3[0] + width, end_pt3[1], z)
    end_pt5 = (end_pt4[0] - width, end_pt4[1] + height/2, z)

    line1 = seg_r.straight_line(start_point, end_pt1)
    set_pts.extend(list(line1))

    line2 = seg_r.straight_line(end_pt1, end_pt2)
    set_pts.extend(list(line2))

    line3 = seg_r.straight_line(end_pt2, end_pt3)
    set_pts.extend(list(line3))

    line4 = seg_r.straight_line(end_pt3, end_pt4)
    set_pts.extend(list(line4))

    line5 = seg_r.straight_line(end_pt4, end_pt5)
    set_pts.extend(list(line5))

    return np.asarray(set_pts)

def reset(start_cords = (0, 20, 10)):
    # move
    AK.setPitchRangeMoving(start_cords, -90, -90, 0, 100)
    # delay
    time.sleep(1)
    
def gripper_open():    
    Board.setBusServoPulse(1, servo1 - 200, 500)  # Open the paws and put down $
    time.sleep(3)
    
def gripper_close():
    Board.setBusServoPulse(1, servo1, 00)  # Holder closed
    time.sleep(1)

    
if __name__ == '__main__':
    height = 5.8
    width = 3.5
    set_pts_H = letter_A((0, 20, 8), height, width)
    reset()
    gripper_open()
    gripper_close()
    
    for i in range(len(set_pts_H)):
        AK.setPitchRangeMoving(tuple(set_pts_H[i]), -90, -90, 0, 100)
        time.sleep(0.4)
    
#     #set_pts_A = letter_A((0, 20, 8), height, width)
#     set_pts_R = letter_R((0, 20, 8), height, width)
#     set_pts_B = letter_B((0, 20, 8), height, width)
#     set_pts_T = letter_T((0, 20, 8), height, width)
#     set_pts_M = letter_M((0, 20, 8), height, width)
#     set_pts_O = letter_O((0, 20, 8), height, width) 
    #letter_files = {"H": str(set_pts_H),  "A": str(set_pts_A), "R": str(set_pts_R), "B": str(set_pts_B), "T": str(set_pts_T), "M": str(set_pts_M), "O": str(set_pts_O)}
    #with open("letter_data.pkl", "w") as a_file:
    #    pickle.dump(letter_files, a_file)
#     # a_file.close()
#     np.save("letter_H", set_pts_H)
#     np.save("letter_A", set_pts_A)
#     np.save("letter_R", set_pts_R)
#     np.save("letter_B", set_pts_B)
#     np.save("letter_T", set_pts_T)
#     np.save("letter_M", set_pts_M)
#     np.save("letter_O", set_pts_O)

    