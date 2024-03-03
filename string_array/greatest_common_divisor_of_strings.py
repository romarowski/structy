"""
1071. Greatest Common Divisor of Strings

Easy

For two strings s and t, we say "t divides s" if and only 
if s = t + t + t + ... + t + t (i.e., t is concatenated with 
itself one or more times).

Given two strings str1 and str2, return the largest string x 
such that x divides both str1 and str2.
"""

def gcdOfStrings(str1, str2):
    m = len(str1)
    n = len(str2)

    if m>=n:
        divisor = str2
        word = str1
    else:
        divisor = str1
        word = str2

    static_divisor = divisor 
    cur = len(divisor)

    while cur > 0:
        remainder = len(word) % len(divisor)
        if remainder==0:
            k = int((len(word)/len(divisor)))
            divisable = word == divisor * k
            if divisable:
                # now check if this gcd also apply to the divisor
                if len(static_divisor) % len(divisor) == 0:
                    k = int(len(static_divisor)/len(divisor))
                    if static_divisor == divisor*k:
                        return divisor
        
        cur-=1
        divisor = divisor[:cur]
    return ""



if __name__ == "__main__":
    print(gcdOfStrings("ABCABC", "ABC")) # -> "ABC"
    print(gcdOfStrings("ABABAB", "AB")) # -> "AB"