# LED_Sync_With_ESP32_and_Alexa


# 1. Hardware Overview
 - ESP32: Main controller (better than Arduino Uno for WiFi & smart features)
 - WS2812B LEDs: Addressable RGB LEDs
 - Power Supply: Ensure you have a 5V supply with enough amperage (e.g., 5V 10A for long strips)
 - Microphone Module: For music-reactive mode (e.g., MAX9814, KY-037)
Level Shifter (optional): For reliable data signal from ESP32 to WS2812B


# Software Overview

## Library Used:
    - [1] FastLED or Adafruit NeoPixel for LED control
    - [2] ESPAsyncWebServer for web interface
    - [3] ArduinoJson for Alexa integration
    - [4] fauxmoESP for Alexa emulation
    - [5] FFT library for music-reactive mode