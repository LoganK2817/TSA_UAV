from machine import Pin, PWM
import time

servo = PWM(Pin(14))
servo.freq(50)

print("Starting servo calibration")

# SAFE starting values
duty = 40

try:
    while True:
        servo.duty(duty)
        print("Duty:", duty)
        time.sleep(1)

        cmd = input("Enter duty (+ / - / number / q): ").strip()

        if cmd == "+":
            duty += 5
        elif cmd == "-":
            duty -= 5
        elif cmd.isdigit():
            duty = int(cmd)
        elif cmd.lower() == "q":
            break

        duty = max(25, min(130, duty))

except KeyboardInterrupt:
    pass

servo.deinit()
print("Done")
