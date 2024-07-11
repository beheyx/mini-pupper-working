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

    def default():
        print("Executing default gesture")
        # Starting leg positions
        initial_position = [512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512]
        esp32.servos_set_position(initial_position)
        print("Default leg positions set to:", initial_position)

    def sit():
        print("Executing sit gesture")
        leg_bend = 53
        right_back_leg = 512
        left_back_leg = 512

        for i in range(4):
            right_back_leg -= leg_bend
            left_back_leg += leg_bend
            leg_positions = [512, 512, 512, 512, 512, 512, 512, 512, right_back_leg, 512, 512, left_back_leg]
            print(f"Setting leg positions (iteration {i}): {leg_positions}")
            esp32.servos_set_position(leg_positions)
            time.sleep(0.05)

        print("Sit gesture completed")

    def lie_down():
        print("Executing lie down gesture")
        leg_bend = 53
        right_back_leg = 512
        left_back_leg = 512

        for i in range(4):
            right_back_leg -= leg_bend
            left_back_leg += leg_bend
            leg_positions = [512, 512, right_back_leg, 512, 512, left_back_leg, 512, 512, right_back_leg, 512, 512, left_back_leg]
            print(f"Setting leg positions (iteration {i}): {leg_positions}")
            esp32.servos_set_position(leg_positions)
            time.sleep(0.1)

        print("Lie down gesture completed")

    def bow():
        print("Executing bow gesture")
        leg_bend = 30
        right_front_leg = 512
        left_front_leg = 512

        for i in range(4):
            right_front_leg -= leg_bend
            left_front_leg += leg_bend
            leg_positions = [512, 512, right_front_leg, 512, 512, left_front_leg, 512, 512, 512, 512, 512, 512]
            print(f"Setting leg positions (iteration {i}): {leg_positions}")
            esp32.servos_set_position(leg_positions)
            time.sleep(0.05)

        print("bow gesture completed")

    # Because front leg is broken, we test it with back leg
    # For head_shake, just change the leg_positions to [462, 512, 512, 462, 512, 512, 512, 512, 512, 512, 512, 512]
    def back_shake():  
        print("Executing head shake gesture")
        
        for i in range(8):
            leg_positions = [512, 512, 512, 512, 512, 512, 512, 512, 480, 512, 512, 544]
            print(f"Setting leg positions (iteration {i}): {leg_positions}")
            esp32.servos_set_position(leg_positions)
            time.sleep(0.1)  # Increased delay to 1 second

            leg_positions = [512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512]
            print(f"Setting leg positions (iteration {i}): {leg_positions}")
            esp32.servos_set_position(leg_positions)
            time.sleep(0.1)  # Increased delay to 1 second

        print("Head shake gesture completed")
        leg_positions = [512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512]
        esp32.servos_set_position(leg_positions)


    def excited():
        print("Executing excited gesture")

        for i in range(8):
            leg_positions = [470, 512, 512, 470, 512, 512, 554, 512, 512, 554, 512, 512]
            print(f"Setting leg positions (iteration {i}): {leg_positions}")
            esp32.servos_set_position(leg_positions)
            time.sleep(0.05)  # Increased delay to 1 second

            leg_positions = [512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512]
            print(f"Setting leg positions (iteration {i}): {leg_positions}")
            esp32.servos_set_position(leg_positions)
            time.sleep(0.05)  # Increased delay to 1 second

            leg_positions = [554, 512, 512, 554, 512, 512, 470, 512, 512, 470, 512, 512]
            print(f"Setting leg positions (iteration {i}): {leg_positions}")
            esp32.servos_set_position(leg_positions)
            time.sleep(0.05)  # Increased delay to 1 second

        print("Excited gesture completed")
        leg_positions = [512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512]
        esp32.servos_set_position(leg_positions)


    def paw():
        print("Executing paw gesture")
        Gesture.sit()
        leg_positions = [512, 512, 512, 512, 700, 512, 512, 512, 300, 512, 512, 724]
        esp32.servos_set_position(leg_positions)

        print(f"Setting leg position: {leg_positions}")
        print("Paw gesture completed")


print("Pupper activated")

# Call the default gesture to reset to known state
Gesture.default()
time.sleep(3)

# Call the sit gesture
#Gesture.sit()
#time.sleep(3)

#Gesture.bow()
#time.sleep(3)

#Gesture.default()
#time.sleep(1)
#Gesture.back_shake()

# Call lie down gesture
#Gesture.default()
#time.sleep(1)
#Gesture.lie_down()
#time.sleep(3)

# Call excited gesture
#Gesture.default()
#time.sleep(1)
#Gesture.excited()
#time.sleep(3)

# Call paw gesture
Gesture.default()
time.sleep(1)
Gesture.paw()
#time.sleep(3)

# Back to default
Gesture.default()
