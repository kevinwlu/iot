int led = D0;
int photoresistor = A0;
int power = A5;
int analogvalue;
void setup() {
    pinMode(led,OUTPUT);
    pinMode(photoresistor,INPUT);
    pinMode(power,OUTPUT);
    digitalWrite(power,HIGH);
    Spark.variable("analogvalue", &analogvalue, INT);
    Spark.function("led",ledToggle);
}
void loop() {
    analogvalue = analogRead(photoresistor);
}
int ledToggle(String command) {
    if (command=="on") {
        digitalWrite(led,HIGH);
        return 1;
    }
    else if (command=="off") {
        digitalWrite(led,LOW);
        return 0;
    }
    else {
        return -1;
    }
}
