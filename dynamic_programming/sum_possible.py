"""
sum possible
Write a function sum_possible that takes in an amount and a list of 
positive numbers. The function should return a boolean indicating whether 
or not it is possible to create the amount by summing numbers of the list.
You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative.
"""

def sum_possible(amount, numbers):
    for n in numbers:
        possible = recur(amount, n, numbers)
        if possible:
            return True 

    return False 

def recur(remainder, subtrahend, numbers):
    
    if subtrahend > remainder:
        return
    
    remainder = remainder - subtrahend

    if remainder == 0:
        return True
    
    

    return False 

    




print(sum_possible(4, [1, 2, 3,])) # -> True, 4 + 4

###############################
# solution with n! complexity #
###############################

#def sum_possible(amount, numbers):
#    for j in range(len(numbers)):
#        possible =_mod(amount, numbers.copy(), j)
#        if possible:
#            return True
#    return False
#
#def _mod(amount, numbers, i):
#    # i need a way to keep track of the numbers i already used for that
#    # branch of the recursive call
#    
#    # i need to try modding simultaneously with all values in the array
#    if i == len(numbers):
#        return 
#
#    #n = numbers[i]
#    n = numbers.pop(i)
#
#    if n > amount:
#        return
#
#    remainder = amount % n 
#    if remainder == 0:
#        return True
#    
#    return _mod(remainder, numbers, 0)
    