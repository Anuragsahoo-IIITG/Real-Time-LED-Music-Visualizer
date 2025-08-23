#include <Adafruit_NeoPixel.h>

#define LED_PIN    5        // Pin connected to DIN of WS2812B
#define NUM_LEDS   300       // Set to your number of LEDs

Adafruit_NeoPixel strip(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(115200);     // Must match Python
  strip.begin();
  strip.show();             // Clear all LEDs
}

void loop() {
  if (Serial.available() >= 3) {
    int r = Serial.read();
    int g = Serial.read();
    int b = Serial.read();

    for (int i = 0; i < NUM_LEDS; i++) {
      strip.setPixelColor(i, strip.Color(r, g, b));
    }
    strip.show();
  }
}

