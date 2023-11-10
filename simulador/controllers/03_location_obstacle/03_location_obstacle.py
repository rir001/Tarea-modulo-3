from local_robot import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

robot.set_GPS()


while robot.step(timestep) != -1:
    print(robot.gpsGetValues())