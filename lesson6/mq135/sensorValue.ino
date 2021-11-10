int sensorValue;
void setup()
{
Serial.begin(9600); // Baud rate 9600
}
void loop()
{
sensorValue = analogRead(0); // Read analog input pin A0
Serial.println(sensorValue, DEC); // Print the value read
delay(1000); 
}
