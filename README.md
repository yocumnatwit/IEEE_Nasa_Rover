# IEEE_Nasa_Rover
For work on the Wentworth Institute of Technology IEEE Nasa Rover

Check branches for specific code snippets/modules/packages.

## Code Usage Examples:

Initializing and using the servo library:

```py
# With no pre-existing servo
from components.servo_lib.slm import servo_lib as srv_lib

servo = srv_lib.Servo_Lib()
# call the init servo command passing it the channel and optionally the frequency
servo.init_servo(0) # create a servo with default frequency 50 and channel 0

servo.rotateTo(90) # rotate the servo to the 90 degrees position
servo.rotateTo(40, 0.05) # rotate the servo to the 40 degrees position with time steps of 0.05 seconds
```
