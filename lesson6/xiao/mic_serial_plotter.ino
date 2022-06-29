#include <mic.h>
#if defined(WIO_TERMINAL)
#include "processing/filters.h"
#endif

// Settings
#if defined(WIO_TERMINAL)
#define DEBUG 1                 // Enable pin pulse during ISR  
#define SAMPLES 16000*3
#elif defined(ARDUINO_ARCH_NRF52840)
#define DEBUG 1                 // Enable pin pulse during ISR  
#define SAMPLES 800
#endif

mic_config_t mic_config{
  .channel_cnt = 1,
  .sampling_rate = 16000,
  .buf_size = 1600,
#if defined(WIO_TERMINAL)
  .debug_pin = 1                // Toggles each DAC ISR (if DEBUG is set to 1)
#elif defined(ARDUINO_ARCH_NRF52840)
  .debug_pin = LED_BUILTIN                // Toggles each DAC ISR (if DEBUG is set to 1)
#endif
};

#if defined(WIO_TERMINAL)
DMA_ADC_Class Mic(&mic_config);
#elif defined(ARDUINO_ARCH_NRF52840)
NRF52840_ADC_Class Mic(&mic_config);
#endif

int16_t recording_buf[SAMPLES];
volatile uint8_t recording = 0;
volatile static bool record_ready = false;

#if defined(WIO_TERMINAL)
FilterBuHp filter;
#endif

void setup() {

  Serial.begin(115200);
  while (!Serial) {delay(10);}
  
#if defined(WIO_TERMINAL)  
  pinMode(WIO_KEY_A, INPUT_PULLUP);
#endif

  Mic.set_callback(audio_rec_callback);

  if (!Mic.begin()) {
    Serial.println("Mic initialization failed");
    while (1);
  }

  Serial.println("Mic initialization done.");

}

void loop() { 

#if defined(WIO_TERMINAL)  
if (digitalRead(WIO_KEY_A) == LOW && !recording) {

    Serial.println("Starting sampling");
    recording = 1;
    record_ready = false;  
}
#endif

#if defined(WIO_TERMINAL)  
  if (!recording && record_ready)
#elif defined(ARDUINO_ARCH_NRF52840)
  if (record_ready)
#endif  
  {
  Serial.println("Finished sampling");
  
  for (int i = 0; i < SAMPLES; i++) {
    
  //int16_t sample = filter.step(recording_buf[i]);
  int16_t sample = recording_buf[i];
  Serial.println(sample);
  }
  
  record_ready = false; 
  }
}

static void audio_rec_callback(uint16_t *buf, uint32_t buf_len) {
  
  static uint32_t idx = 0;
  // Copy samples from DMA buffer to inference buffer
#if defined(WIO_TERMINAL)
  if (recording) 
#endif
  {
    for (uint32_t i = 0; i < buf_len; i++) {
  
      // Convert 12-bit unsigned ADC value to 16-bit PCM (signed) audio value
#if defined(WIO_TERMINAL)
      recording_buf[idx++] = filter.step((int16_t)(buf[i] - 1024) * 16);
      //recording_buf[idx++] = (int16_t)(buf[i] - 1024) * 16;  
#elif defined(ARDUINO_ARCH_NRF52840)
      recording_buf[idx++] = buf[i];
#endif

      if (idx >= SAMPLES){ 
      idx = 0;
      recording = 0;
      record_ready = true;
      break;
     } 
    }
  }

}
