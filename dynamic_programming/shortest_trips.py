"""
From amazon OA.

Given a number n, and only two operations, -2 and -3, find the shortest
number of operations to reach 0.

Example:
n = 10
output = 5
10 - 3 = 7
7 - 3 = 4
4 - 2 = 2
2 - 2 = 0
"""


def shortest_trips(n):
    memo = {}
    shortest = dp(n, memo)
    return shortest


def dp(n, memo):
    
    if n in memo:
        return memo[n]

    if n==0:
        return 0 
    
    if n<0:
        return float('inf')
    
    branch_3=1+dp(n-3, memo)
    branch_2=1+dp(n-2, memo)
    shortest = min(branch_3, branch_2)

    memo[n] = shortest
    return shortest
    
    


if __name__ == '__main__':
    n=2017
    print(shortest_trips(n))
    
    

