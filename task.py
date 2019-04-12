#
#Flight simulator.
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
#The program should print out current orientation, and applied tilt correction. 
#The program should run in infinite loop, until user breaks the loop. 
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 

#With every simulation step the orentation should be corrected, applied and printed out.
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.

from random import randint

class FlightSimulator:

#Defining the constructor
    
    def __init__(self):
        self.orientation = randint(0, 90)
        self.disturb = randint(0, 7)

    def adjust(self):
        return randint(self.orientation-self.disturb, self.orientation+self.disturb)

    def __str__(self):
        return "It was " + str(self.orientation) + " angle, with " + str(self.disturb) + " disturbing. After adjusting it is " + str(self.adjust())

if __name__ == '__main__':

    while True:
        choice = input ("Stop? [y]es, any keys for no").strip()
        if choice == 'y':
            break
        sim = FlightSimulator()
        print(sim)
