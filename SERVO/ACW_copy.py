import utime
import machine

MAP = {0: 30, 180: 130}
# MAP = {0: 1000, 90:4250, 180: 7500}
SERVOPIN = 14
FREQ = 50

class custom_servo:
    def __init__(self, servo_id, map: dict, freq, home_angle=0):
        self.servo = machine.PWM(machine.Pin(SERVOPIN))
        self.servo.freq(freq)
        self.map = map 
        self._current_duty = 0
        self._current_angle = home_angle
        self._set_duty(self._get_duty(home_angle))
        

    def _set_duty(self, duty):
        self.servo.duty_u16(duty)
        self._current_duty = duty
    
    def _get_duty(self, angle):
        set_angles = sorted([i for i in self.map.keys()])

        if angle in set_angles:
            return self.map[angle]

        closest_set_angle_high = None
        closest_set_angle_low = None

        for v in set_angles:
            if v <= angle:
                closest_set_angle_low = v
            elif v > angle and closest_set_angle_high is None:
                closest_set_angle_high = v
                break
        
        if closest_set_angle_high is None:
            closest_set_angle_high = closest_set_angle_low
        if closest_set_angle_low is None:
            closest_set_angle_low = closest_set_angle_high

        if closest_set_angle_high == closest_set_angle_low:
            return self.map[closest_set_angle_low]

        if closest_set_angle_high is None or closest_set_angle_low is None:
            return self.map[closest_set_angle_low] if closest_set_angle_low is not None else self.map[closest_set_angle_high]

        closest_set_duty_low = self.map[closest_set_angle_low]
        closest_set_duty_high = self.map[closest_set_angle_high]

        # closest_set_angle_low
                
        
        magic_percent = (angle - closest_set_angle_low) / (closest_set_angle_high - closest_set_angle_low)
        float_duty = (magic_percent * (closest_set_duty_high-closest_set_duty_low)) + closest_set_duty_low
        return int(round(float_duty))
        # print(closest_set_angle_high, closest_set_angle_low)  

    
    def goto(self, angle, time=0, resolution=50):
        """
        resolution is in steps per second, and decides how many times the servo updates per second
        """
        
        total_steps = time*resolution
        self._current_duty = 0
        end_duty = self._get_duty(angle)
        # print(end_duty)
        time_at_start_of_planing = utime.ticks_ms()

        if time == 0:
            time_at_start_of_stepping = utime.ticks_ms()
            self._set_duty(end_duty)
        else:
            plan = []
            pre_angle = self._current_angle
            rate_of_change = angle/total_steps
            if self._current_angle < angle:
                while pre_angle < angle:
                    pre_angle += rate_of_change
                    plan.append(int(round(self._get_duty(pre_angle))))

            elif self._current_angle > angle:
                while pre_angle > angle:
                    pre_angle -= rate_of_change
                    plan.append(int(round(self._get_duty(pre_angle))))
            
            else:
                print("roc = 0")

            # print(plan)
            sleep_per_tick = round(1000/(resolution))
            # print(sleep_per_tick, "<<")
            # print(len(plan))

            time_at_start_of_stepping = utime.ticks_ms()

            for step in plan:
                # print(step)
                self._set_duty(step)
                utime.sleep_ms(sleep_per_tick)
            
            
            plan = [] #clean memory
            self._set_duty(end_duty)

        self._current_angle = angle
        time_at_finish = utime.ticks_ms()
        return (utime.ticks_diff(time_at_start_of_stepping, time_at_start_of_planing)/1000, utime.ticks_diff(time_at_finish, time_at_start_of_stepping)/1000)


if __name__ == "__main__":
    s1 = custom_servo(
        servo_id=SERVOPIN,
        map=MAP,
        freq=FREQ,
        home_angle=0
    )
    utime.sleep(4)

    print(s1.goto(180, time=10, resolution=200))
    


