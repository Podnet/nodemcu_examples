import machine, time

led = machine.Pin(2, machine.Pin.OUT)

for i in range(20):
        led.off()
        time.sleep_ms(500)
        led.on()
        time.sleep_ms(500)
