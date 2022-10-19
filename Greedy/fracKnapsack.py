'''

Joe Zoll | 10/19/22

Intention: Programmtically create the abstract explanation of the fractional knapsack problem from TechWithTim's
'Greedy Algorithms Explained' YouTube video [URL :: https://youtu.be/lfQvPHGtu6Q].

MY UNIQUE SOLUTION:

We are traveling with a knapsack that has a capacity C
Say we found treasure (i items) each with a value (v_i).
How do we pick the best items that maximize our total value AND fit into our backpack? 
                            (Σ weights <= C)
'''

myTreasure = [(22,19), (10,9), (9,9), (7,6)]
northFaceCapacity = 25
def seizeTreasure(treasure, capacity):
    res = 0
    C = capacity
    weights = [w for (w,v) in treasure]
    values = [v for (w,v) in treasure]
    VperW = [v/w for (w,v) in treasure]

    # Greedy Algorithm:
    #   1) Choose optimal solution via greedy criteria 
    #   2) Update our situation unti we cannot keep moving forward
    #   aka:
    #   1) Choose max value/weight proportion (item i)
    #   2) Decrement w[i] from C, updating how much left we can fit into our knapsack

    while C > 0:
        bestItem = 0
        for i in range(1, len(VperW)):
            if VperW[i] >= VperW[bestItem]:
                bestItem = i

        # if fraction is needed, extract it out
        # otherwise, use given weights and values
        
        if C - weights[bestItem] < 0:
            frac = C / weights[bestItem]
            oldVal = values[bestItem]
            v = oldVal * frac
            w = C
        else:
            v = values[bestItem]
            w = weights[bestItem]

        res += v
        C -= w
        del weights[bestItem]
        del values[bestItem]
        del VperW[bestItem]
    
    return res
        
print(seizeTreasure(myTreasure, northFaceCapacity))