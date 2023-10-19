from local_robot import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

robot.set_GPS()
robot.set_Gyro()


while robot.step(timestep) != -1:
    print(robot.gpsGetValues())
    print(robot.gyroGetValues())