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


#Problem 3: Tree Map

def treemap(f, tree):
    '''modifies the tree according to the function'''
    
    if tree is None:
        return
    
    key, value, left, right = tree
    
    new_key, new_value = f(key, value)
    tree[0] = new_key
    tree[1] = new_value
    
    treemap(f, left)
    treemap(f, right)
