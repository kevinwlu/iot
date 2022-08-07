/*
* Sketch: Arduino2Arduino_Main_01
* By Martyn Currey
* 08.04.2016
* Written in Arduino IDE 1.6.3
*
* Send commands through a serial connection to turn a LED on and OFF on a remote Arduino
* There is no error checking and this sketch sends only
* Commands should be contained within the start and end markers < and >
*
* D8 - AltSoftSerial RX
* D9 - AltSoftSerial TX
*
*/
 
// AltSoftSerial uses D9 for TX and D8 for RX. While using AltSoftSerial D10 cannot be used for PWM.
// Remember to use a voltage divider on the Arduino TX pin / Bluetooth RX pin
// Download AltSoftSerial from https://www.pjrc.com/teensy/td_libs_AltSoftSerial.html
 
#include <AltSoftSerial.h>
AltSoftSerial BTserial; 
 
// Change DEBUG to true to output debug information to the serial monitor
boolean DEBUG = true;
 
void setup()  
{
    if (DEBUG)
    {
        // open serial communication for debugging and show 
        // the sketch filename and the date compiled
        Serial.begin(9600);
        Serial.println(__FILE__);
        Serial.println(__DATE__);
        Serial.println(" ");
    }
 
    //  open software serial connection to the Bluetooth module.
    BTserial.begin(9600); 
    if (DEBUG)  {   Serial.println("BTserial started at 9600");     }
 
} // void setup()
 
 
void loop()  
{
    BTserial.println("<LEDON>");
    if (DEBUG) {Serial.println("LEDON command sent");}    
    delay (1000);
 
    BTserial.println("<LEDOFF>");
    if (DEBUG) {Serial.println("LEDOFF command sent");}      
    delay (1000);    
}
