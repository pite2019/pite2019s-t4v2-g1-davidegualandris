from random import gauss
import logging
import time


class Environment:

    def __init__(self, plane):
        self.plane = plane

    def next_simulation(self):
        while True:
            self.plane.adjust()
            turb = gauss(0, 4)
            self.plane.orientation += turb
            if -90 < self.plane.orientation < 90:
                yield self.plane.orientation, turb
                continue
            break

    def __str__(self):
        return self.plane.__str__()


class Plane:

    def __init__(self):
        self.orientation = gauss(0, 9.4868329)

    def adjust(self):
        if -3 <= self.orientation <= 3:
            self.orientation = 0
        else:
            if self.orientation < 0:
                self.orientation += 3
            else:
                self.orientation -= 3

    def __str__(self):
        return "The angle is " + str(self.orientation)


if __name__ == '__main__':

    pln = Plane()

    env = Environment(pln)

    logging.basicConfig(filename='simulation.log', level=logging.DEBUG)

    logging.info(env)

    for sim in env.next_simulation():
        logging.info("After the adjustment, the angle is " + str(sim[0]) + ", the turbolence was " + str(sim[1]))
        time.sleep(2)
    logging.error("Oooooh no, the plane has crashed \n")
