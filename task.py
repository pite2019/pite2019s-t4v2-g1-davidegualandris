from random import randint


class FlightSimulator:

    # defining the constructor
    def __init__(self):
        self.orientation = randint(-90, 90)  # orientation of the plane, the goal is to reach 0

    # we are considering that the pilot adjust the plane and then a turbolence arrive\
    # basically he is not expecting the turbolence
    def adjust(self):

        # at every step, the angle could be adjusted of maximum 10 degrees by the pilot
        if -10 <= self.orientation <= 10:
            self.orientation = 0
        else:
            if self.orientation < 0:
                self.orientation += 10
            else:
                self.orientation -= 10

        # the turbolence is between -10 and 10 degrees
        turb = randint(-10, 10)
        self.orientation += turb

        return self.orientation, turb

    def __str__(self):
        return "The angle is " + str(self.orientation)


if __name__ == '__main__':

    fs = FlightSimulator()
    print(fs)

    while True:
        if input("Stop? [y]es, any other keys for no").strip() == 'y':
            break
        res = fs.adjust()
        print("After the adjustment, the angle is " + str(res[0]) + ", the turbolence was " + str(res[1]))
