import time
import RPi.GPIO as gpio

class Motor_Lib:
    

    def __init__(self, enable_pin, in1_pin, in2_pin, frequency=1000):
        """
        Create a single motor object
        """
        gpio.setmode(gpio.BCM)
        self.enable_pin = enable_pin
        self.in1_pin = in1_pin
        self.in2_pin = in2_pin

        gpio.setup(enable_pin, gpio.OUT)
        gpio.setup(in1_pin, gpio.OUT)
        gpio.setup(in2_pin, gpio.OUT)

        self.pwm = gpio.PWM(self.enable_pin, frequency)
        self.pwm.start(0)

    def __TL(self, translateable):
        """
        Translate high or low into gpio sets
        """
        match translateable:
            case 'HIGH':
                return gpio.HIGH
            case 'LOW':
                return gpio.LOW  # Corrected from gpio.HIGH to gpio.LOW
            case _:
                raise ValueError("unknown input to translation function")

    def control_motor(self, direction, speed):
        """
        Control motor direction and speed
        """
        if direction == "forward":
            gpio.output(self.in1_pin, self.__TL('HIGH'))
            gpio.output(self.in2_pin, self.__TL('LOW'))
        elif direction == "backward":
            gpio.output(self.in1_pin, self.__TL('LOW'))
            gpio.output(self.in2_pin, self.__TL('HIGH'))
        else:
            raise ValueError("Invalid direction. Use 'forward' or 'backward'.")

        self.pwm.ChangeDutyCycle(speed)

    def stop_motor(self):
        self.pwm.ChangeDutyCycle(0)

    def cleanup(self):
        self.pwm.stop()
        gpio.cleanup()
    
    def self_destruct(self):
        self.cleanup()
        del self


class Drive_Lib:
    def __init__(self):
        pass
