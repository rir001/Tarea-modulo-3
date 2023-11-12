from controller import Robot, Keyboard
import numpy as np



robot = Robot()
timestep = int(robot.getBasicTimeStep())


camera = robot.getDevice('camera')
camera.enable(timestep)
camera.recognitionEnable(timestep)


motor_l  = robot.getDevice('left wheel motor')
motor_l.setPosition(float("inf"))
motor_l.setVelocity(0.0)

motor_r  = robot.getDevice('right wheel motor')
motor_r.setPosition(float("inf"))
motor_r.setVelocity(0.0)


gps = robot.getDevice('gps')
gps.enable(timestep)


keyboard = Keyboard()
keyboard.enable(timestep)



while robot.step(timestep) != -1:

    key=keyboard.getKey()


    if (key == Keyboard.UP):
        motor_l.setVelocity(3)
        motor_r.setVelocity(3)



    if (key == Keyboard.DOWN):
        motor_l.setVelocity(0)
        motor_r.setVelocity(0)


    print(gps.getValues())





    # n = camera.getRecognitionNumberOfObjects()
    # if n > 0:
    #     objects = camera.getRecognitionObjects()
    #     for o in objects:
    #         print(o.getModel())
    #         print(dir(o))

    pass





















































# from controller import Robot, Keyboard
# import numpy as np



# robot = Robot()

# timestep = int(robot.getBasicTimeStep())
# motor_l  = robot.getDevice('left wheel motor')
# motor_l.setPosition(float("inf"))
# motor_l.setVelocity(0.0)

# motor_r  = robot.getDevice('right wheel motor')
# motor_r.setPosition(float("inf"))
# motor_r.setVelocity(0.0)


# lidar = robot.getDevice('LDS-01')
# lidar.enable(timestep)

# compass = robot.getDevice('compass')
# compass.enable(timestep)



# camera = robot.getDevice('camera')
# camera.enable(timestep)
# camera.recognitionEnable(timestep)



# keyboard=Keyboard()
# keyboard.enable(timestep)


# print(dir(camera))

# while robot.step(timestep) != -1:

#     key=keyboard.getKey()
#     if (key==ord(',')):
#         # print("M")
#         motor_l.setVelocity(3)
#         motor_r.setVelocity(3)
#     if (key==ord('O')):
#         # print("M")
#         motor_l.setVelocity(0)
#         motor_r.setVelocity(0)
#     if (key==ord('A')):
#         # print("M")
#         motor_l.setVelocity(-5)
#         motor_r.setVelocity(5)
#     if (key==ord('E')):
#         # print("M")
#         motor_l.setVelocity(5)
#         motor_r.setVelocity(-5)
#     if (key==ord('Q')):
#         # print("M")
#         motor_l.setVelocity(-3)
#         motor_r.setVelocity(-3)

#     # print(camera.getRecognitionNumberOfObjects())
#     # print(dir(camera.getRecognitionObjects()))
#     print(dir(camera.getRecognitionObjects()[0]))
#     print(camera.getRecognitionObjects()[0].getId())
#     print(camera.getRecognitionObjects()[0].getModel())
#     print(list(camera.getRecognitionObjects()[0].getPosition()))
#     print(list(camera.getRecognitionObjects()[0].getSize()))
#     print(list(camera.getRecognitionObjects()[0].getSizeOnImage()))


#     pass
