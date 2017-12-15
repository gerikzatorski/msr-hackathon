#!/usr/bin/env python
import serial
import rospy
from numpy import binary_repr
import time
from std_msgs.msg import String
from geometry_msgs.msg import Point

horiz_channel = 0x05
vert_channel = 0x04
port1 = '/dev/ttyACM0'

hPos = 1500
vPos = 1500


def target_low_bits(x):
    number_string = str(binary_repr(x*4, width=14))
    number_string = number_string[-7:]
    number_string = '0' + number_string
    return int(number_string, 2)

def target_high_bits(x):
    number_string = str(binary_repr(x*4, width=14))
    number_string = number_string[:7]
    number_string = '0' + number_string
    return int(number_string, 2)

def go_home(port):
    cmd_seq = []
    cmd_seq.append(chr(0x84))
    cmd_seq.append(chr(horiz_channel))
    cmd_seq.append(chr(0x70))
    cmd_seq.append(chr(0x2E))

    cmd_string = ""
    for i in cmd_seq:
        cmd_string += i
    port.write(cmd_string)

def set_horiz_target(port,pos):
    cmd_seq = []
    cmd_seq.append(chr(0x84))
    cmd_seq.append(chr(horiz_channel))
    cmd_seq.append(chr(target_low_bits(pos)))
    cmd_seq.append(chr(target_high_bits(pos)))

    cmd_string = ""
    for i in cmd_seq:
        cmd_string += i
    port.write(cmd_string)

def set_vert_target(port,pos):
    cmd_seq = []
    cmd_seq.append(chr(0x84))
    cmd_seq.append(chr(vert_channel))
    cmd_seq.append(chr(target_low_bits(pos)))
    cmd_seq.append(chr(target_high_bits(pos)))

    cmd_string = ""
    for i in cmd_seq:
        cmd_string += i
    port.write(cmd_string)

'''
    if i.y < -deadzone:
        vPos += (vPos/3)
    elif i.y > deadzone:
        vPos -= 5
    if i.x > deadzone:
        hPos += 5
    elif i.x < -deadzone:
        hPos -= 5
'''

def callback(data):
    global hPos
    global vPos
    i =data
    deadzone = 40

    print "data.x = ",
    print data.x
    print "data.y = ",
    print data.y

    if i.y < -deadzone or i.y > deadzone:
        vPos += int(i.y/10)
    if i.x < -deadzone or i.x > deadzone:
        hPos += int(i.x/10)

    #elif i == "q":
     #   ser1.close()
    set_horiz_target(ser1,hPos)
    set_vert_target(ser1,vPos)

rospy.init_node('motor_converter', anonymous=True)
sub = rospy.Subscriber("servo_commands",Point, callback)
ser1 = serial.Serial(port1)
set_horiz_target(ser1,1500)
set_vert_target(ser1,1500)

rospy.spin()

def loop():
    ser1 = serial.Serial(port1)

    hPos = 1500
    vPos = 1500
    set_horiz_target(ser1,hPos)
    set_vert_target(ser1,vPos)

    try:
        while True:
            i = raw_input()
            if i == "u":
                vPos += 50
            elif i == "d":
                vPos -= 50
            elif i == "r":
                hPos += 50
            elif i == "l":
                hPos -= 50
            set_horiz_target(ser1,hPos)
            set_vert_target(ser1,vPos)
    except KeyboardInterrupt:
        ser1.close()
        ser2.close()

#if __name__ == '__main__':
    #print target_low_bits(1500)
    #print target_high_bits(1500)
    #$loop()
