
import maxmin as Mm
import lowerupperbound as Lu

#================ Feature : max/min element : Test start =======================#
'''
Test case to find minimum from different containers
'''
# Find and print minimum element from multiple containers 
print(Mm.min_element([1,2,3,4],[-1,2,3,4],(9,-10)))

# Find minimum from multiple integer elements  
a,b,c,d = 1,10,-1,5
print(Mm.min_element(a,b,c,d))


'''
Test case to find maximum from different containers
'''
# Find and print maximum element from multiple containers 
print(Mm.max_element([1,2,3,4],[-1,2,3,4],(9,-10)))

# Find maximum from multiple integer elements
a,b,c,d = 1,10,-1,50
print(Mm.max_element(a,b,c,d))

'''
Test case to find minimum and maximum from different containers
'''
# Find and print minimum and maximum element from multiple containers 
print(Mm.minmax_element([1,2,3,4],[-1,2,3,4],(9,-10)))

# Find minimum and maximum from multiple integer elements
a,b,c,d = 1,11,-7,15
print(Mm.minmax_element(a,b,c,d))


#================ Feature : lower/upper bounds : Test start =======================#

'''
Find lower and upper bounds of a given number in a given series
'''

#Find lower bound of a number from an empty container
print(Lu.lower_bound([],12))

#Find lower bound of a number from an container where all numbers are greater than the number
print(Lu.lower_bound([10,2,3,4,7,11],1))

# Find lower bound of a number when number itself is spresent in the list
print(Lu.lower_bound([1,2,3,90,4,7,11],11))

#Find lower bound 
print(Lu.lower_bound([1,2,3,90,4,7,11],12))


# Find lower and upper bound of a number in the given list where number is present 
print(Lu.lower_upper_bound([1,2,3,90,4,7,11],11))

# Find lower and upper bound of a number
print(Lu.lower_upper_bound([1,2,3,90,4,70,10],11))