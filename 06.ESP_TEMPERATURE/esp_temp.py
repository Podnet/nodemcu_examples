# This program will run only on ESP32 boards. This program reads the internal temperature sensor readings on the ESP32.

import esp32
import time
for i in range(50):
    F = esp32.raw_temperature()
    print("Temperature in Fahrenheit =",F)
    C = (F-32) * (5/9)
    print("Temperature in Celsius =",C)
    time.sleep(0.5)
