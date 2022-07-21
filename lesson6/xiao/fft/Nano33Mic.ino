#include <PDM.h>
#include <arduinoFFT.h>

#define SAMPLES 256             //Must be a power of 2
#define SAMPLING_FREQUENCY 16000 //Hz, must be less than 10000 due to ADC
short sampleBuffer[SAMPLES];
volatile int samplesRead;

unsigned long microseconds;


double vReal[SAMPLES];
double vImag[SAMPLES];

void onPDMdata(void);

const int ledPin = 22;
const int ledPin2 = 23;
const int ledPin3 = 24;
const uint8_t amplitude = 100;

arduinoFFT FFT = arduinoFFT();

void setup() {
  Serial.begin(115200);
   
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
 
  PDM.onReceive(onPDMdata);
  PDM.setBufferSize(SAMPLES);
  //PDM.setGain(0);
  // setup the I2S audio input for the sample rate with 32-bits per sample
  if (!PDM.begin(1, 16000)) {
    Serial.println("Failed to start PDM!");
    while (1);
  }
  pinMode(22, OUTPUT);
  pinMode(23, OUTPUT);
  pinMode(24, OUTPUT);

  digitalWrite(ledPin, HIGH);
  digitalWrite(ledPin2, HIGH);
  digitalWrite(ledPin3, HIGH);
  
}

void lightOne() {
  digitalWrite(ledPin, LOW);
  digitalWrite(ledPin2, HIGH);
  digitalWrite(ledPin3, HIGH);
}

void lightTwo() {
  digitalWrite(ledPin, HIGH);
  digitalWrite(ledPin2, LOW);
  digitalWrite(ledPin3, HIGH);
}

void lightThree() {
  digitalWrite(ledPin, HIGH);
  digitalWrite(ledPin2, HIGH);
  digitalWrite(ledPin3, LOW);
}

void loop() {
  if (samplesRead) {
    for (int i = 0; i < SAMPLES; i++) {
      vReal[i] = sampleBuffer[i];
      vImag[i] = 0;
    }

    FFT.Windowing(vReal, SAMPLES, FFT_WIN_TYP_HAMMING, FFT_FORWARD);
    FFT.Compute(vReal, vImag, SAMPLES, FFT_FORWARD);
    FFT.ComplexToMagnitude(vReal, vImag, SAMPLES);
 
    double peak = FFT.MajorPeak(vReal, SAMPLES, SAMPLING_FREQUENCY);
    
    Serial.println(peak);
    
    if (peak <=600)
      lightOne();
    if (peak >600 && peak < 1200)
      lightTwo();
    if (peak >= 1200)
      lightThree();
    samplesRead = 0;
   
  }
}

void onPDMdata()
{
  int bytesAvailable = PDM.available();
  PDM.read(sampleBuffer, bytesAvailable);
  samplesRead = bytesAvailable / 2;
}
