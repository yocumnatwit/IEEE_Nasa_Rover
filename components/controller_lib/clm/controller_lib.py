from inputs import get_gamepad
import math
import threading
import time 

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()


    def read(self): 
        """
        Currently Does nothing
        """
        pass
 
    def __readSticksRaw(self):
        """
        Read with no processing in order of x/y Left x/y Right
        """
        xL = self.LeftJoystickX
        yL = self.LeftJoystickY
        xR = self.RightJoystickX
        xL = self.RightJoystickY
        return [xL, yL, xR, xL]
    
    def __normalizeLeft(self):
        """
        Read and normalize left values (sticks)
        """
        sticks = self.__readSticksRaw(self)
        if math.fabs(sticks[0] * 100) <= 40:
            xL = 0
        elif sticks[0] > 0:
            xL = math.floor(sticks[0] * 100) - 40
        else:
            xL = math.floor(sticks[0] * 100) + 40  

        if math.fabs(sticks[1] * -100) <= 20:
            yL = 0
        elif sticks[1] > 0:
            yL = math.floor(sticks[1] * -100) - 20
        else:
            yL = math.floor(sticks[1] * -100) + 20  

        return [xL, yL]
    
        
    def __normalizeRight(self):
        """
        Read and normalize right values (sticks)
        """
        sticks = self.__readSticksRaw(self)
        if math.fabs(sticks[2] * 100) <= 40:
            xR = 0
        elif sticks[0] > 0:
            xR = math.floor(sticks[2] * 100) - 40
        else:
            xR = math.floor(sticks[2] * 100) + 40  

        if math.fabs(sticks[3] * -100) <= 20:
            yR = 0
        elif sticks[3] > 0:
            yR = math.floor(sticks[3] * -100) - 20
        else:
            yR = math.floor(sticks[3] * -100) + 20  

        return [xR, yR]

    def readSticks(self):
        """
        Read sticks with corrected values
        """
        xL, yL = self.__normalizeLeft(self)
        xR, yR = self.__normalizeRight(self)
        return [xL, yL, xR, yR]

    def zeroSticks(self):
        self.LeftJoystickX = 0
        self.LeftJoystickY = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0

    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.Y = event.state #previously switched with X
                elif event.code == 'BTN_WEST':
                    self.X = event.state #previously switched with Y
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state