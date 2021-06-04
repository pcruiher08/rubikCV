#include <FastLED.h>

#define LED_PIN     5
#define NUM_LEDS    30

CRGB leds[NUM_LEDS];

void setup() {

  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(4);

}

void loop() {
  for (int i = 0; i <= NUM_LEDS; i++) {
    //if(i!= 21 && i != 20 && i != 19 && i != 18 && i != 7 )
    if(i > 7 && i < 20){
      if(i > 15) FastLED.setBrightness(6);
      if(i != 11 && i!= 12 && i!= 13)
      leds[i] = CRGB ( 255, 255, 255);
    }
    FastLED.show();
    delay(40);
  }
}