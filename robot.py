import magicbot
import wpilib
import wpilib.drive

from rev import CANSparkMax, CANSparkLowLevel

from subsystems.iris import Iris
from subsystems.wheels import Wheels

class Robot(magicbot.MagicRobot):
    iris:   Iris   # iris subsystem
    wheels: Wheels # wheels subsystem

    def createObjects(self):
        # device instances
        self.left = CANSparkMax(
            1,
            CANSparkLowLevel.MotorType.kBrushless,
        )
        self.lift = CANSparkMax(
            2,
            CANSparkLowLevel.MotorType.kBrushless,
        )
        self.right = CANSparkMax(
            3,
            CANSparkLowLevel.MotorType.kBrushless,
        )

        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)  

        self.input = wpilib.Joystick(0)
        self.input.setThrottleChannel(1)
        self.input.setTwistChannel(0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        if self.input.getTrigger():
            self.iris.up()

        self.wheels.go(self.input.getThrottle(), self.input.getTwist())

        
           
        