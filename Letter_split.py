#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/pi/ArmPi/')
import cv2
import time
import Camera
from ArmIK.ArmMoveIK import *
import HiwonderSDK.Board as Board
import numpy as np 

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)




class Segmentation:
    def __init__(self):
        self.AK = ArmIK()
        self.servo1 = 500
    
    def straight_line(self, point1, point2):
        result1 = self.AK.setPitchRangeMoving(point1, -90, -90, 0, 100)
        time.sleep(1)
        zp = point1[2]
        print(zp)
        segments = 10
        for i in range(segments):
            xp = point1[0] + (1/(segments-i))*(point2[0]-point1[0])
            print(xp)
            yp = point1[1] + (1/(segments-i))*(point2[1]-point1[1])
            result2 = self.AK.setPitchRangeMoving((xp, yp, zp), -90, -90, 0, 10$
            time.sleep(0.5)
            point1 = (xp, yp, zp)
        return None

            
    
 #   def small_sem_cir(self, point1, point2, cir_dir):
 #       if 


  #  def big_sem_cir(self, point1, point2, cir_dir):

if __name__ == '__main__':
    seg1 = Segmentation()
    seg1.straight_line((0, 20, 8), (10, 20, 8))