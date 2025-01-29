from pion import Spion


drone = Spion(logger=True)
drone.arm()
drone.takeoff()
drone.land()
drone.stop()
