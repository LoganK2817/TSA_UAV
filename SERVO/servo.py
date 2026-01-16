from machine import Pin, PWM
import time

servo_pin = Pin(14)
servo_pwm = PWM(servo_pin)
servo_pwm.freq(50)

DUTY_MIN = 30
DUTY_MAX = 130



desired_angle = 180; #Angle to hit
desired_time = 5; #Time to Run


def set_servo_angle(angle):
    angle = max(0, min(180, angle))
    duty = int(DUTY_MIN + (angle / 180) * (DUTY_MAX - DUTY_MIN))
    servo_pwm.duty(duty)
    #print("Angle:", angle, "Duty:", duty)
    
def calculate_Delay(degress,seconds):
    return seconds / degress

def rest_servo():

    set_servo_angle(0)
    print("Rest Pause...")
    # time.sleep(2.5)
    print("STARTING...")
    time.sleep(4)

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
