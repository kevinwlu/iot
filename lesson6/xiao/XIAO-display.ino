#include <Arduino.h>
#include <U8x8lib.h>
 
// U8X8_SSD1306_128X64_NONAME_HW_I2C u8x8(/* reset=*/ U8X8_PIN_NONE);
 U8X8_SSD1306_64X48_ER_HW_I2C u8x8(/* reset=*/ U8X8_PIN_NONE); 
// U8X8_SSD1306_64X32_NONAME_HW_I2C u8x8(/* reset=*/ U8X8_PIN_NONE);
 
// U8X8_SSD1306_128X64_NONAME_SW_I2C u8x8(/* clock=*/ SCL, /* data=*/ SDA, /* reset=*/ U8X8_PIN_NONE);   // OLEDs without Reset of the Display
 
void setup(void) {
  u8x8.begin();
  //u8x8.setFlipMode(2);   // set number from 1 to 3, the screen word will rotary 180
}
 
void loop(void) {
      u8x8.setFont(u8x8_font_amstrad_cpc_extended_r);
      u8x8.drawString(0,0,"idle");
      u8x8.drawString(0,1,"left");
      u8x8.drawString(0,2,"right");
      u8x8.drawString(0,3,"up&down");   
} 
