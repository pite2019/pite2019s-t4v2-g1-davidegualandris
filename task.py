from random import gauss
import logging
import time


# class for handle the Environment
class Environment:

    # defining the constructor
    def __init__(self, plane):
        # TODO: more than one plane in the environment
        self.plane = plane  # the environment contains the plane

    # generator to use the simulate one step
    # we are considering that the pilot adjust the plane and then a turbolence arrive\
    # basically he is not expecting the turbolence
    def next_simulation(self):
        while True:
            self.plane.adjust()
            turb = gauss(0, 4)
            self.plane.orientation += turb
            if -90 < self.plane.orientation < 90:
                yield self.plane.orientation, turb
                continue
            break

    # function to print the environment
    def __str__(self):
        return self.plane.__str__()


# class for handle the Plane
# the orientation of the plane
class Plane:

    # defining the constructor
    def __init__(self):
        self.orientation = gauss(0, 9.4868329)  # orientation of the plane is between -90 and 90

    # the pilot is trying to adjust the airplane
    def adjust(self):
        # at every step, the angle could be adjusted of maximum 3 degrees by the pilot
        # because the sigma for the disturbance is 4
        if -3 <= self.orientation <= 3:
            self.orientation = 0
        else:
            if self.orientation < 0:
                self.orientation += 3
            else:
                self.orientation -= 3

    # function to print the environment
    def __str__(self):
        return "The angle is " + str(self.orientation)


if __name__ == '__main__':

    # create the plane
    pln = Plane()

    # create the environment
    env = Environment(pln)

    logging.basicConfig(filename='simulation.log', level=logging.DEBUG)

    logging.info(env)

    # iterate the simulations
    for sim in env.next_simulation():
        logging.info("After the adjustment, the angle is " + str(sim[0]) + ", the turbolence was " + str(sim[1]))
        time.sleep(2)
    logging.error("Oooooh no, the plane has crashed \n")
