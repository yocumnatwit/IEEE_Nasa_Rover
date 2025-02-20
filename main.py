from components.controller_lib.clm import controller_lib as ctrl_lib
from components.motor_lib.mlm import motor_lib as mtr_lib
from components.servo_lib.slm import servo_lib as srv_lib

import time

if __name__ == '__main__':
    servo = srv_lib.Servo_Lib()
    controller = ctrl_lib.Controller()
    servo.init_servo(0, 100)
    servo.setPosition(0)
    time.sleep(0.25)