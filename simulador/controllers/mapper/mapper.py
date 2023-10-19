from parameters import WIDTH, HEIGHT, SCALE, BLACK, WHITE
from controller import Robot, CameraRecognitionObject
from functions import cloud_to_points
import pygame as pg
import numpy as np


import matplotlib.image as mpimg



class Turtle(Robot):

    def __init__(self):
        super().__init__()
        self.run = True

        self.im = np.zeros((420, 420, 3), dtype=np.uint8)

        self.window = pg.display.set_mode((WIDTH, HEIGHT))

        print(self.getBasicTimeStep())
        self.timeStep = int(self.getBasicTimeStep())
        print(self.timeStep)
        print(self.getBasicTimeStep())
        self.timeStep = 1
        print(self.timeStep)
        print(self.getBasicTimeStep())
        self.step(self.timeStep)
        print(self.timeStep)
        print(self.getBasicTimeStep())
        print(dir(self))

        self.L = self.getDevice("left wheel motor")
        self.L.setPosition(float("inf"))
        self.L.setVelocity(0)
        self.R = self.getDevice("right wheel motor")
        self.R.setPosition(float("inf"))
        self.R.setVelocity(0)


        self.lidar = self.getDevice("LDS-01")
        self.lidar.enable(self.timeStep)

        self.lidar_m1 = self.getDevice("LDS-01_main_motor")
        self.lidar_m2 = self.getDevice("LDS-01_secondary_motor")
        self.lidar_m1.setPosition(float("inf"))
        self.lidar_m2.setPosition(float("inf"))
        self.lidar_m1.setVelocity(30)
        self.lidar_m2.setVelocity(60)


        self.accelerometer = self.getDevice("accelerometer")
        self.accelerometer.enable(self.timeStep)

        self.compass = self.getDevice("compass")
        self.compass.enable(self.timeStep)

        self.gyro = self.getDevice("gyro")
        self.gyro.enable(self.timeStep)

        self.gps = self.getDevice("gps")
        self.gps.enable(self.timeStep)

        self.camera = self.getDevice("camera")
        self.camera.enable(self.timeStep)
        self.camera.recognitionEnable(self.timeStep)



    @property
    def X(self):
        return self.gps.getValues()[0]

    @property
    def Y(self):
        return self.gps.getValues()[1]

    @property
    def ANGLE(self):
        comp = self.compass.getValues()
        return np.arctan2(comp[1], comp[0]) * 180 / np.pi + 90

    @property
    def IMAGE(self):
        return np.array(self.camera.getImageArray())

    @property
    def xy_distance(self):
        data = self.lidar.getRangeImage()
        return data[::int(len(data)/4)]

    def start(self):
        self.auto = 0
        self.window.fill(WHITE)
        while self.run and self.step(self.timeStep) != -1:
            for event in pg.event.get():
                if event.type in [pg.QUIT, pg.K_ESCAPE]:
                    self.run = False
                if event.type == pg.KEYDOWN:

                    if event.key == pg.K_LEFT:
                        self.L.setVelocity(-5)
                        self.R.setVelocity(5)

                    if event.key == pg.K_RIGHT:
                        self.L.setVelocity(5)
                        self.R.setVelocity(-5)

                    if event.key == pg.K_UP:
                        self.L.setVelocity(6)
                        self.R.setVelocity(6)

                    if event.key == pg.K_DOWN:
                        self.L.setVelocity(-6)
                        self.R.setVelocity(-6)

                    if event.key == pg.K_SPACE:
                        self.L.setVelocity(0)
                        self.R.setVelocity(0)

                    if event.key == pg.K_a:
                        self.window.fill(WHITE)

            if self.xy_distance[0] < 0.15:
                self.auto = 1
                self.L.setVelocity(3)
                self.R.setVelocity(3)
            elif self.xy_distance[2] < 0.13:
                self.auto = 1
                self.L.setVelocity(-3)
                self.R.setVelocity(-3)
            elif self.xy_distance[1] < 0.14:
                self.auto = 1
                self.L.setVelocity(3)
                self.R.setVelocity(-3)
            elif self.xy_distance[3] < 0.14:
                self.auto = 1
                self.L.setVelocity(-3)
                self.R.setVelocity(3)
            elif self.auto == 1:
                self.auto = 0
                self.L.setVelocity(0)
                self.R.setVelocity(0)




            x, y = self.X, self.Y
            pg.draw.circle(self.window, (125, 125, 255), center=[int(WIDTH/2)+x*SCALE, int(HEIGHT/2)-y*SCALE], radius=2)
            cloud = self.lidar.getRangeImage()
            im =  cloud_to_points(cloud, self.ANGLE)
            for n in im:
                pg.draw.circle(self.window, BLACK, center=n+[int(WIDTH/2), int(HEIGHT/2)]+[x*SCALE,-y*SCALE], radius=2)
                for s in np.arange(0, 1, 0.05):
                    self.im[200 + int(40 * (s*n[1] / SCALE - y))][200 + int(40 * (s*n[0] / SCALE + x))] = 122
                self.im[200 + int(40 * (n[1] / SCALE - y))][200 + int(40 * (n[0] / SCALE + x))] = 255
            mpimg.imsave(f"map.png", self.im, cmap='gray')

            pg.display.update()





robot = Turtle()

robot.start()
