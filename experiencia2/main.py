#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
md = Motor(Port.D)
mi = Motor(Port.A)
robot = DriveBase(mi,md,55.5,104)

color_sensor = ColorSensor(Port.S4)

while True:
    color = color_sensor.color()

    if color == Color.BLACK: 
        md.run(speed=90)
        mi.run(speed=300)
    else:
        md.run(speed=300)
        mi.run(speed=90)
        wait(10)
