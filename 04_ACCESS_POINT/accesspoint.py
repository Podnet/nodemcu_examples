# Code to make the NodeMCU (ESP8266) an access point, so that other devices can connect to it.

import network

ap = network.WLAN(network.AP_IF)        # Access point interface, this will be used to make the Node into a hotspot.

ap.active(True)     # Activate the Access Point interface.

ap.config(essid="ESSID", password="PASSWORD")       # Replace ESSID with the network name, and PASSWORD with the password for other devices to connect.

print(ap.ifconfig())        # Prints (on Terminal) the IP address, netmask, gateway, DNS.

# The following command returns True if devices are connected to the NodeMCU.
# ap_if.active()