#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/pi/ArmPi/')
import cv2
import time
import Camera
from ArmIK.ArmMoveIK import *
import HiwonderSDK.Board as Board

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)

AK = ArmIK()
# The angle at which the gripper is closed when gripping
servo1 = 500

if __name__ == '__main__':
    my_camera = Camera.Camera()
    my_camera.camera_open()
    Board.setBusServoPulse(1, servo1 - 200, 500)  # Open the paws and put down the object
    time.sleep(2)
    Board.setBusServoPulse(1, servo1, 00)  # Holder closed
    time.sleep(1)
    result1 = AK.setPitchRangeMoving((-15, 28, 10), -90, -90, 0, 1000)
    print(result1)
    time.sleep(2)
    result2 = AK.setPitchRangeMoving((15, 28, 10), -90, -90, 0, 1000)
    print(result2)
    time.sleep(2)
    result3 = AK.setPitchRangeMoving((15, 12, 10), -90, -90, 0, 1000)
    print(result3)
    time.sleep(2)
    result4 = AK.setPitchRangeMoving((-15, 12, 10), -90, -90, 0, 1000)
    print(result4)
    time.sleep(2)
