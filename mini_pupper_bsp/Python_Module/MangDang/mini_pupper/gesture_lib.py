#from UDPComms import Publisher
#import pygame
#import netifaces as ni
#from PIL import Image, ImageDraw, ImageFont
#from enum import Enum
#from MangDang.LCD.ST7789 import ST7789
#import sounddevice as sd
#import soundfile as sf
import time
#import os
#from display import Display
#from display import BehaviorState
import helper_movement
#from mini_pupper_bsp.Python_Module.MangDang.mini_pupper.helper_movement import *
#import RPi.GPIO as GPIO
from MangDang.mini_pupper.ESP32Interface import ESP32Interface

esp32 = ESP32Interface()
wait_time = 500
#MESSAGE_RATE = 20
counter_a = 0

class Gesture:

    #gesture 1 stand
    def default():
        global counter_a

        #starting leg positions
        initial_position = [512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512]  
        esp32.servos_set_position(initial_position)

        msg,counter_a = helper_movement.toggle_activation(counter_a)
        helper_movement.pub_msg(msg, wait_time)

    #gesture 2 sit
    def sit():
        global counter_a
        leg_bend = 53
        right_back_leg = 512
        left_back_leg = 512

        for _ in range (4):
            right_back_leg -= leg_bend
            left_back_leg += leg_bend
            leg_positions = [512, 512, 512, 512, 512, 512, 512, 512, right_back_leg, 512, 512, left_back_leg]
            esp32.servos_set_position(leg_positions)
            time.sleep(0.1)

        msg,counter_a = helper_movement.toggle_activation(counter_a)
        helper_movement.pub_msg(msg, wait_time)

    #gesture 2 give me paw: sit down first, then extend front-left leg outward
    def paw():
        global counter_a

        Gesture.default()  
        Gesture.sit()

        #leg_positions = [512, 512, 512, 512, 512, 512, 512, 512, 300, 512, 512, 724]  #change the value that is related t o FL
        #esp32.servos_set_position(leg_positions)

        msg,counter_a = helper_movement.toggle_activation(counter_a)
        helper_movement.pub_msg(msg, wait_time)


Gesture.default()
Gesture.sit()
Gesture.paw()