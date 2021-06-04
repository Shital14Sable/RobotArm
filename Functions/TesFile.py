#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/pi/ArmPi/')
import cv2
import time
import Camera
import threading
from LABConfig import *
from ArmIK.Transform import *
from ArmIK.ArmMoveIK import *
import HiwonderSDK.Board as Board
from CameraCalibration.CalibrationConfig import *


if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)

AK = ArmIK()


if __name__ == '__main__':
    AK.setPitchRangeMoving((0, 0 - 2, 5), -90, -90, 0, 20)
    time.sleep(1)
    AK.setPitchRangeMoving((20, 20 - 2, 5), -90, -90, 0, 20)