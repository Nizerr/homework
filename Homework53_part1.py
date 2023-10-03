class Printer:
    def does(self):
        return 'print'

class Lamp:
    def does(self):
        return 'glow'

class Car:
    def does(self):
        return 'ride'

class Robot:
    def __init__(self):
        self.printer = Printer()
        self.lamp = Lamp()
        self.car = Car()

    def do_it(self):
        actions = [
            self.printer.does(),
            self.lamp.does(),
            self.car.does()
        ]
        print(",".join(actions))

robot = Robot()
robot.do_it()