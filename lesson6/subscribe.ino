int led = D0;
int boardLed = D7;
int photoresistor = A0;
int power = A5;
int intactValue;
int brokenValue;
int beamThreshold;
bool beamBroken = false;
void setup() {
  pinMode(led,OUTPUT);
  pinMode(boardLed,OUTPUT);
  pinMode(photoresistor,INPUT);
  pinMode(power,OUTPUT);
  Spark.subscribe("buddy_unique_event_name", myHandler);
  analogWrite(power,4095);
  digitalWrite(boardLed,HIGH);
  delay(2000);
  digitalWrite(boardLed,LOW);
  digitalWrite(led,HIGH);
  delay(500);
  int on_1 = analogRead(photoresistor);
  delay(200);
  int on_2 = analogRead(photoresistor);
  delay(300);
  digitalWrite(boardLed,HIGH);
  delay(100);
  digitalWrite(boardLed,LOW);
  delay(100);
  digitalWrite(boardLed,HIGH);
  delay(100);
  digitalWrite(boardLed,LOW);
  delay(100);
  digitalWrite(boardLed,HIGH);
  delay(2000);
  digitalWrite(boardLed,LOW);
  int off_1 = analogRead(photoresistor);
  delay(200);
  int off_2 = analogRead(photoresistor);
  delay(1000);
  digitalWrite(boardLed,HIGH);
  delay(100);
  digitalWrite(boardLed,LOW);
  delay(100);
  digitalWrite(boardLed,HIGH);
  delay(100);
  digitalWrite(boardLed,LOW);
  delay(100);
  digitalWrite(boardLed,HIGH);
  delay(100);
  digitalWrite(boardLed,LOW);
  intactValue = (on_1+on_2)/2;
  brokenValue = (off_1+off_2)/2;
  beamThreshold = (intactValue+brokenValue)/2;
}
void loop() {
  if (analogRead(photoresistor)>beamThreshold) {
    if (beamBroken==true) {
      Spark.publish("your_unique_event_name","intact");
      beamBroken=false;
    }
  }
  else {
    if (beamBroken==false) {
      Spark.publish("your_unique_event_name","broken");
      beamBroken=true;
    }
  }
}
void myHandler(const char *event, const char *data)
{
  if (strcmp(data,"intact")==0) {
    digitalWrite(boardLed,LOW);
  }
  else if (strcmp(data,"broken")==0) {
    digitalWrite(boardLed,HIGH);
  }
  else {
  }
}
