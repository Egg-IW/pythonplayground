from random import randint
import numpy as np 
import matplotlib.pyplot as plt

class Simulation:    
    def __init__(self):
        attempts = -1
        while(attempts < 1):
            attempts = GetIntegerInput("How many attempts? ")
        self.attempts = attempts
        self.meanScore = []
        self.count = []

    def Simulate(self):
        for i in range(1, self.attempts):
            scores = []
            
            for _ in range(1, i):
                scores.append(self.RunTurn())

            self.meanScore.append(np.mean(scores))
            self.count.append(i)

        self.DisplayResults()


    def RunTurn(self):
        actual = randint(0,2)
        guess = randint(0,2)

        if actual == guess:
            return 1
        else:
            return 0

    def DisplayResults(self):
        plt.plot(self.count, self.meanScore)
        plt.show()

def GetIntegerInput(message):
    while True:
        try:
            print("")
            choice = int(input(message))
        except ValueError:
            print("Please enter a number")
        else:
            return choice

class SimulationWithSwitching(Simulation):
    def RunTurn(self):
        actual = randint(0,2)
        guess = randint(0,2)

        newGuess = [0,1,2]
        newGuess.remove(guess)

        if newGuess[0] == actual:
            del newGuess[1]
        elif newGuess[1] == actual:
            del newGuess[0]
        else:
            del newGuess[randint(0,len(newGuess))-1]

        guess = newGuess[0]

        if actual == guess:
            return 1
        else:
            return 0
  

def Menu():

    print("")
    print("Monty Hall Simulator")
    print("1) No switching")
    print("2) switching")
    print("3) end simulation")
    print("")

    menuOptions = [1,2,3]
    
    choice = -1

    while(choice not in menuOptions):
        choice = GetIntegerInput("Choose simulation!")

    if choice == 1:
        simulation = Simulation()
    elif choice == 2:
        simulation = SimulationWithSwitching()
    elif choice == 3:
        exit()
    
    simulation.Simulate()

    Menu()  

if __name__ == "__main__":
    Menu()