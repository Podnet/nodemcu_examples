import machine
import time

blue = machine.Pin(14, machine.Pin.OUT)
red = machine.Pin(12, machine.Pin.OUT)
green = machine.Pin(13, machine.Pin.OUT)

while True:
        green.on()
        time.sleep_ms(500)
        green.off()
        blue.on()
        time.sleep_ms(500)
        blue.off()
        red.on()
        time.sleep_ms(500)
        red.off()
        
