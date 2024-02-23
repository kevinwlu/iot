/*
    ARDUINO RGB LED TUTORIAL: Loop RGB
    By: TheGeekPub.com
    More Arduino Tutorials: https://www.thegeekpub.com/arduino-tutorials/
*/
  
const int PIN_RED   = 9; //Red LED on pin 9
const int PIN_GREEN = 10; //Green LED on pin 10
const int PIN_BLUE  = 11; //Blue LED on Pin 11
  
//variables to hold our color intensities
int red;
int green;
int blue;
  
/* This function "Set Color" will set the color of the LED
   rather than doing it over and over in the loop. */
void setColor(int R, int G, int B) {
  analogWrite(PIN_RED,   R);
  analogWrite(PIN_GREEN, G);
  analogWrite(PIN_BLUE,  B);
}
  
void setup() {
  //set all three pins to output mode
  pinMode(PIN_RED,   OUTPUT);
  pinMode(PIN_GREEN, OUTPUT);
  pinMode(PIN_BLUE,  OUTPUT);
  
}
  
void loop() {
 
  // set the colors of the LED
  // Loop through Red-Green-Blue and repeat
  setColor(255, 0, 0); //set LED to Red
  delay(500);
  setColor(0, 255, 0); //set LED to Green
  delay(500);
  setColor(0, 0, 255); //set LED to Blue
  delay(500);
   
}
