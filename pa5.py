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

class KVTree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def treemap(f, tree):
    '''modifies the tree according to the function'''
    if tree is None:
        return
    
    # Apply the function to the current node
    tree.key, tree.value = f(tree.key, tree.value)
    
    # Recursively apply the function to each child
    for child in tree.children:
        treemap(f, child)

