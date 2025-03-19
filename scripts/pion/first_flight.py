from pion import Pion
import time

# Пример взлета и посадки

def main():
    drone = Pion(ip="10.1.100.217")
    time.sleep(0.5)
    drone.arm()
    time.sleep(0.5)
    drone.takeoff()
    time.sleep(10)
    drone.land()
    time.sleep(7)
    drone.disarm()
    drone.stop()

if __name__ == "__main__":
    main()
