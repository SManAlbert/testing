#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2019, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

"""
Description: Record trajectory
    1. requires firmware 1.2.0 and above support
"""

import threading as th
import os
import sys
import time
import keyboard
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI


#######################################################
"""
Just for test example
"""
if len(sys.argv) >= 2:
    ip = sys.argv[1]
else:
    try:
        from configparser import ConfigParser
        parser = ConfigParser()
        parser.read('../robot.conf')
        ip = parser.get('xArm', 'ip')
    except:
        ip = input('Please input the xArm ip address:')
        if not ip:
            print('input error, exit')
            sys.exit(1)
########################################################


arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

speed = 60

while True:
    arm.set_position(x=178, y=-13.5, z=160, roll=180, pitch=0, yaw=0, speed=100, is_radian=False, wait=True)
    time.sleep(5)

    arm.set_servo_angle(angle=[30, -45, 0, 0, -45, 0], speed=10, wait=True)
    print(arm.get_position())

    time.sleep(2)

    arm.set_tool_position(x=0, y=100, z=0, roll=0, pitch=0, yaw=0, speed=speed, wait=True)

    time.sleep(2)
    arm.set_tool_position(x=-60, y=0, z=0, roll=0, pitch=0, yaw=0, speed=speed, wait=True)

    time.sleep(2)
    arm.set_tool_position(x=0, y=0, z=300, roll=0, pitch=0, yaw=0, speed=speed, wait=True)

    time.sleep(5)

    #reset
    arm.set_tool_position(x=0, y=0, z=-300, roll=0, pitch=0, yaw=0, speed=speed, wait=True)
    print(arm.get_servo_angle(), arm.get_servo_angle(is_radian=True))
    # Analog recording process, here with delay instead


arm.disconnect()

