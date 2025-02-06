import time

import board

from adafruit_motor import servo

from adafruit_pca9685 import PCA9685

class Servo_Lib:
    
    def __init__(self, servoObj):
        self.servo = servoObj

    def rotateTo(self, pos_deg, step_delay=0.03):
        """
        Rotate the servo to a specific position in degrees.
        step_delay: Time delay between each step of rotation default 0.03 seconds.
        """
        if pos_deg > 180:
            raise ValueError("Desired position greater than 180!")
        elif pos_deg < 0:
            raise ValueError("Desired position less than 0!")

        servo = self.servo
        starting_angle = servo.angle
        delta = pos_deg - starting_angle
        step = 1

        if delta < 0:
            delta = starting_angle - pos_deg
            step = -1
        elif delta == 0:
            return

        for i in range(abs(delta)):
            servo.angle = starting_angle + (i * step)
            time.sleep(step_delay)

    def self_destruct(self):
        del self

    
