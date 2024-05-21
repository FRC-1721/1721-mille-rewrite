from rev import CANSparkMax

class Iris:
    lift: CANSparkMax

    def __init__(self):
        self.state = None

    def up(self):
        self.state = True
    def down(self):
        self.state = False

    def execute(self):
        if self.state is True:
            self.lift_motor.set(.1)
        elif self.state is False:
            self.lift_motor.set(-.1)

        self.state = None
