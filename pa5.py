#Problem 1: Bisection Method

def bisection_root(function, LB, UB):
    '''Uses bisection root method to find a root of a function'''
    
    if function(LB) * function(UB) > 0:
        raise ValueError("we cannot expect to find a root between two points on the same side of the x-axis")
        
    while abs(UB - LB) > 1e-6:
        midpoint = (LB + UB) / 2
        if abs(function(midpoint)) < 1e-6:
            return midpoint
        elif function(LB) * function(midpoint) < 0:
            UB = midpoint
        else:
            LB = midpoint
            
    return (LB + UB) / 2

#Problem 2: Dictionary Filter

def dict_filter(f, d):
    '''produces a new dictionary where a given key and value 
    remain associated with each other 
    in the new dictionary, if and only if the function 
    returns True when called with the key and the value'''    
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
    
    tree.key, tree.value = f(tree.key, tree.value)
    for child in tree.children:
        treemap(f, child)

#Problem 4: Trees Modeling Decisions
class DTree:
    def __init__(self, variable, threshold, lessequal, greater, outcome):
        if (variable is not None and threshold is not None and 
            lessequal is not None and greater is not None and outcome is None) or \
           (variable is None and threshold is None and 
            lessequal is None and greater is None and outcome is not None):
            self.variable = variable
            self.threshold = threshold
            self.lessequal = lessequal
            self.greater = greater
            self.outcome = outcome
        else:
            raise ValueError("Invalid input parameters")

    def tuple_atleast(self):
        """Analyzes tree to determine how many entries there need to be in the tuple."""
        if self.lessequal is None and self.greater is None:
            if self.variable is None:
                return 0
            return self.variable + 1 
        elif self.lessequal:
            return max(self.variable + 1, self.lessequal.tuple_atleast()) 
        elif self.greater:
            return max(self.variable + 1, self.greater.tuple_atleast())

    def find_outcome(self, tup):
        '''Takes in a tuple with observations and navigates through 
        the tree to provide the outcome that matches'''
        if self.variable is None:
            return self.outcome
        else:
            next_node = self.greater if tup[self.variable] > self.threshold else self.lessequal
            return next_node.find_outcome(tup)

    def no_repeats(self):
        '''Analyzes the tree and returns True if and only if there are no “repeats”, False otherwise.'''
        def helper(node, variable_set):
            if node.variable in variable_set:
                return False
            if node.lessequal is None and node.greater is None:
                return True
            variable_set.add(node.variable)
            return helper(node.lessequal, set(variable_set)) and helper(node.greater, set(variable_set))

        return helper(self, set())
