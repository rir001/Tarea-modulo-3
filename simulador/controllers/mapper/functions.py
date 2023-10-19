from parameters import SCALE
import numpy as np

def cloud_to_points(cloud:list[int], angle:int) -> list[list[int]]:
    points = []
    step = 360/len(cloud)
    for n in range(0, len(cloud)):
        if cloud[n] < 1.5:
            x = np.cos((n*step+angle)*np.pi/180) * cloud[n] * SCALE
            y = np.sin((n*step+angle)*np.pi/180) * cloud[n] * SCALE
            points.append([x, y])

    return np.array(points, dtype=int)