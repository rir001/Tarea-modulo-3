from controller import Robot
import numpy as np

import matplotlib.image as mpimg


robot = Robot()

timestep = int(robot.getBasicTimeStep())
# timestep = int(32)

motor_l  = robot.getDevice('left wheel motor')
motor_l.setPosition(float("inf"))
motor_l.setPosition(0)

motor_r  = robot.getDevice('right wheel motor')
motor_r.setPosition(float("inf"))
motor_r.setPosition(0)


lidar = robot.getDevice('LDS-01')
lidar.enable(timestep)

compass = robot.getDevice('compass')
compass.enable(timestep)

print(dir(lidar))


scale = 20



center = np.array((10*scale, 10*scale))

while robot.step(timestep) != -1:
    mapa = np.zeros((20*scale, 20*scale))

    # motor_l.setVelocity(3)
    # motor_r.setVelocity(3)

    data = np.array(lidar.getRangeImage()) * scale

    print(compass.getValues())



    comp = compass.getValues()
    ang_base = np.arctan2(comp[1], comp[0]) * 180 / np.pi + 90
    ang_base = 0

    for i in range(data.shape[0]):

        if data[i] != float("inf"):

            angle = np.deg2rad(i * 360 / 240+ ang_base)


            x = int(np.cos(angle) * data[i])
            y = int(np.sin(angle) * data[i])


            mapa[center[1] + y, center[0] + x] = 1

    mpimg.imsave("mapa.png", mapa)





    pass
