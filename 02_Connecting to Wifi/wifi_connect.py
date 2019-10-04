import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect('<Your ESSID>', '<Password>')
        while not sta_if.isconnected():
            pass
    print('Network config:', sta_if.ifconfig())