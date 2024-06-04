from UDPComms import Publisher
pub = Publisher(8830)
import pygame




def pub_msg(msg,wait_time):
    pub.send(msg)
    #pygame.display.flip()
    pygame.time.wait(int(1000/20))
    pygame.time.wait(wait_time)

def reset():
    msg = {
        "ly": 0,
        "lx": 0,
        "rx": 0,
        "ry": 0,
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 0,
        "dpadx": 0,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": 20,
    }
    return msg

def toggle_activation(counter_a):
        counter_a += 1
        if(counter_a%2):
             print("turned on pupper")
        else :
             print("pupper turned off")         
        msg = {
            "ly": 0,
            "lx": 0,
            "rx": 0,
            "ry": 0,
            "L2": 0,
            "R2": 0,
            "R1": 0,
            "L1": 1,
            "dpady": 0,
            "dpadx": 0,
            "x": 0,
            "square": 0,
            "circle": 0,
            "triangle": 0,
            "message_rate": 20,
        }
        return msg,counter_a%2

def toggle_movement(counter_m):
        counter_m += 1
        if(counter_m%2):
             print("turned on movement")
        else :
             print("movement turned off") 
        msg = {
            "ly": 0,
            "lx": 0,
            "rx": 0,
            "ry": 0,
            "L2": 0,
            "R2": 0,
            "R1": 1,
            "L1": 0,
            "dpady": 0,
            "dpadx": 0,
            "x": 0,
            "square": 0,
            "circle": 0,
            "triangle": 0,
            "message_rate": 20,
        }
        return msg,counter_m%2

def movement_dpapx_negative():
    msg = {
        "ly": 0,
        "lx": 0,
        "rx": 0,
        "ry": 0,
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 0,
        "dpadx": -1,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": 20,
    }
    return msg

def movement_dpapx_positive():
    msg = {
        "ly": 0,
        "lx": 0,
        "rx": 0,
        "ry": 0,
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 0,
        "dpadx": 1,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": 20,
    }
    return msg

def movement_dpapy_positive():
    msg = {
        "ly": 0,
        "lx": 0,
        "rx": 0,#counter
        "ry": 0,#clockwise
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 1,
        "dpadx": 0,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": 20,
    }

def movement_dpapy_negative():
    msg = {
        "ly": 0,
        "lx": 0,
        "rx": 0,#counter
        "ry": 0,#clockwise
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": -1,
        "dpadx": 0,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": 20,
    }

def movement_rx(val):  
    msg = {
        "ly": 0,
        "lx": 0,
        "rx": val,#counter
        "ry": 0,#clockwise
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 0,
        "dpadx": 0,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": 20,
    }
    return msg

def movement_ry(val):
    msg = {
        "ly": 0,
        "lx": 0,
        "rx": 0,#counter
        "ry": val,#clockwise
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 0,
        "dpadx": 0,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": 20,
    }
    return msg

def movement_lx(val):  
    msg = {
        "ly": 0,
        "lx": val,
        "rx": 0,#counter
        "ry": 0,#clockwise
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 0,
        "dpadx": 0,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": 20,
    }
    return msg

def movement_ly(val):  
    msg = {
        "ly": val,
        "lx": 0,
        "rx": 0,#counter
        "ry": 0,#clockwise
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 0,
        "dpadx": 0,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": 20,
    }
    return msg

def movement_rx_ry(val_rx, val_ry):  
    msg = {
        "ly": 0,
        "lx": 0,
        "rx": val_rx,#counter
        "ry": val_ry,#clockwise
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 0,
        "dpadx": 0,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": 20,
    }
    return msg

def movement_lx_ly(val_lx, val_ly):  
    msg = {
        "ly": val_ly,
        "lx": val_lx,
        "rx": 0,#counter
        "ry": 0,#clockwise
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 0,
        "dpadx": 0,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": 20,
    }
    return msg