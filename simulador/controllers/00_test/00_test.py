from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

motor_l  = robot.getDevice('left wheel motor')
motor_l.setPosition(float("inf"))

motor_r  = robot.getDevice('right wheel motor')
motor_r.setPosition(float("inf"))


lidar = robot.getDevice('LDS-01')
lidar.enable(timestep)



print(dir(lidar))


while robot.step(timestep) != -1:

    motor_l.setVelocity(3)
    motor_r.setVelocity(3)

    # print(lidar.getRangeImage())


    pass
