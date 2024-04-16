#!/bin/python3
import time
from djitellopy import Tello

def main():
    tello = Tello()

    tello.connect()
    tello.takeoff()
    time.sleep(2)
    tello.rotate_clockwise(225)
    tello.flip_forward()

    tello.land()

if __name__ == "__main__":
    main()
