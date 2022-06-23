'''
Given items 

| items | A | B | C | D |
|-------|---|---|---|---|
| p     | 15| 20| 30| 14|
| wt    |  3|  2| 10|  2|

capacity(m) = 6

optimum solution = [2/3,1,0,1]

'''
from typing import List

items=['A','B','C','D']
weight = [3,2,10,2]
profit = [15,20,30,14]

capacity= 6

items_table= []

# solving continuous knapsack problem using greedy approach
def fractional_knapsack_greedy_solution(items: List[str], profits: List[int] ,weights: List[int], capacity: int)-> List[int]: 
    # calculating profit to wt ratio
    for i, val in enumerate(items):
        ratio = profits[i]/weights[i]
        items_table.append({ 'item': val, 'profit': profits[i], 'weight': weights[i], 'p_to_wt': ratio  })

    # sorting the values 
    items_table.sort(key=lambda item: item.get('p_to_wt'), reverse=True )

    # selecting the items [x-vals]
    x_vals=[]
    for i, val in enumerate(items_table):
        wt = val.get('weight')
        # add to x_vals if the wt is less than or equal to a non-zero capacity
        if (wt <= capacity and capacity >= 0):
            x_vals.append(1)
            capacity -= wt
            continue
        # calculate the fraction required to fit the next item
        x_val_frac = capacity / wt
        # add the frac to x_vals
        x_vals.append(x_val_frac)
        # reduce the capacity
        capacity -= x_val_frac * wt

    return x_vals

print(fractional_knapsack_greedy_solution(
    items=items,
    profits=profit,
    weights=weight,
    capacity=capacity
))














