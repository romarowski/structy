"""
sum possible
Write a function sum_possible that takes in an amount and a list of 
positive numbers. The function should return a boolean indicating whether 
or not it is possible to create the amount by summing numbers of the list.
You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative.
"""

##############################
# dynamic programming O(a*n) #
##############################

def sum_possible(amount, numbers):
    calculated = dict()
    return _sum_it(amount, numbers, calculated)

def _sum_it(amount, numbers, calculated):
    if amount < 0: 
        return False
    
    if amount == 0:
        return True
    
    if amount in calculated:
        return calculated[amount]
    
    for n in numbers:
        if _sum_it(amount-n, numbers, calculated):
            calculated[amount] = True
            return True
    
    calculated[amount] = False
    return False


print(sum_possible(4, [1, 2, 3,])) # -> True, 4 + 4


#################################
# brute force recursion O(n**a) #
#################################

#def sum_possible(amount, numbers):
#    if amount < 0:
#        return False
#
#    if amount == 0:
#        return True
#    for n in numbers:
#        if sum_possible(amount-n, numbers):
#            return True
#    
#    return False 


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
    