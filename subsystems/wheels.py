import wpilib
import wpilib.drive
from rev import CANSparkMax

class Wheels:
    drive: wpilib.drive.DifferentialDrive

    def __init__(self):
        self.speed = 0
        self.rot   = 0

    def go(self, speed, rot):
        self.speed = speed
        self.rot   = rot

    def stop(self):
        self.speed = 0
        self.rot   = 0

    def execute(self):
        self.drive.tankDrive(self.speed * .5, self.rot * .5)
        
        wpilib.SmartDashboard.putNumber("speed", self.speed)
        wpilib.SmartDashboard.putNumber("rot",   self.rot)
