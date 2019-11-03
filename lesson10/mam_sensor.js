/*
Author: Robert Lie (mobilefish.com)
The mam_sensor.js file publishes DHT11 sensor data (temperature and humidity) on the tangle using MAM.
This file only works on the Raspberry Pi.
The published data can be viewed using the mam_receive.js file or
https://www.mobilefish.com/services/cryptocurrency/mam.html (Select option: Data receiver)
Usage:
1)  Connect DHT11 sensor to Raspberry Pi.
2)  Do not forget to type: npm install
3)  You can change the default settings: MODE, SIDEKEY, SECURITYLEVEL or TIMEINTERVAL
    If you do, make the same changes in mam_receive.js file.
4)  Start the app: node mam_sensor.js
More information:
https://www.mobilefish.com/developer/iota/iota_quickguide_raspi_mam.html
*/
const sensor = require('node-dht-sensor');
const Mam = require('./lib/mam.client.js');
const IOTA = require('iota.lib.js');
const moment = require('moment');

const iota = new IOTA({ provider: 'https://nodes.devnet.iota.org:443' });

const MODE = 'restricted'; // public, private or restricted
const SIDEKEY = 'mysecret'; // Enter only ASCII characters. Used only in restricted mode
const SECURITYLEVEL = 3; // 1, 2 or 3
const TIMEINTERVAL = 30; // seconds
const SENSORTYPE = 11; // 11=DHT11, 22=DHT22
const GPIOPIN = 4; // The Raspi gpio pin where data from the DHT11 is read

// Initialise MAM State
let mamState = Mam.init(iota, undefined, SECURITYLEVEL);

// Set channel mode
if (MODE == 'restricted') {
    const key = iota.utils.toTrytes(SIDEKEY);
    mamState = Mam.changeMode(mamState, MODE, key);
} else {
    mamState = Mam.changeMode(mamState, MODE);
}

// Publish to tangle
const publish = async function(packet) {
    // Create MAM Payload
    const trytes = iota.utils.toTrytes(JSON.stringify(packet));
    const message = Mam.create(mamState, trytes);

    // Save new mamState
    mamState = message.state;
    console.log('Root: ', message.root);
    console.log('Address: ', message.address);

    // Attach the payload.
    await Mam.attach(message.payload, message.address);

    return message.root;
}

function readSensor(){
    sensor.read(SENSORTYPE, GPIOPIN, async function(err, temperature, humidity) {
        if (!err) {
            const dateTime = moment().utc().format('DD/MM/YYYY hh:mm:ss');
            const data = `{temp: ${temperature.toFixed(1)} C, humidity: ${humidity.toFixed(1)} %}`;
            const json = {"data": data, "dateTime": dateTime};

            const root = await publish(json);
            console.log(`dateTime: ${json.dateTime}, data: ${json.data}, root: ${root}`);

        } else {
            console.log(err);
        }
    });
}

// Start it immediately
readSensor();

// Automatically update sensor value every N seconds
setInterval(readSensor, TIMEINTERVAL*1000);
