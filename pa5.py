#Problem 1: Bisection Method

def bisection_root(function, LB, UB):
    '''Uses bisection root method to find a root of a function'''
    
    if function(LB) * function(UB) > 0:
        raise ValueError ("we cannot expect to find a root between two points on the same side of the xaxis")
        
    if abs(function(LB)) < 1e-6:
        return LB
    if abs(function(UB)) < 1e-6:
        return UB

#Problem 2: Dictionary Filter

def dict_filter(f, d):
    '''produces a new dictionary where a given key and value remain associated with each other 
    in the new dictionary, if and only if the function returns True when called with the key and the value'''
    
    filtered_d = {}
    
    for key, value in d.items():
        if f(key, value):
            filtered_d[key] = value
    
    return filtered_d

def checker(name, abbrev):
    return abbrev[0] == "I" and name[1] == "l"
example = {"Illinois": "IL", "Pennsylvania": "PA", "Indiana": "IN"}

dict_filter(checker, example)
