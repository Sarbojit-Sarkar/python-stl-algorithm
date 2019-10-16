
def lower_bound(container, num):
    '''
        @Brief: Method is to find lower bound of a given number 'num' in given container
        
        Description: lower_bound() function returns index of the greatest value less than or equal to 'num' 
                     from given container
        Examples : 
            1) lower_bound([],12) -> 0th index : 
                    Returns first index of the container
            2) lower_bound([10,2,3,4,7,11],1) -> 0th index : 
                    In case container does not have any number smaller than 'num' it returns 0th 
            3) lower_bound([1,2,3,90,4,7,11],12) -> 6
                    11 is the largest value less than 'num'(12) hence function returns 6th as container index
            4) lower_bound([1,2,3,90,4,7,11],11) -> 6
                    11 is the largest value less than equal to 'num'(11) hence function returns 6th as container index

        Practical scenarios :
            1) Function can be used to find smallest deviation from given input
            2) In case of error margine one can use the function to see how close results to expected value 
    '''
    foundLowerBound = False
    index = 0
    lowerBoundIdx = 0
    for ele in container:
        if ele <= num:
            if not foundLowerBound:
                lowerBoundIdx = index 
                foundLowerBound = True
            elif container[lowerBoundIdx] < ele:
                lowerBoundIdx = index
        index = index + 1
    return lowerBoundIdx

def upper_bound(container, num):
    '''
        @Brief: Method is to find upper bound of a given number 'num' in given container
        
        Description: upper_bound() function returns index of the smallest value greater than or equal to 'num' 
                     from given container
        Examples : 
            1) upper_bound([],12) -> 0th index : 
                    Returns first index of the container
            2) upper_bound([10,2,3,4,7,11],100) -> 0th index : 
                    In case container does not have any number greater than 'num' it returns 0th 
            3) upper_bound([1,2,3,90,4,7,11],12) -> 3
                    90 is the largest value less than 'num'(12) hence function returns 3rd as container index
            4) upper_bound([1,2,3,90,4,7,11],11) -> 6
                    11 is the smallest value greater than equal to 'num'(11) hence function returns 6th as container index

        Practical scenarios :
            1) Function can be used to find deviation from given input
            2) In case of error margine one can use the function to see how close results to expected value 
    '''
    foundUpperBound = False
    index = 0
    upperBoundIdx = 0
    for ele in container:
        if ele >= num:
            if not foundUpperBound:
                upperBoundIdx = index 
                foundUpperBound = True
            elif container[upperBoundIdx] > ele:
                upperBoundIdx = index
        index = index + 1
    return upperBoundIdx

def lower_upper_bound(container, num):
    '''
        @Brief: Method is to find lower and upper bound of a given number 'num' in given container
        
        Description: lower_upper_bound() function returns tuple of lower_bound and upper_bound of a given number
                    lower_bound : Greatest number smaller than 'num'
                    upper_bound : Smallest number greater than 'num'
        Example:
            lower_upper_bound([1,2,3,90,4,7,11],12) -> (6,3) 
                Lower bound is at 6th index and upper boud is at 3rd index

        Practical scenarios :
            1) It is more useful when one needs to find out closest range of a number

    '''
    foundUpperBound = False
    foundLowerBound = False
    index = 0
    upperBoundIdx = 0
    lowerBoundIdx = 0
    for ele in container:
        if ele < num:
            if not foundLowerBound:
                lowerBoundIdx = index 
                foundLowerBound = True
            elif container[lowerBoundIdx] < ele:
                lowerBoundIdx = index
        elif ele > num:
            if not foundUpperBound:
                upperBoundIdx = index 
                foundUpperBound = True
            elif container[upperBoundIdx] > ele :
                upperBoundIdx = index
        else:
            lowerBoundIdx = index
            upperBoundIdx = index

        index = index + 1
    return (lowerBoundIdx,upperBoundIdx)
