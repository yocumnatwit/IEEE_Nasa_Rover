import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Motor_Lib:

    def __init__(self, enable_pin, in1_pin, in2_pin, frequency=1000):
        """
        Create a single motor object
        """
        self.enable_pin = enable_pin
        self.in1_pin = in1_pin
        self.in2_pin = in2_pin

        self.pwm = GPIO.PWM(self.enable_pin, frequency)
        self.pwm.start(0)

    def __TL(translateable):
        """
        Translate high or low into GPIO sets
        """
        match translateable:
            case 'HIGH':
                return GPIO.HIGH
            case 'LOW':
                return GPIO.HIGH
            case _:
                raise ValueError("unknown input to translation function")

    def control_motor(self, direction, speed):
        """
        """
        if direction == "forward":
            GPIO.output(self.in1_pin, self.__TL('HIGH'))
            GPIO.output(self.in2_pin, self.__TL('LOW'))
        elif direction == "backward":
            GPIO.output(self.in1_pin, self.__TL('LOW'))
            GPIO.output(self.in2_pin, self.__TL('HIGH'))
        else:
            raise ValueError("Invalid direction. Use 'forward' or 'backward'.")

        self.pwm.ChangeDutyCycle(speed)

    def stop_motor(self):
        self.pwm.ChangeDutyCycle(0)

    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()
    
    def self_destruct(self):
        self.cleanup()
        del self
        