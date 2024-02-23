/*
    ARDUINO RGB LED TUTORIAL: RAINBOW COLOR
    By: TheGeekPub.com
    More Arduino Tutorials: https://www.thegeekpub.com/arduino-tutorials/
*/
 
const int PIN_RED   = 9; //Red LED on pin 9
const int PIN_GREEN = 10; //Green LED on pin 10
const int PIN_BLUE  = 11; //Blue LED on Pin 11
 
//variables to hold our color intensities and direction
//and define some initial "random" values to seed it
int red             = 254;
int green           = 1;
int blue            = 127;
int red_direction   = -1;
int green_direction = 1;
int blue_direction  = -1;
 
/* This function "Set Color" will set the color of the LED
   rather than doing it over and over in the loop above. */
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
  red = red + red_direction;   //changing values of LEDs
  green = green + green_direction;
  blue = blue + blue_direction;
 
  //now change direction for each color if it reaches 255
  if (red >= 255 || red <= 0)
  {
    red_direction = red_direction * -1;
  }
  if (green >= 255 || green <= 0)
  {
    green_direction = green_direction * -1;
  }
  if (blue >= 255 || blue <= 0)
  {
    blue_direction = blue_direction * -1;
  }
  setColor(red, green, blue);
  delay(5);    //a little delay is needed so you can see the change
}
