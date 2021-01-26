import machine
import utime
    led_external = machine.Pin(15, machine.Pin.OUT)
    button = machine.Pin(14, machine.Pin.IN)
while True:
    if button.value() == 1:
        print("You pressed the button!")
        led_external.value(1)
        utime.sleep(2)
    led_external.value(0)
