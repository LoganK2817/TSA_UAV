from machine import Pin, PWM
import time
from neopixel import NeoPixel


servo_pin = Pin(14)
servo_pwm = PWM(servo_pin)
servo_pwm.freq(50)
DUTY_MIN = 30
DUTY_MAX = 130

np = NeoPixel(Pin(48), 1) # Initialize NeoPixel on a specific pin (e.g., GPIO 48 or 38) The second argument is the number of LEDs (1 for a single built-in)


desired_angle = 180; #Angle to hit
desired_time = 2.5; #Time to Run


def set_servo_angle(angle):
    angle = max(0, min(180, angle))
    duty = int(DUTY_MIN + (angle / 180) * (DUTY_MAX - DUTY_MIN))
    servo_pwm.duty(duty)
    #print("Angle:", angle, "Duty:", duty)
    
def calculate_Delay(degress,seconds):
    return seconds / degress

def rest_servo():
    np[0] = (10, 0, 0) # Set Red (R, G, B)
    np.write()   # Send data to the LED
    
    set_servo_angle(0)
    print("Rest Pause...")
    time.sleep(2.5)
    
    np[0] = (10, 3, 0) # Set Red (R, G, B)
    np.write()   # Send data to the LED
    print("STARTING...")
    time.sleep(4)
    np[0] = (0, 10, 0) # Set Red (R, G, B)
    np.write()  # Send data to the LED

Time_delay = calculate_Delay(desired_angle,desired_time)

while True:
    rest_servo()
    servo_angle = 0
    print("Current Time Delay: ",Time_delay)
    while servo_angle != desired_angle:
        servo_angle += 1
        #print("Angle",servo_angle)
        set_servo_angle(servo_angle)
        time.sleep(Time_delay)
    break

np[0] = (10, 0, 0) # Set Red (R, G, B)
np.write()          # Send data to the LED