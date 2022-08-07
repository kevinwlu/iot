/*
* Sketch: Arduino2Arduino_example2_RemoteTemp_Main
* By Martyn Currey
* 11.05.2016
* Written in Arduino IDE 1.6.3
*
* Send a temperature reading by Bluetooth
* Uses the following pins
*
* D8 - software serial RX
* D9 - software serial TX
* A0 - single wire temperature sensor
*
*
* AltSoftSerial uses D9 for TX and D8 for RX. While using AltSoftSerial D10 cannot be used for PWM.
* Remember to use a voltage divider on the Arduino TX pin / Bluetooth RX pin
* Download from https://www.pjrc.com/teensy/td_libs_AltSoftSerial.html
*/
#include <AltSoftSerial.h>
AltSoftSerial BTserial; 
 
 
// If you don't have an LCD you can use the serial monitor.
// I use the LCD library from https://bitbucket.org/fmalpartida/new-liquidcrystal/wiki/Home
// if you use a different library change the following lines
#include <Wire.h>  
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);  // Set the LCD I2C address
 
 
 
// define the pattern for a custom degree character. You can also use chr 233
byte degreeChr[8] = { B00111, B00101, B00111, B00000, B00000, B00000, B00000,}; 
 
 
 
// Set DEBUG to true to output debug information to the serial monitor
boolean DEBUG = true;
 
 
// Variables used for incoming data
const byte maxDataLength = 20;
char receivedChars[21] ;
boolean newData = false;
 
// Variables used for the timer
unsigned long startTime = 0;
unsigned long waitTime = 1000;
 
const byte TEMP_PIN = A0;
 
 
void setup()  
{
  lcd.begin(20,4); 
  lcd.createChar(1, degreeChr);
  lcd.setCursor(0,0);  lcd.print("Remote Temp Monitor"); 
  lcd.setCursor(0,1);  lcd.print("Starting..."); 
 
  if (DEBUG)
  {
       // open serial communication for debugging
       Serial.begin(9600);
       Serial.println(__FILE__);
       Serial.println(" ");
  }
 
    BTserial.begin(9600); 
    if (DEBUG)  {  Serial.println("AltSoftSerial started at 9600");     }
 
    newData = false; 
    startTime = millis();
 
} // void setup()
 
 
 
 
void loop()  
{
    if (  millis()-startTime > waitTime ) 
    {
       BTserial.print("<sendTemp>");  
       if (DEBUG) { Serial.println("Request sent"); }
       startTime = millis();
    }
 
    recvWithStartEndMarkers(); 
    if (newData)  
    {    
         if (DEBUG) { Serial.println("Data received"); }
         lcd.setCursor(0,1);   lcd.print("Temp = "); 
         lcd.setCursor(7,1);   lcd.print(receivedChars);  
         lcd.write(1);  lcd.print("C"); 
         newData = false;  
         receivedChars[0]='\0';     
    }    
}
 
 
 
 
// function recvWithStartEndMarkers by Robin2 of the Arduino forums
// See  http://forum.arduino.cc/index.php?topic=288234.0
/*
****************************************
* Function recvWithStartEndMarkers
* reads serial data and returns the content between a start marker and an end marker.
* 
* passed:
*  
* global: 
*       receivedChars[]
*       newData
*
* Returns:
*          
* Sets:
*       newData
*       receivedChars
*
*/
void recvWithStartEndMarkers()
{
     static boolean recvInProgress = false;
     static byte ndx = 0;
     char startMarker = '<';
     char endMarker = '>';
     char rc;
 
     if (BTserial.available() > 0) 
     {
          rc = BTserial.read();
          if (recvInProgress == true) 
          {
               if (rc != endMarker) 
               {
                    receivedChars[ndx] = rc;
                    ndx++;
                    if (ndx > maxDataLength) { ndx = maxDataLength; }
               }
               else 
               {
                     receivedChars[ndx] = '\0'; // terminate the string
                     recvInProgress = false;
                     ndx = 0;
                     newData = true;
               }
          }
          else if (rc == startMarker) { recvInProgress = true; }
     }
}
