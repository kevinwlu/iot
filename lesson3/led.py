from gpiozero import LED
from time import sleep

green = LED(18)

while True:
    try:
        green.on()
        sleep(2)
        green.off()
        sleep(2)
    except KeyboardInterrupt:
        exit()
