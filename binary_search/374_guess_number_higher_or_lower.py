"""
374. Guess Number Higher or Lower

Easy

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is 
higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible 
results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
"""
import math

def guess(num):
    pick=6
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

def guessNumber(n):
    myg = n//2
    lb, ub = 1, n

    while guess(myg) !=0:
        
        if guess(myg) == 1:
            lb = myg+1
        
        if guess(myg) == -1:
            ub = myg-1
        
        myg = (lb+ub) // 2
    return myg
        



if __name__ == '__main__':
    n = 10
    print(guessNumber(n)) # -> 6