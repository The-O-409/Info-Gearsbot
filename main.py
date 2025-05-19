#19.May 25

#imports
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)
spkr = Sound()
btn = Button()
radio = Radio()
obtr = ObjectTracker()
gyro_sensor_in1 = GyroSensor(INPUT_1)
gps_sensor_in2 = GPSSensor(INPUT_2)
laser_sensor_in3 = LaserRangeSensor(INPUT_3)
laser_sensor_in4 = LaserRangeSensor(INPUT_4)
laser_sensor_in5 = LaserRangeSensor(INPUT_5)

def angle(gyro,tankDrive):
    tankDrive.on(1,-1)
    while round(gyro.angle % 90) != 0:
        print(round(gyro.angle % 90))
    tankDrive.off()

def driveForward(laserFront,tankDrive):
    tankDrive.on(10,10)
    while laserFront.distance_centimeters < 20:
        pass
    tankDrive.off()

print(gyro_sensor_in1.angle)
tank_drive.on(20,10)
time.sleep(3.5324)
tank_drive.off()
angle(gyro_sensor_in1,tank_drive)

     