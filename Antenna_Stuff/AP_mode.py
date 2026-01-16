import network


ap_active = False

# Create access-point interface
ap = network.WLAN(network.AP_IF)

# Configure AP with WPA2 password
ap.config(
    ssid="ESP32-3200",
    password="1203-1003",  # must be at least 8 characters
    authmode=network.AUTH_WPA2_PSK,
    max_clients=2
)

# Activate or deactivate
if ap_active:
    ap.active(True)
    print("--- AP Active ---")
    print("IP:", ap.ifconfig()[0])
else:
    ap.active(False)
    print("--- AP Deactivated ---")
