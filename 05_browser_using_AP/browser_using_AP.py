import usocket as socket
from machine import UART

uart = UART(0, 115200)                         # init with given baudrate
uart.init(115200, bits=8, parity=None, stop=1) # init with given parameters
import network
import machine
import time

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'ESP8266'
password = 'nodeesp8266'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body><h1>Hello, World!</h1>
  <a href=”red"><button>RED</button></a>
  <a href="green"><button>Green</button></a>
  <a href="blue"><button>Blue</button></a>
  </body></html>"""
  return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

blue = machine.Pin(14, machine.Pin.OUT)
red = machine.Pin(12, machine.Pin.OUT)
green = machine.Pin(13, machine.Pin.OUT)

for i in range(2):
        green.on()
        time.sleep_ms(500)
        green.off()
        blue.on()
        time.sleep_ms(500)
        blue.off()
        red.on()
        time.sleep_ms(500)
        red.off()
while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  print("conn = %s" % str(conn))
  str_conn = str(request)
  if "red" in str_conn:
    red.on()
    blue.off()
    green.off()
  if "blue" in str_conn:
    red.off()
    blue.on()
    green.off()
  if "green" in str_conn:
    red.off()
    blue.off()
    green.on()
  response = web_page()
  conn.send(response)
  conn.close()
