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
    def __init__(self, segments=10):
        self.AK = ArmIK()
        self.servo1 = 500
        self.segments = segments
    
    def code_initialize(self):
        Board.setBusServoPulse(1, self.servo1 - 200, 500)  # Open the paws and put down $
        time.sleep(2)
        Board.setBusServoPulse(1, self.servo1, 600)  # Holder closed
        time.sleep(1)

    def straight_line(self, point1, point2):
        zp = point1[2]
        plt_pts = []
        for i in range(self.segments):
            xp = point1[0] + (1/(self.segments-i))*(point2[0]-point1[0])
            yp = point1[1] + (1/(self.segments-i))*(point2[1]-point1[1])
            #result2 = self.AK.setPitchRangeMoving((xp, yp, zp), -90, -90, 0, 100)
            #time.sleep(0.5)
            point1 = (xp, yp, zp)
            plt_pts.append(list(point1))
        return plt_pts
    
            
    
    def small_sem_cir(self, point1, point2, cir_dir=1):
        zp = point1[2]
        cir_rad = np.linalg.norm(np.array(point1)-np.array(point2))/2
        print(cir_rad)
        #cir_center[0] = point1[0] + 0.5*(point2[0]-point1[0])
        #cir_center[1] = point1[1] + 0.5*(point2[1]-point1[1])
        #cir_center[2] = point1[2]
        plt_pts = []
        plt_pts.append(list(point1))
        theta_n = np.pi/self.segments
        #if cir_dir == 1:
        #    cir_dir = -1
        
        for i in range(self.segments):
            xp = cir_rad*cos(cir_dir*theta_n) + point1[0] + 0.5*(point2[0]-point1[0])
            yp = cir_rad*sin(cir_dir*theta_n) + point1[1] + 0.5*(point2[1]-point1[1])
            result2 = self.AK.setPitchRangeMoving((xp, yp, zp), -90, -90, 0, 100)
            time.sleep(0.5)
            point1 = (xp, yp, zp)
            print(point1)
            plt_pts.append(list(point1))
        return plt_pts
    
    def generate_semicircle(self, center_x, center_y, center_z, radius, stepsize=1):
        mid_pt = (center_x + radius + stepsize)
        x = np.arange(center_x, mid_pt, stepsize)
        y = np.sqrt(radius**2 - x**2)
        
        x = np.concatenate([x,x[::-1]])
        y = np.concatenate([y,-y[::-1]])
        for i in range(len(x)):
            print(x[i], y[i])
            result2 = self.AK.setPitchRangeMoving((x[i], y[i], center_z), -90, -90, 0, 100)
            print(i)
            time.sleep(0.5)

        return x, y + center_y 


  #  def big_sem_cir(self, point1, point2, cir_dir):

if __name__ == '__main__':
    seg1 = Segmentation()
    seg1.straight_line((0, 20, 8), (0, 15, 8))

