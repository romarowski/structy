"""
1768. Merge Strings Alternately

Easy

You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, 
append the additional letters onto the end of the merged string.

Return the merged string.
"""

def mergeAlternatively(word1, word2):
    cur1 = 0
    cur2 = 0
    ans = ""

    while cur1 < len(word1) and cur2 < len(word2):
        ans += word1[cur1] + word2[cur2]

        cur1+=1
        cur2+=1
        
        if cur1 == len(word1):
            if cur2 < len(word2):
                ans+=word2[cur2:]
            return ans
        
        if cur2 == len(word2):
            if cur1 < len(word1):
                ans+=word1[cur1:]
            return ans
    return ans



print(mergeAlternatively("abc","pqr")) #-> "apbqcr"