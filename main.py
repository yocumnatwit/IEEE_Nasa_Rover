# from components.controller_lib.clm import controller_lib as ctrl_lib
from components.motor_lib.mlm import motor_lib as mtr_lib
# from components.servo_lib.slm import servo_lib as srv_lib

import time

import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

"""def servoSetupSteering(channels):
    for channel in channels:
        servo = srv_lib.Servo_Lib()
        servo.init_servo(0, 100)
        servo.setPosition(60)"""


if __name__ == '__main__':
    """servo = srv_lib.Servo_Lib()
    controller = ctrl_lib.Controller()
    servoSetupSteering()
    servo.init_servo(0, 100)
    pressed = False
    while not pressed:
        buttons = controller.readLetterButtons()
        if buttons[0] == 1:
            pressed = True
        sticks = controller.readSticks()
        servo.servo.angle = servo.getAngle + sticks[0]"""
    motor = mtr_lib.Motor_Lib(23, 24, 25)

    motor.control_motor("forward", 50)
    time.sleep(5)
    motor.stop_motor()
    gpio.cleanup()


    
