import network
import time

# Define your network credentials
ssid = "Banshee's Cry"
password = "NetW0rking!17"

# Initialize WLAN interface in Station mode (to connect to a router)
wlan = network.WLAN(network.WLAN.IF_STA)
wlan.active(True) # Activate the Wi-Fi interface

print("Scanning for networks...")
# Optional: Scan for networks to see available SSIDs
nets = wlan.scan()
for net in nets: 
    print(f"SSID: {net[0].decode()}, RSSI: {net[2]}")

print(f"Connecting to {ssid}...")
wlan.connect(ssid, password)

# Wait for connection to establish
timeout = 10
while not wlan.isconnected() and timeout > 0:
    time.sleep(1)
    timeout -= 1

if wlan.isconnected():
    print('Connected!')
    print('Network config:', wlan.ifconfig()) # Print IP address, etc.
else:
    print('Failed to connect to Wi-Fi.')

# For Access Point mode:
# ap = network.WLAN(network.WLAN.IF_AP)
# ap.config(essid='MyESP32AP', password='mypassword')
# ap.active(True)
