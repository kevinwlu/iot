'''
https://class.textile-academy.org/2020/jeanmarie.durney/assignments/week05/
'''
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from touchio import TouchIn
import adafruit_dotstar as dotstar

# external RGB led connected to A0
pixel_pin = board.A0
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
# One pixel connected internally!
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Analog input on A1
analog1in = AnalogIn(board.A1)

# Capacitive touch on A2
touch = TouchIn(board.A2)

# Helper to convert analog input to voltage
def getVal():
    Valpot = analog1in.value / 256
    if Valpot > 255:
        Valpot = 255
    if Valpot < 0:
        Valpot = 0
    Valpot = int(Valpot)
    return (Valpot)

ValR = 0
ValG = 0
ValB = 0

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
Compteur = 0


dot[0] = WHITE
dot.show()

# MAIN LOOP
while True:

# print for debug
#   print("A1: ", getVal(), Compteur, ValR, ValG, ValB)

    # use A2 as capacitive touch to turn on internal LED
    if touch.value:
        print("A2 touched!", Compteur)
        Compteur = Compteur + 1
    led.value = touch.value

    while touch.value and Compteur == 1:
        dot[0] = RED
        dot.show()
        ValR = getVal()


    while touch.value and Compteur == 2:
        dot[0] = GREEN
        dot.show()
        ValG = getVal()

    while touch.value and Compteur == 3:
        dot[0] = BLUE
        dot.show()
        ValB = getVal()

    while touch.value and Compteur == 4:
        dot[0] = BLACK
        dot.show()
        pixels[0] = (ValR, ValG, ValB)
        pixels.show()

    if Compteur == 4:
        Compteur = 0
        ValR = 0
        ValG = 0
        ValB = 0
