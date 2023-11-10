from controller import Robot as base_robot
import numpy as np

class Robot(base_robot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_GPS(self):
        self.gps = self.getDevice('gps')
        self.gps.enable(int(self.getBasicTimeStep()))
        self._desfase_gps = np.random.randint(-100, 100, 3)

    def gpsGetValues(self):
        return np.array(self.gps.getValues()) + self._desfase_gps