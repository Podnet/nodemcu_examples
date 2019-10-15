# 06_ESP_TEMPERATURE
To run the program use the following ampy command

##NOTE
The temperature values differ from chip to chip, and the temperature sensor returns a higher value than the room temperature because of the temperature that SoC is operating upon is higher and closer to the sensor. Typically the values are 20 Celsius higher than room temperature.

## MAC OS
```bash
    ampy --port /dev/tty.SLAB_USBtoUART run accesspoint.py
```

## Linux
```bash
    ampy --port /dev/ttyUSB0 run accesspoint.py
```
