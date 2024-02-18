## Dynamic Programming

### Fibonacci sequence problem

**Statement:** Given a number ```n``` $\in\N$, find the its Fibonacci number.

$$
\begin{align*}
F_0 &=  0, \\
F_1 &=  1, \\
F_n &=  F_{n-1} + F_{n-2}
\end{align*}
$$

**Approach**:
It is possible to solve this problem with brute force recursion.

```python
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
```

Nevertheless this leads to repeated work. For example, the call to ```fib(3)``` will call ```fib(2)``` and ```fib(1)```, and the call to ```fib(2)``` will call ```fib(1)``` and ```fib(0)```. This means that the call to ```fib(1)``` is repeated.
Leading to a complexity of $O(2^n)$.

A better approach is to use **dynamic programming** and store the results of the subproblems.

**Complexity**:
- Time: $O(n)$
- Space: $O(n)$


