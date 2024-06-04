from UDPComms import Publisher
import pygame
import netifaces as ni
from PIL import Image, ImageDraw, ImageFont, ImageOps
from enum import Enum
from MangDang.LCD.ST7789 import ST7789
import sounddevice as sd
import soundfile as sf
import time
import os

# Audio record parameters
fs = 48000  # 48KHz, Audio sampling rate
duration = 5  # Recording duration in seconds
#filename = 'bibi1.wav'
# Extract data and sampling rate from file
#data, fs = sf.read(filename, dtype='float32')
# Set the default speaker volume to maximum
# Headphone number is 0 without HDMI output
# Headphone number is 1 when HDMI connect the display
os.system("amixer -c 0 sset 'Headphone' 100%")

def direction_helper(trigger, opt1, opt2):
    if trigger == opt1:
        return -1
    if trigger == opt2:
        return 1
    return 0

class BehaviorState(Enum):
    DEACTIVATED = -1
    REST = 0
    TROT = 1
    HOP = 2
    FINISHHOP = 3
    SHUTDOWN = 96
    IP = 97
    TEST = 98
    LOWBATTERY = 99

class Display:

    def __init__(self, image_dir='/var/lib/mini_pupper_bsp'):
        self.image_dir = image_dir
        self.disp = ST7789()
        self.disp.begin()
        self.thread = None
        self.current_state = None

    def state_to_image(self, state):
        path = "%s.png" % state.name
        return path.lower()

    def show_state(self, state):
        if state.name == self.current_state:
            return
        self.current_state = state.name
        image_path = "%s/%s" % (self.image_dir, self.state_to_image(state))
        image = Image.open(image_path)
        self.disp.display(image)

    def show_image(self, image_path):
        image = Image.open(image_path)
        im2 = ImageOps.fit(image, (320,240),method=0,bleed = 0.0, centering = (0.5,0.5))
        im2.resize((320, 240))
        self.disp.display(im2)
    
    def show_ip(self):
        image_path = "%s/%s" % (self.image_dir, self.state_to_image(BehaviorState.IP))
        image = Image.open(image_path)
        image.resize((320, 240))
        if ni.AF_INET in ni.ifaddresses('wlan0').keys():
            ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
        elif ni.AF_INET in ni.ifaddresses('eth0').keys():
            ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        else:
            ip = 'no IPv4 address found'
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 30)
        draw = ImageDraw.Draw(image)
        text = "IP: %s" % str(ip)
        draw.text((20, 95), text, font=font, fill="#000000", spacing=0, align='left')
        self.disp.display(image)

if __name__ == "__main__":
    pub = Publisher(8830)
    
    pygame.init()
    pygame.display.init()
    MESSAGE_RATE = 20
    win = pygame.display.set_mode((500, 250))
    
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 20)
    text_surface = font.render("Click to enable.", False, (220, 0, 0))
    win.fill((255, 255, 255))
    win.blit(text_surface, (40, 100))
    
    rx_ = 0.0
    ry_ = 0.0
    lx_ = 0.0
    ly_ = 0.0
    l_alpha = 0.15
    r_alpha = 0.3
    
    disp = Display()
    #disp.show_ip()
    disp.show_image('moonphases/moon11.png')
    
    #sd.play(data, fs)
    #sd.wait()  # Wait for playback to finish
    #print("Mini Pupper 2 audio playback end.")
    
    # Your additional code logic can go here.
    pygame.event.pump()

    # msg = {
    #     "ly": 0,
    #     "lx": 0,
    #     "rx": 0,
    #     "ry": 0,
    #     "L2": 0,
    #     "R2": 0,
    #     "R1": 0,
    #     "L1": 0,
    #     "dpady": 0,
    #     "dpadx": 0,
    #     "x": 0,
    #     "square": 0,
    #     "circle": 0,
    #     "triangle": 0,
    #     "message_rate": MESSAGE_RATE,
    # }
    # pub.send(msg)
    # #pygame.display.flip()
    # pygame.time.wait(int(1000/MESSAGE_RATE))
    # pygame.time.wait(500)
    # #if not pygame.key.get_focused():
    #     #print("Application not in focus! Click the application window to re-enable control.")
    # #else:
    # msg = {
    #         "ly": 0,
    #         "lx": 0,
    #         "rx": 0,
    #         "ry": 0,
    #         "L2": 0,
    #         "R2": 0,
    #         "R1": 0,
    #         "L1": 1,
    #         "dpady": 0,
    #         "dpadx": 0,
    #         "x": 0,
    #         "square": 0,
    #         "circle": 0,
    #         "triangle": 0,
    #         "message_rate": MESSAGE_RATE,
    #     }
    # pub.send(msg)
    # #pygame.display.flip()
    # pygame.time.wait(int(1000/MESSAGE_RATE))
    # pygame.time.wait(500)
    # msg = {
    #         "ly": 0,
    #         "lx": 0,
    #         "rx": 0,
    #         "ry": 0,
    #         "L2": 0,
    #         "R2": 0,
    #         "R1": 0,
    #         "L1": 0,
    #         "dpady": 0,
    #         "dpadx": 0,
    #         "x": 0,
    #         "square": 0,
    #         "circle": 0,
    #         "triangle": 0,
    #         "message_rate": MESSAGE_RATE,
    #     }
    # pub.send(msg)
    # #pygame.display.flip()
    # pygame.time.wait(int(500/MESSAGE_RATE))
    pygame.time.wait(500)
    while(1):
        disp.show_image('owlpng/garden2/frame_00_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden2/frame_01_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden2/frame_02_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden2/frame_03_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden2/frame_04_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden2/frame_05_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden2/frame_06_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden2/frame_07_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden2/frame_08_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden2/frame_09_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_00_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_01_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_00_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_01_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_02_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_03_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_04_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_05_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_06_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_07_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_08_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_09_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_10_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_11_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_12_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_13_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_14_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_15_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_16_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_17_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_18_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_19_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_20_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_21_delay-0.1s.png')
        pygame.time.wait(500)   
        disp.show_image('owlpng/garden3/frame_22_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_23_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_24_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_25_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_26_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_27_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_28_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_29_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_30_delay-0.1s.png')
        pygame.time.wait(500)
        disp.show_image('owlpng/garden3/frame_31_delay-0.1s.png')
        pygame.time.wait(500)
    
        # msg = {
        #         "ly": 0,
        #         "lx": 0,
        #         "rx": 0,
        #         "ry": 0,
        #         "L2": 0,
        #         "R2": 0,
        #         "R1": 0,
        #         "L1": 1,
        #         "dpady": 0,
        #         "dpadx": 0,
        #         "x": 0,
        #         "square": 0,
        #         "circle": 0,
        #         "triangle": 0,
        #         "message_rate": MESSAGE_RATE,
        #     }
    # pub.send(msg)
    # #pygame.display.flip()
    # pygame.time.wait(int(1000/MESSAGE_RATE))
