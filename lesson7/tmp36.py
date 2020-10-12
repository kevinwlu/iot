import json
import time
import readadc
import datetime
import RPi.GPIO as GPIO

# temperature sensor middle pin connected channel 1 of mcp3008
sensor_pin = 1
readadc.initialize()

#the main sensor reading and plotting loop
while True:
    try:
        sensor_data = readadc.readadc(sensor_pin,
                                      readadc.PINS.SPICLK,
                                      readadc.PINS.SPIMOSI,
                                      readadc.PINS.SPIMISO,
                                      readadc.PINS.SPICS)

        millivolts = sensor_data * (3300.0 / 1024.0)
        # 10 mv per degree
        temp_C = ((millivolts - 100.0) / 10.0) - 40.0
        # convert celsius to fahrenheit
        temp_F = (temp_C * 9.0 / 5.0) + 32
        # remove decimal point from millivolts
        millivolts = "%d" % millivolts
        # show only one decimal place for temprature and voltage readings
        temp_C = "%.1f" % temp_C
        temp_F = "%.1f" % temp_F

        # print the data
        print(datetime.datetime.now(), temp_C)

        # delay between stream posts
        time.sleep(10)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
