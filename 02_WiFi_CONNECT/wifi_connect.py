# Code to connect the NodeMCU (ESP8266) to a WiFi network.

import network      # The network module is used to configure the WiFi connection. 

sta_if = network.WLAN(network.STA_IF)   # Station interface.
ap_if = network.WLAN(network.AP_IF)     # Access point interface.

# Checking if interfaces are active. 
"""
Upon a fresh install the ESP8266 is configured in access point mode, so ap_if interface is active and sta_if interface is inactive.
"""
print(sta_if.active())         # Prints (on Terminal) FALSE.
print(ap_if.active())          # Prints (on Terminal) TRUE.

sta_if.active(True)     # Activate the station interface.

sta_if.connect('ESSID', 'PASSWORD')  # Replace ESSID with the network name, and PASSWORD with the password for the network.


print(sta_if.isconnected())     # Prints (on Terminal) TRUE if connection is established properly.

print(sta_if.ifconfig())        # Prints (on Terminal) the IP address, netmask, gateway, DNS.

ap_if.active(False)           # To disable the access point when not in use.