from pion import Spion
import numpy as np
import time


drone = Spion(logger=True)
drone.set_v()
drone.arm()
drone.takeoff()

drone.t_speed = np.array([1, 0, 0, 0])
time.sleep(6)
drone.land()
drone.stop()
