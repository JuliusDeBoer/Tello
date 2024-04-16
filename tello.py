#!/bin/python3
from djitellopy import Tello

def main():
    tello = Tello()

    tello.connect()
    tello.takeoff()

    tello.move_left(100)
    tello.rotate_counter_clockwise(90)
    tello.move_forward(100)

    tello.land()

if __name__ == "__main__":
    main()
