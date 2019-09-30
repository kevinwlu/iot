#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gpiotest.py
#
#  Copyright 2016 Roman Mindlin <Roman@Mindlin.ru>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

import sys
import getopt
import curses
import random
import time
from datetime import datetime

def termOn():
    # Enable character buffering and echo
    curses.nocbreak()
    curses.echo()

def termOff():
    # Disable character buffering and echo
    curses.cbreak()
    curses.noecho()

def MainScreen():
    #Draw main screen
    #coords - screen position of placeholders for pin states
    coords = [[6,15],[7,15],[8,15],[9,15],[10,15],[11,15],[12,15],[13,15],[14,15],
            [6,42],[7,42],[8,42],[9,42],[10,42],[11,42],[12,42],[13,42],[14,42],
            [6,69],[7,69],[8,69],[9,69],[10,69],[11,69],[12,69],[13,69]]

    myscreen.erase()
    myscreen.addstr(1,0, "--------------------------------------------------------------------------------")
    myscreen.addstr(2,0, "|                        * Raspberry Pi GPIO monitor *                         |")
    myscreen.addstr(3,0, "--------------------------------------------------------------------------------")
    myscreen.addstr(4,0, "|                                                      *   Debounce            |")
    myscreen.addstr(4,2, RaspiModel + " detected (" + str(gpio_num) + " lines)")
    myscreen.addstr(4,68, str(debounce) + " ms")
    myscreen.addstr(5,0, "--------------------------------------------------------------------------------")
    if (gpio_num == 17):
        myscreen.addstr(6,0, "|     GPIO0  =           |      GPIO15  =            |                         |")
        myscreen.addstr(7,0, "|     GPIO1  =           |      GPIO17  =            |                         |")
        myscreen.addstr(8,0, "|     GPIO4  =           |      GPIO18  =            |                         |")
        myscreen.addstr(9,0, "|     GPIO7  =           |      GPIO21  =            |                         |")
        myscreen.addstr(10,0, "|     GPIO8  =           |      GPIO22  =            |                         |")
        myscreen.addstr(11,0, "|     GPIO9  =           |      GPIO23  =            |                         |")
        myscreen.addstr(12,0, "|     GPIO10 =           |      GPIO24  =            |                         |")
        myscreen.addstr(13,0, "|     GPIO11 =           |      GPIO25  =            |                         |")
        myscreen.addstr(14,0, "|     GPIO14 =           |                           |                         |")
    else:
        myscreen.addstr(6,0, "|     GPIO2  =           |      GPIO11  =            |      GPIO20 =           |")
        myscreen.addstr(7,0, "|     GPIO3  =           |      GPIO12  =            |      GPIO21 =           |")
        myscreen.addstr(8,0, "|     GPIO4  =           |      GPIO13  =            |      GPIO22 =           |")
        myscreen.addstr(9,0, "|     GPIO5  =           |      GPIO14  =            |      GPIO23 =           |")
        myscreen.addstr(10,0, "|     GPIO6  =           |      GPIO15  =            |      GPIO24 =           |")
        myscreen.addstr(11,0, "|     GPIO7  =           |      GPIO16  =            |      GPIO25 =           |")
        myscreen.addstr(12,0, "|     GPIO8  =           |      GPIO17  =            |      GPIO26 =           |")
        myscreen.addstr(13,0, "|     GPIO9  =           |      GPIO18  =            |      GPIO27 =           |")
        myscreen.addstr(14,0, "|     GPIO10 =           |      GPIO19  =            |                         |")
    myscreen.addstr(15,0,  "--------------------------------------------------------------------------------")
    myscreen.addstr(21,0,  "--------------------------------------------------------------------------------")
    myscreen.addstr(23,0,  "Q = Quit  P = Pause  D = Debounce  U = pullUp  O = Output I = Input")


    #Print states and pullup status
    for i in range(gpio_num):
        state_text = "True" if gpio_state[i] else "False"
        state_text = state_text + ("(^)" if gpio_pud[i] else "(v)")
        myscreen.addstr(coords[i][0], coords[i][1], state_text,
                        curses.A_REVERSE if gpio_inout[i] else curses.A_NORMAL)

    #Activity indicator
    myscreen.addstr(0,0, chr(int(random.random()*32) + 32))

    # Print log strings
    logwindow.erase()
    for i in range(0,5):
        logwindow.insstr(i,0,log[i])

    #Set cursor position
    myscreen.move(22,0)
    myscreen.refresh()

def SendToLog(LogMessage):
    # Rotate log lines
    global log
    for i in range(0,5):
        log[i] = log[i+1]
    log[4] = LogMessage

def PrintMsg(Msg):
    # Print messages on bottom line of screen
    msgwindow.erase()
    msgwindow.addstr(Msg)
    msgwindow.refresh()

def CheckKeys():
    # Keyboard events
    global debounce
    global on_pause

    myscreen.nodelay(1)
    key = myscreen.getch()
    myscreen.nodelay(0)

    if key == ord('q') or key == ord('Q'):
        raise KeyboardInterrupt
    elif key == ord('p') or key == ord('P'):
        PrintMsg("Paused. Press P again to continue")
        on_pause = 1
        while on_pause:
            key = msgwindow.getch()
            if key == ord('p') or key == ord('P'):
                on_pause = 0
    elif key == ord('d') or key == ord('D'):
        try:
            termOn()
            PrintMsg("Enter debounce value (ms): ")
            debounce_ = int(msgwindow.getstr())
            if (debounce_ < 0 or debounce_ > 5000):
                raise ValueError
            if (debounce_ != debounce):
                debounce = debounce_
                initGpio()
            termOff()
        except ValueError:
            PrintMsg("Value not in range")
            termOff()
            msgwindow.getch()
    elif key == ord('u') or key == ord('U'):
        try:
            termOn()
            PrintMsg("Enter GPIO line number: ")
            channel = int(msgwindow.getstr())
            if not (channel in gpio_ch):
                raise ValueError
            num = gpio_ch.index(channel)
            if (gpio_inout[num]):
                raise IOError
            PrintMsg("Enter 0 for GPIO.PUD_DOWN or 1 GPIO.PUD_UP: ")
            pud = int(msgwindow.getstr())
            if (pud != 1 and pud != 0):
                raise ValueError
            gpio_pud[num] = pud
            initGpio()
            termOff()
        except ValueError:
            PrintMsg("Value not in range")
            termOff()
            msgwindow.getch()
        except IOError:
            PrintMsg("Output line cannot be pulled up")
            termOff()
            msgwindow.getch()
    elif key == ord('o') or key == ord('O'):
        try:
            termOn()
            PrintMsg("Enter GPIO line number: ")
            channel = int(msgwindow.getstr())
            if not (channel in gpio_ch):
                raise ValueError
            num = gpio_ch.index(channel)
            PrintMsg("Enter 0 for GPIO.LOW or 1 GPIO.HIGH: ")
            val = int(msgwindow.getstr())
            if (val != 1 and val != 0):
                raise ValueError
            gpio_inout[num] = 1
            gpio_state[num] = val
            GPIO.setup(channel, GPIO.OUT)
            GPIO.output(channel,GPIO.HIGH if val else GPIO.LOW)
            termOff()
        except ValueError:
            PrintMsg("Value not in range")
            termOff()
            msgwindow.getch()
    elif key == ord('i') or key == ord('I'):
        try:
            termOn()
            PrintMsg("Enter GPIO line number: ")
            channel = int(msgwindow.getstr())
            if not (channel in gpio_ch):
                raise ValueError
            num = gpio_ch.index(channel)
            gpio_inout[num] = 0
            initGpio()
            termOff()
        except ValueError:
            PrintMsg("Value not in range")
            termOff()
            msgwindow.getch()

def getPinFunctionName(pin):
    # Unused
    functions = {GPIO.IN:'Input',
                 GPIO.OUT:'Output',
                 GPIO.I2C:'I2C',
                 GPIO.SPI:'SPI',
                 GPIO.HARD_PWM:'HARD_PWM',
                 GPIO.SERIAL:'Serial',
                 GPIO.UNKNOWN:'Unknown'}

    return functions[GPIO.gpio_function(pin)]

def getRaspiModel(argument):
    #Detect Raspberry Pi model
    switcher = {
        "0002": "Model B Revision 1.0 256Mb",
        "0003": "Model B Revision 1.0 + ECN0001 256Mb",
        "0004": "Model B Revision 2.0 256Mb",
        "0005": "Model B Revision 2.0 256Mb",
        "0006": "Model B Revision 2.0 256Mb",
        "0007": "Model A 256Mb",
        "0008": "Model A 256Mb",
        "0009": "Model A 256Mb",
        "000d": "Model B Revision 2.0 512Mb",
        "000e": "Model B Revision 2.0 512Mb",
        "000f": "Model B Revision 2.0 512Mb",
        "0010": "Model B+ 512Mb",
        "0012": "Model A+ 256Mb",
        "0013": "Model B+ 512Mb",
        "0015": "Model A+ 256/512Mb",
        "a01040": "2 Model B Revision 1.0 1Gb",
        "a01041": "2 Model B Revision 1.1 1Gb",
        "a21041": "2 Model B Revision 1.1 1Gb",
        "a22042": "2 Model B (with BCM2837) 1Gb",
        "900021": "Model A+ 512Mb",
        "900032": "Model B+ 512Mb",
        "900092": "Zero Revision 1.2 512Mb",
        "900093": "Zero Revision 1.3 512Mb",
        "920093": "Zero Revision 1.3 512Mb",
        "9000c1": "Zero W Revision 1.1 512Mb",
        "a02082": "3 Model B 1Gb",
        "a22082": "3 Model B 1Gb",
        "a32082": "3 Model B 1Gb",
        "a020d3": "3 Model B+ 1Gb",
        "9020e0": "3 Model A+ 512Mb"
    }
    return switcher.get(argument, "not supported")

def getGpioNum(argument):
    #Return number of GPIO lines
    switcher = {
        "0002": 17,
        "0003": 17,
        "0004": 17,
        "0005": 17,
        "0006": 17,
        "0007": 17,
        "0008": 17,
        "0009": 17,
        "000d": 17,
        "000e": 17,
        "000f": 17,
        "0010": 26,
        "0012": 26,
        "0013": 26,
        "0015": 26,
        "a01040": 26,
        "a01041": 26,
        "a21041": 26,
        "a22042": 26,
        "900021": 26,
        "900032": 26,
        "900092": 26,
        "900093": 26,
        "920093": 26,
        "9000c1": 26,
        "a02082": 26,
        "a22082": 26,
        "a32082": 26,
        "a020d3": 26,
        "9020e0": 26
    }
    return switcher.get(argument, 17)

def initGpio(firstrun=0):
    curses.savetty()  #Save screen

    #Init GPIO
    if not firstrun:
        GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(0)

    #Init GPIO pins, set event_detect callbacks, save initial states etc.
    for i,channel in enumerate(gpio_ch):
        if not gpio_inout[i]:
            GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN if gpio_pud[i] == 0 else GPIO.PUD_UP)
            GPIO.add_event_detect(channel, GPIO.BOTH, callback = gpio_callback, bouncetime = debounce)
            gpio_state[i] = GPIO.input(channel) # Primary state

    curses.resetty()  # Restore screen

def gpio_callback(channel):
    # Callback fucntion - waiting for event, changing gpio states
    global gpio_state

    if not on_pause:
        gpio_state[gpio_ch.index(channel)] = GPIO.input(channel)
    SendToLog(datetime.now().strftime("%Y-%b-%d %H:%M:%S")+": Channel " + str(channel) +
          " changed " + ("(on)" if GPIO.input(channel) else "(off)")+"\n")

try:
    #Check command line options
    gpio_num = 0
    opts, args = getopt.getopt(sys.argv[1:],"hg:",["help","gpio_num="])
except getopt.GetoptError:
    print('Usage: gpiotest.py [--gpio_num <num>]')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h' or opt == '--help':
        print('Usage: gpiotest.py [--gpio_num <num>]')
        sys.exit()
    elif opt == '-g' or opt == '--gpio_num':
        if arg == '17':
            gpio_num = 17
        elif arg == '26':
            gpio_num = 26
        else:
            print('Error: gpio_num must be 17 or 26')
            sys.exit()

try:
    #Detect Raspberry Pi model
    RaspiModel = getRaspiModel(GPIO.RPI_INFO['REVISION'])
    if (RaspiModel == "not supported"):
        raise NameError('hardware not supported')

    #Detect GPIO parameters
    #gpio_ch - array of GPIO lines numbers
    if gpio_num == 0:
        gpio_num = getGpioNum(GPIO.RPI_INFO['REVISION'])

    if (gpio_num == 17):
        gpio_ch = [0,1,4,7,8,9,10,11,14,15,17,18,21,22,23,24,25]
    else:
        gpio_ch = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    debounce = 200

    #Init vars
    # 3 main structures:
    # gpio_state stores current states of GPIO pins
    # gpio_inout stores where pin configured to be IN or OUT
    # gpio_pud stores pin's pullup state
    gpio_state = [0 for _ in range(gpio_num)]
    gpio_inout = [0 for _ in range(gpio_num)]
    gpio_pud = [0 for _ in range(gpio_num)]
    on_pause = 0
    log = ['' for _ in range(6)]

    #Init curses
    myscreen = curses.initscr()
    logwindow = myscreen.subwin(5,80,16,0)
    msgwindow = myscreen.subwin(1,80,22,0)
    termOff()

    #Init GPIO
    initGpio(1)

    #Main loop
    while True:
        MainScreen()
        CheckKeys()
        time.sleep(0.1)

except KeyboardInterrupt:
    # In case of keyboard interrupt
    myscreen.addstr(21,0,"Ctrl-C pressed")
    time.sleep(0.5)
    GPIO.cleanup()

except Exception as e:
    print(e)

finally:
    # Reset terminal
    termOn()
    curses.endwin()
