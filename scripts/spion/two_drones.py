from pion import Spion


drone1 = Spion(logger=True)
drone2 = Spion(logger=True)
drone1.arm()
drone2.arm()
drone1.takeoff()
drone2.takeoff()
drone1.land()
drone2.land()
drone1.stop()
drone2.stop()
