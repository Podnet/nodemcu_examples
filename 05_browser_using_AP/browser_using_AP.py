import usocket as socket
import network
import machine
import time

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'ESP8266' # Name of your network
password = 'nodeesp8266' # password of your network

# Making NodeMCU Hotspot
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

# Web Template
def web_page():
  html = """<html><head>
  <style>
  .button {
  background-color: black; 
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
}
  </style>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body><h1 style="text-align:center;">The Podnet</h1>
  <h2>Press any button to blink LED of yout choice</h2>
  <a href="colourblink"><button  class="button">Blink All</button></a>
  <a href=”colourred"><button  class="button button3" style="background-color: #f44336;">Red</button></a>
  <a href=”colourpink"><button  class="button button6" style="background-color: pink;">Pink</button></a>
  <a href="colourgreen"><button  class="button" style="background-color: green;">Green</button></a>
  <a href="colourblue"><button class="button button2" style="background-color: blue;">Blue</button></a>
  <a href="colourcyan"><button class="button button8" style="background-color: cyan;">Cyan</button></a>
  </body></html>"""
  return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# Initialization of the pins for different colours
blue = machine.Pin(14, machine.Pin.OUT)
red = machine.Pin(12, machine.Pin.OUT)
green = machine.Pin(13, machine.Pin.OUT)

# Starter blinking to authenticate node is working properly
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

# To continue detecting devices
while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  print("conn = %s" % str(conn))
  str_conn = str(request)
  if "colourred" in str_conn:
    red.on()
    blue.off()
    green.off()
  if "colourblue" in str_conn:
    red.off()
    blue.on()
    green.off()
  if "colourgreen" in str_conn:
    red.off()
    blue.off()
    green.on()
  if "colourpink" in str_conn:
    red.on()
    blue.on()
    green.off()
  if "colouryellow" in str_conn:
    red.on()
    blue.off()
    green.on()
  if "colourcyan" in str_conn:
    red.off()
    blue.on()
    green.on()
  if "colourblink" in str_conn:
    for i in range(5):
      red.off()
      blue.off()
      green.on()
      time.sleep_ms(300)
      green.off()
      red.on()
      blue.on()
      time.sleep_ms(300)
      red.off
      green.off()
      blue.on()
      time.sleep_ms(300)
      blue.off()
      green.on()
      red.on()
      time.sleep_ms(300)
      blue.off()
      green.off()
      red.on()
      time.sleep_ms(300)
      red.off()
      blue.on()
      green.on()
  response = web_page()
  conn.send(response)
  conn.close()
