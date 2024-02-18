"""
fib
Write a function fib that takes in a number argument, n, and returns 
the n-th number of the Fibonacci sequence.

The 0-th number of the sequence is 0.

The 1-st number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of 
previous two numbers.

Solve this recursively.
"""

def fib(n):
    calculated = dict()
    calculated[0] = 0
    calculated[1] = 1
    return _fib(n, calculated)


def _fib(n, calculated):
    
    if n in calculated:
        return calculated[n]
    
    calculated[n] = _fib(n-1, calculated) + _fib(n-2, calculated)
    return calculated[n]


print(fib(35)) # -> 9227465