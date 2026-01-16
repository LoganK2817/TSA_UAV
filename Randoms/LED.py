from machine import Pin
from neopixel import NeoPixel
from time import sleep

# Initialize NeoPixel on a specific pin (e.g., GPIO 48 or 38)
# The second argument is the number of LEDs (1 for a single built-in)
np = NeoPixel(Pin(48), 1) # Use Pin(38) if 48 doesn't work [11]

while True:
    np[0] = (10, 0, 0) # Set Red (R, G, B)
    np.write()          # Send data to the LED
    sleep(1)

    np[0] = (0, 10, 0) # Set Green
    np.write()
    sleep(1)

    np[0] = (0, 0, 10) # Set Blue
    np.write()
    sleep(1)

    np[0] = (0, 0, 0) # Turn off (Black)
    np.write()
    sleep(1)
