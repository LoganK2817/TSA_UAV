from machine import Pin
from neopixel import NeoPixel
from time import sleep
import network
 
np = NeoPixel(Pin(48), 1) # Initialize NeoPixel on a specific pin (e.g., GPIO 48 or 38) The second argument is the number of LEDs (1 for a single built-in)
volt = Pin(21, Pin.OUT) # Initialize Pin #21 for Output
wlan = network.WLAN(network.WLAN.IF_STA) # Initialize 'wlan' for network usage
ap = network.WLAN(network.WLAN.IF_AP) # Create access-point interface

def LED():
    print("TESTING LED")
    np[0] = (10, 0, 0) # Set Red (R, G, B)
    np.write()          # Send data to the LED
    sleep(.5)

    np[0] = (0, 10, 0) # Set Green
    np.write()
    sleep(.5)

    np[0] = (0, 0, 10) # Set Blue
    np.write()
    sleep(.5)

    np[0] = (0, 0, 0) # Turn off (Black)
    np.write()

def VOLT():
    print("TESTING PIN #21")
    volt.on()
    sleep(5)
    volt.off()

def CHECK_LAN():
    print("TEST CLIENT CONNECTION")
    if wlan.isconnected():
        print("NETWORK CONNECTED")
        print("NetConfig:", wlan.ifconfig())
    else:
        print("NETWORK NOT CONNECTED")
        
    print("TEST AP CONNECTION")
    if ap.isconnected():
        print("NETWORK CONNECTED")
        print("NetConfig:", ap.ifconfig())
    else:
        print("NETWORK NOT CONNECTED")
    

    
def main():
    LED()
    # VOLT()
    # CHECK_LAN()

main()