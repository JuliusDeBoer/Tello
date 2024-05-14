#!/bin/python3
import time
from djitellopy import Tello
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    tello = Tello()

    tello.connect()
    tello.takeoff()
    time.sleep(2)
    tello.rotate_clockwise(225)
    tello.flip_forward()

    tello.land()
    print("Ran the code!")
    return "Organs have been traded!"
