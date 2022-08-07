#include <ArduinoBLE.h>

BLEService echoService("00000000-0000-1000-8000-00805f9b34fb");
BLEStringCharacteristic charac ("741c12b9-e13c-4992-8a5e-fce46dec0bff", BLERead | BLEWrite | BLENotify,40);
BLEDescriptor Descriptor("beca6057-955c-4f8a-e1e3-56a1633f04b1","Descriptor");
String var = "";

void setup(){
  Serial.begin(9600);
  while(!Serial);

  if(!BLE.begin()){
    Serial.println("starting BLE failed.");
    while(1);
  }

  
  BLE.setLocalName("Arduino BLE Echo");
  BLE.setAdvertisedService(echoService);
  charac.addDescriptor(Descriptor);
  echoService.addCharacteristic(charac);
  BLE.addService(echoService);
  BLE.advertise();
  Serial.println("Bluetooth device active, waiting for connections...");
  Serial.println(" ");

}

void loop(){
  BLEDevice central = BLE.central();
  if(central){
    Serial.println("* Connected to central device!");
    Serial.print("Connected to central : ");
    Serial.println(central.address());
    Serial.println(" ");

    while(central.connected()){
      if(charac.written()){
        var = charac.value();
        Serial.println(String(var));
        delay(500);
        charac.writeValue(var);
        Serial.println("write stringCharacteristic");
      }
      
    }
    Serial.print("Disconnected from central: ");
    Serial.println(central.address());   
  }
}
