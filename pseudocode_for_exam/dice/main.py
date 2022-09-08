import random 

def roll_die():
    return random.choice([1,2,3,4,5,6])

def simulate(goal, trials): 
    total = 0
    for _ in range(trials):
        result =''
        for _ in range(len(goal)):
            result += str(roll_die())

        if result == goal: 
            total+=1
            ''' actual probability for 3 rolls = 1/6 * 1/6 * 1/6
                general formula : 1/(6 ^n) 
                '''
    print(f'Actual probability = {round(1/(6**len(goal)),8)}')

    estimation = total/trials
    print(f'Estimated probability = {estimation}')

simulate('55', 10_00_000)
