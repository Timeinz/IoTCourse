#def do_connect():
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
f = open('secret.txt', 'r')
ssid = f.readline()
ssid = ssid.strip()
password = f.readline()
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect(ssid, password)
while not wlan.isconnected():
    pass
print('network config:', wlan.ifconfig())