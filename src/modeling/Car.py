import numpy as np

class Car:
    x: float
    y: float
    yaw: float
    velocity: float = 0.0
    steer: float = 0.0

    def __init__(self, x: float, y: float, yaw: float):
        self.x = x
        self.y = y
        self.yaw = yaw
        