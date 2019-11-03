/*
Author: Robert Lie (mobilefish.com)
The sensor.js file reads DHT11 sensor data (temperature and humidity) and displays in on the console.
This file will only work on a Raspberry Pi.
Usage:
1)  You can change the default setting: TIMEINTERVAL
2)  Do not forget to type: npm install
3)  Start the app: node sensor.js
4)  If you encounter problems reading the DHT11 sensor data and wants more logging:
    Type: npm uninstall node-dht-sensor
    Type: npm install node-dht-sensor --dht_verbose=true
    If you have fixed your problem:
    Type: npm uninstall node-dht-sensor
    Type: npm install node-dht-sensor --dht_verbose=false
More information:
https://www.mobilefish.com/developer/iota/iota_quickguide_raspi_mam.html
*/
const sensor = require('node-dht-sensor');

const TIMEINTERVAL = 10; // seconds
const SENSORTYPE = 11; // 11=DHT11, 22=DHT22
const GPIOPIN = 4; // The Raspi gpio pin where data from the DHT11 is read

function readSensor(){
    sensor.read(SENSORTYPE, GPIOPIN, function(err, temperature, humidity) {
        if (!err) {
            console.log('temp: ' + temperature.toFixed(1) + 'C, ' + 'humidity: ' + humidity.toFixed(1) + '%');
        } else {
            console.log(err);
        }
    });
}

readSensor();

// Automatically update sensor value every N seconds
setInterval(readSensor, TIMEINTERVAL*1000);
