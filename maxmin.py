def min_element(*args):
    '''
        @Brief: Method is to find minimum element from the given input
        
        Description: min_element() is a generic function with variable arguments. 
                    It finds minimum element from different containers. 
        Examples : 
            1) min_element([1,2,3,4,5]) -> 1
            2) min_element([1,2,3,4],{-1,-2,3,4}) -> -1
            3) min_element([1,2,3,-10,200], -1000) -> -1000
        Practical scenarios :
            1) Using two differnet library APIs and one returns list and other returns a set, 
            today we don't have any ways to find min element from both container
            2) Program has multiple lists and need to find min from all the lists, 
            today to find min all list objects has to get merged and then min() will be performed
    '''
    if not isinstance(args[0], (int,float,list,set,tuple)):
        return

    foundMin = False
    for arg in args:
        if isinstance(arg, (int,float)):
            lowest = arg
        else:
            lowest = min(arg)

        if foundMin == False:
            minimum = lowest
            foundMin = True            
        elif lowest < minimum:
            minimum = lowest

    return minimum

def max_element(*args):
    '''
        @Brief: Method is to find maximum element from the given input
        
        Description: max_element() is a generic function with variable arguments. 
                    It finds maximum element from different containers. 
        Examples : 
            1) max_element([1,2,3,4,5]) -> 5
            2) max_element([1,2,3,4],{-1,-2,3,4}) -> 4
            3) max_element([1,2,3,-10,200], 100) -> 200
        Practical scenarios :
            1) Using two differnet library APIs and one returns list and other returns a set, 
            today we don't have any ways to find max element from both container
            2) Program has multiple lists and need to find max from all the lists, 
            today to find max all list objects has to get merged and then max() will be performed
    '''
    if not isinstance(args[0], (int,float,list,set)):
        return

    foundMax = False
    for arg in args:
        if isinstance(arg, (int,float)):
            highest = arg
        else:
            highest = max(arg)

        if foundMax == False:
            maximum = highest
            foundMax = True
        elif highest > maximum:
            maximum = highest

    return maximum

def minmax_element(*args):
    '''
        @Brief: Method is to find minmax elements from the given input container
        
        Description: minmax_element() is a generic function with variable arguments. 
                    It finds minimum and maximum element from different/multiple containers and
                    returns a tuple (min,max). 
        Examples : 
            1) minmax_element([1,2,3,4,5]) -> (1,5)
            2) minmax_element([1,2,3,4],{-1,-2,3,4}) -> (-1,4)
            3) minmax_element([1,2,3,-10,200], 100) -> (-10,200)
        Practical scenarios :
            1) It is very usefull when application needs max and min element. Python does not have a 
            single function which queries multiple containers and get min and max element from it. 
    '''    
    return (min_element(*args),max_element(*args))
