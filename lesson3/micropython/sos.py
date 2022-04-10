import machine
import utime
led_external = machine.Pin(15, machine.Pin.OUT)
while True:
    led_external.toggle() # dot
    utime.sleep(0.5)
    led_external.toggle() # pause
    utime.sleep(0.5)
    led_external.toggle() # dot
    utime.sleep(0.5)
    led_external.toggle() # pause
    utime.sleep(0.5)
    led_external.toggle() # dot
    utime.sleep(0.5)
    led_external.toggle() # pause
    utime.sleep(0.5)
    led_external.toggle() # dash
    utime.sleep(1.5)
    led_external.toggle() # pause
    utime.sleep(0.5)
    led_external.toggle() # dash
    utime.sleep(1.5)
    led_external.toggle() # pause
    utime.sleep(0.5)
    led_external.toggle() # dash
    utime.sleep(1.5)
    led_external.toggle() # pause
    utime.sleep(0.5)
    led_external.toggle() # dot
    utime.sleep(0.5)
    led_external.toggle() # pause
    utime.sleep(0.5)
    led_external.toggle() # dot
    utime.sleep(0.5)
    led_external.toggle() # pause
    utime.sleep(0.5)
    led_external.toggle() # dot
    utime.sleep(0.5)
    led_external.toggle() # pause
    utime.sleep(0.5)
