# TheShlock 2022
"""Returns the total implied probability of the event
a bet function is returned that takes a stake amount and computes the respective bet on each outcome
{"name_of_outcome": odds, ...}"""

def betting_edge(d):
    TIP = 0 # Total implied probability
    for key in d:
        print(f"{key}, {1/d[key]}")
        TIP += 1/d[key]
    print(f"TIP: {TIP}")
    

a = {'f_wins': 1.61, 'draw': 2.3}
betting_edge(a)
