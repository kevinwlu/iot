void setup() {
    Serial.begin(115200); // open serial connection to USB Serial
                          // port (connected to your computer) 
    Serial1.begin(57600); // open internal serial connection to
                          // MT7688
    pinMode(13, OUTPUT);  // in MT7688, this maps to device
} 

void loop() {
    int c = Serial1.read();// read from MT7688
    if (c != -1) {
        switch(c) {
            case '0':  // turn off D13 when receiving "0"
            digitalWrite(13, 0);
            break;
            case '1':  // turn on D13 when receiving "1"
            digitalWrite(13, 1);
            break;
        }
    }
}
