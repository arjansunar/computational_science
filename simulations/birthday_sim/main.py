import math
import random

'''
    Returns if there are at least numSame people with the same birthday
'''
def isSameDate(numPeople, numSame):
    # possible dates
    possibleDates = range(366)
    # list of birthday dates
    birthdays = [0] * 366     

    for _ in range(numPeople):
        # generate random date
        birthDate = random.choice(possibleDates)
        birthdays[birthDate] += 1
    return max(birthdays) >= numSame

def birthdayProblem(numPeople, numSame, numTrials): 
    num_of_same_birthday = 0
    for _ in range(numTrials):
        if isSameDate(numPeople, numSame):
            num_of_same_birthday += 1
    return num_of_same_birthday / numTrials

def birthDaySimulation(list_of_people=[10,20,40,100], num_of_trials=100):
    for numPeople in list_of_people:
        print(f'For {numPeople},  est. probability is {birthdayProblem(numPeople,2, num_of_trials)}')
        numerator = math.factorial(366)
        denom = (366**numPeople) * math.factorial(366-numPeople)
        print(f'Actual prob. 2 people to have same birthday in {numPeople} is {1- numerator/denom}')

birthDaySimulation()