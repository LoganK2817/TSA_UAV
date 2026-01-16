from machine import Pin
import time

# Configure GPIO 4 as an input pin with an internal pull-up resistor
# Change '4' to the GPIO number you are using
button_pin = Pin(21, Pin.IN, Pin.PULL_UP)

print("Reading input from GPIO 4...")

while True:
    # Read the current value of the pin (0 or 1)
    # 0 when button is pressed, 1 when released (due to pull-up)
    print(button_pin.value())
        
    # Add a small delay to prevent excessive printing and stabilize readings
    print("--------")
    time.sleep(0.5)
