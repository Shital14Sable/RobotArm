#!/usr/bin/python3
# coding=utf8

from Segmentation import Segmentation
from ArmIK.ArmMoveIK import *
import time
import numpy as np
import pickle
import HiwonderSDK.Board as Board



class Letters:
    def __init__(self, width, ratio, segments):
#         self.AK = ArmIK()
        self.servo1 = 500
        self.segments = segments
        self.width = width
        self.height = width * ratio
        self.seg1 = Segmentation(self.segments)
        
    def letter_H(self, start_point):
        set_pts = []
        #result1 = AK.setPitchRangeMoving(start_point, -90, -90, 0, 100)
        #time.sleep(1)
        set_pts.append(list(start_point))
        end_pt1 = (start_point[0], start_point[1] - self.height, start_point[2])
        point_list1 = self.seg1.straight_line(start_point, end_pt1)
        set_pts.extend(point_list1)
        #AK.setPitchRangeMoving((end_pt1[0], end_pt1[1], end_pt[2]+5), -90, -90, 0, 100)
        #time.sleep(0.5)
        #AK.setPitchRangeMoving((end_pt1[0], end_pt1[1], end_pt[2]+5), -90, -90, 0, 100)
        end_pt2 = (end_pt1[0], end_pt1[1] + self.height/2, end_pt1[2])
        set_pts.append(list(end_pt2))
#         self.AK.setPitchRangeMoving(end_pt2, -90, -90, 0, 100)
        
        end_pt3 = (end_pt2[0] - self.width, end_pt2[1], end_pt2[2])
        point_list2 = self.seg1.straight_line(end_pt2, end_pt3)
        set_pts.extend(point_list2)
        
        end_pt4 = (end_pt3[0], end_pt3[1] - self.height/2, end_pt3[2])
        set_pts.append(list(end_pt4))
#         self.AK.setPitchRangeMoving(end_pt4, -90, -90, 0, 100)
        
        end_pt5 = (end_pt4[0], end_pt4[1] + self.height, end_pt4[2])
        point_list3 = self.seg1.straight_line(end_pt4, end_pt5)
        set_pts.extend(point_list3)
        return np.asarray(set_pts)

    def letter_B(self, start_point):
        set_pts = []
        #result1 = self.AK.setPitchRangeMoving(start_point, -90, -90, 0, 100)
        #time.sleep(1)
        set_pts.append(list(start_point))
        
        end_pt1 = (start_point[0], start_point[1] - self.height, start_point[2])
        point_list1 = self.seg1.straight_line(start_point, end_pt1)
        set_pts.extend(point_list1)
        
        end_pt2 = (end_pt1[0] - self.width, end_pt1[1], end_pt1[2])
        point_list2 = self.seg1.straight_line(end_pt1, end_pt2)
        set_pts.extend(point_list2)
        
        end_pt3 = (end_pt2[0], end_pt2[1] + self.height/2, end_pt2[2])
        point_list3 = self.seg1.straight_line(end_pt2, end_pt3)
        set_pts.extend(point_list3)
        
        end_pt4 = (end_pt3[0] + self.width, end_pt3[1], end_pt3[2])
        point_list4 = self.seg1.straight_line(end_pt3, end_pt4)
        set_pts.extend(point_list4)
        
        # self.AK.setPitchRangeMoving(end_pt3, -90, -90, 0, 100)
        # time.sleep(0.5)
        set_pts.append(list(end_pt3))
        
        end_pt5 = (end_pt3[0], end_pt3[1] + self.height/2, end_pt3[2])
        point_list5 = self.seg1.straight_line(end_pt3, end_pt5)
        set_pts.extend(list(point_list5))
        
        point_list6 = self.seg1.straight_line(end_pt5,start_point)
        set_pts.extend(list(point_list6))
        
        return np.asarray(set_pts)

    def letter_A(self, start_point):
        set_pts = []
#         result1 = self.AK.setPitchRangeMoving(start_point, -90, -90, 0, 100)
        time.sleep(1)
        set_pts.append(list(start_point))
        
        end_pt1 = (start_point[0]-self.width/2, start_point[1] - self.height, start_point[2]) 
        point_list1 = self.seg1.straight_line(start_point, end_pt1)
        set_pts.extend(point_list1)
        
        end_pt2 = (end_pt1[0] - self.width/2, end_pt1[1]+self.height, end_pt1[2])
        point_list2 = self.seg1.straight_line(end_pt1, end_pt2)
        set_pts.extend(point_list2)
        
        pt_move_up = (end_pt2[0], end_pt2[1], end_pt1[2] + 5)
        #self.AK.setPitchRangeMoving(pt_move_up, -90, -90, 0, 100)
        #time.sleep(1)
        set_pts.append(list(pt_move_up))
        
        start_point2 = (start_point[0] - self.width/4, start_point[1] - self.height/2, end_pt1[2])
        set_pts.append(list(start_point2))
        end_pt3 = (start_point2[0] - self.width/2, start_point2[1], start_point[2])
        point_list3 = self.seg1.straight_line(start_point2, end_pt3)
        set_pts.extend(point_list3)
        
        return np.asarray(set_pts)

    def letter_T(self, start_point):
        set_pts = []
        start_point =  (start_point[0], start_point[1] - self.height, start_point[2])
        set_pts.append(list(start_point))
        end_pt1 = (start_point[0] - self.width, start_point[1], start_point[2])
        point_list1 = self.seg1.straight_line(start_point, end_pt1)
        set_pts.extend(list(point_list1))
        
        start_pt2 = (start_point[0] - self.width/2, start_point[1], start_point[2])
        set_pts.append(list(start_pt2))
        end_pt2 = (start_pt2[0], start_pt2[1] + self.height, start_pt2[2])
        point_list2 = self.seg1.straight_line(start_pt2, end_pt2)
        set_pts.extend(list(point_list2))
        return np.asarray(set_pts)

    def letter_M(self, start_point):
        set_pts = []
        set_pts.append(list(start_point))
        
        
        end_pt1 = (start_point[0], start_point[1]-self.height, start_point[2])
        point_list1 = self.seg1.straight_line(start_point, end_pt1)
        set_pts.extend(point_list1)
        
        start_pt2 = end_pt1
        end_pt2 = (start_point[0] - self.width/2, start_point[1] - self.height/2, start_point[2])
        point_list2 = self.seg1.straight_line(start_pt2, end_pt2)
        set_pts.extend(point_list2)
        
        start_pt3 = end_pt2
        end_pt3 = (start_point[0] - self.width, start_point[1] - self.height, start_point[2])
        point_list3 = self.seg1.straight_line(start_pt3, end_pt3)
        set_pts.extend(point_list3)
        
        start_pt4 = end_pt3
        end_pt4 = (start_point[0] - self.width, start_point[1], start_point[2])
        point_list4 = self.seg1.straight_line(start_pt4, end_pt4)
        set_pts.extend(point_list4)
        return np.asarray(set_pts)
        
    def letter_O(self, start_point):
        set_pts = []
        set_pts.append(list(start_point))
        z = start_point[2]

        end_pt1 = (start_point[0], start_point[1] - self.height, z)
        end_pt2 = (end_pt1[0] - self.width, end_pt1[1], z)
        end_pt3 = (end_pt2[0],  end_pt2[1] + self.height, z)

        line1 = self.seg1.straight_line(start_point, end_pt1)
        set_pts.extend(list(line1))

        line2 = self.seg1.straight_line(end_pt1, end_pt2)
        set_pts.extend(list(line2))

        line3 = self.seg1.straight_line(end_pt2, end_pt3)
        set_pts.extend(list(line3))

        line4 = self.seg1.straight_line(end_pt3, start_point)
        set_pts.extend(list(line4))

        return np.asarray(set_pts)

    def letter_R(self, start_point):
        set_pts = []
        set_pts.append(list(start_point))
        z = start_point[2]

        end_pt1 = (start_point[0], start_point[1] - self.height, z)
        end_pt2 = (end_pt1[0] - self.width, end_pt1[1], z)
        end_pt3 = (end_pt2[0],  end_pt2[1] + self.height/2, z)
        end_pt4 = (end_pt3[0] + self.width, end_pt3[1], z)
        end_pt5 = (end_pt4[0] - self.width, end_pt4[1] + self.height/2, z)

        line1 = self.seg1.straight_line(start_point, end_pt1)
        set_pts.extend(list(line1))

        line2 = self.seg1.straight_line(end_pt1, end_pt2)
        set_pts.extend(list(line2))

        line3 = self.seg1.straight_line(end_pt2, end_pt3)
        set_pts.extend(list(line3))

        line4 = self.seg1.straight_line(end_pt3, end_pt4)
        set_pts.extend(list(line4))

        line5 = self.seg1.straight_line(end_pt4, end_pt5)
        set_pts.extend(list(line5))

        return np.asarray(set_pts)
# 
#     def reset(self, start_cords = (0, 20, 10)):
#         # move
#         self.AK.setPitchRangeMoving(start_cords, -90, -90, 0, 100)
#         # delay
#         time.sleep(1)
#         
#     def gripper_open(self):    
#         Board.setBusServoPulse(1, self.servo1 - 200, 500)  # Open the paws and put down $
#         time.sleep(3)
#         
#     def gripper_close(self):
#         Board.setBusServoPulse(1, self.servo1, 100)  # Holder closed
#         time.sleep(1)

        
if __name__ == '__main__':
    run_letters = Letters(3, 1.67, 5)
    set_pts_H = run_letters.letter_H((0, 20, 8))
    set_pts_A = run_letters.letter_A((0, 20, 8))
    set_pts_R = run_letters.letter_R((0, 20, 8))
    set_pts_B = run_letters.letter_B((0, 20, 8))
    set_pts_T = run_letters.letter_T((0, 20, 8))
    set_pts_M = run_letters.letter_M((0, 20, 8))
    set_pts_O = run_letters.letter_O((0, 20, 8)) 
#     run_letters.reset()
#     run_letters.gripper_open()
#     run_letters.gripper_close()
    AK = ArmIK()
#     
#     for i in range(len(set_pts_H)):
#         AK.setPitchRangeMoving(tuple(set_pts_H[i]), -90, -90, 0, 300)
#         time.sleep(0.4)
     
    np.save("Letters/letter_H", set_pts_H)
    np.save("Letters/letter_A", set_pts_A)
    np.save("Letters/letter_R", set_pts_R)
    np.save("Letters/letter_B", set_pts_B)
    np.save("Letters/letter_T", set_pts_T)
    np.save("Letters/letter_M", set_pts_M)
    np.save("Letters/letter_O", set_pts_O)

    