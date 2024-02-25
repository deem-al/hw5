#Problem 1: Bisection Method

def bisection_root(function, LB, UB):
    '''Uses bisection root method to find a root of a function'''    
    if function(LB) * function(UB) > 0:
        raise ValueError ("can't find two roots on same side of xaxis")        
    if abs(function(LB)) < 1e-6:
        return LB
    if abs(function(UB)) < 1e-6:
        return UB

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
        self.variable = variable
        self.threshold = threshold
        self.lessequal = lessequal
        self.greater = greater
        self.outcome = outcome
        
        if ((variable is not None and threshold is not None and
             lessequal is not None and greater is not None) and
            (outcome is None)) or ((variable is None and
                                    threshold is None and
                                    lessequal is None and
                                    greater is None) and
                                    (outcome is not None)):
            raise ValueError("Invalid input parameters")

    def tuple_atleast(self):
        if self is None:
            return 0
        
        if self.variable is not None:
            return max(self.variable + 1, self.lessequal.tuple_atleast(), self.greater.tuple_atleast())
        else:
            return max(self.lessequal.tuple_atleast(), self.greater.tuple_atleast())

    def find_outcome(self, observations):
        if self.variable is not None:
            observation_value = observations[self.variable]
            threshold_value = self.threshold

            if observation_value < threshold_value or observation_value == threshold_value:
                return self.lessequal.find_outcome(observations)
            else:
                return self.greater.find_outcome(observations)
        else:
            return self.outcome

    def no_repeats(self):
        def helper(tree, seen_variables):
            if tree is None:
                return True
            if tree.variable in seen_variables:
                return False
            seen_variables.add(tree.variable)
            return helper(tree.lessequal, seen_variables.copy()) and helper(tree.greater, seen_variables.copy())

        return helper(self, set())
