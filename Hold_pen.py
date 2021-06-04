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
    Board.setBusServoPulse(1, servo1 - 200, 500)  # Open the paws and put down $
    time.sleep(2)
    Board.setBusServoPulse(1, servo1, 00)  # Holder closed
    time.sleep(1)