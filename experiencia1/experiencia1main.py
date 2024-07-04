#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

motora = Motor(Port.A)
motord = Motor(Port.D)

color_sensor = ColorSensor(Port.S4)
SPEED = 150  
while True:
    color=color_sensor.color()
    if color==Color.WHITE:
        motora.stop()
        motord.run(SPEED)
    elif color==Color.BLACK:
        motora.run(SPEED)
        motord.stop()
    else:
        motora.run(SPEED)
        motord.run(SPEED)
    wait(100)