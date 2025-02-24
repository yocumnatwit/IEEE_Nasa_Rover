import time

import board

from adafruit_motor import servo

from adafruit_pca9685 import PCA9685

class Servo_Lib:
    
    def __init__(self, servoObj=None):
        if servoObj is not None:
            self.servo = servoObj
            self.pca = None
        else:
            print("Warning: no servo obj provided!")
            print("Please use init_servo before proceeding!")
            pass

    def init_servo(self, channel, frequency=50):
        """
        Create a servo object on a channel
        frequency: the frequency at which to operate the servo. Default: is 50
        """
        if channel > 7 or channel < 0:
            raise ValueError("Invalid channel!")
        if frequency <= 0 or frequency > 100:
            raise ValueError("Invalid frequency!")
        i2c = board.I2C()
        self.pca = PCA9685(i2c)
        self.pca.frequency = frequency
        self.servo = servo.Servo(self.pca.channels[channel])
        ##self.servo.angle = 0


    def rotateTo(self, pos_deg, step_delay=0.03):
        """
        Rotate the servo to a specific position in degrees.
        step_delay: Time delay between each step of rotation default 0.03 seconds.
        """

        servo = self.servo
        starting_angle = servo.angle
        delta = pos_deg - starting_angle
        step = 1

        if delta < 0:
            delta = starting_angle - pos_deg
            step = -1
        elif delta == 0:
            return

        for i in range(abs(int(delta))):
            servo.angle = starting_angle + (i * step)
            time.sleep(step_delay)

    def setPosition(self, pos_deg):
        self.servo.angle = pos_deg

    def getAngle(self):
        return self.servo.angle

    def self_destruct(self):
        if self.pca is not None:
            self.pca.deinit()
        del self

    
