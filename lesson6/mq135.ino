// https://stackoverflow.com/questions/31109021/how-to-find-co2-and-o2-level-using-mq135-with-arduino
int sensorValue;
int pin8 = 8;
void setup()
{
  Serial.begin(9600);      // sets the serial port to 9600
  pinMode(pin8, OUTPUT);
}

void loop()
{
  sensorValue = analogRead(0);       // read analog input pin 0
  Serial.print(sensorValue, DEC);  // prints the value read
  Serial.println("ppm");
  if (sensorValue > 500) {
    // Activate digital output pin 8 - the LED will light up
    digitalWrite(pin8, HIGH);
  }
  else {
    // Deactivate digital output pin 8 - the LED will not light up
    digitalWrite(pin8, LOW);
  }

  delay(5000);                        // wait 5000 ms for next reading
}
