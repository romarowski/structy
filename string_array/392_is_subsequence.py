
######
# DP #
######
def isSubsequence(s,t):
    nxt = [{} for _ in range(len(t) + 1)]
    for i in range(len(t) - 1, -1, -1):
        nxt[i] = nxt[i + 1].copy()
        nxt[i][t[i]] = i + 1
    
    print("hello")

    pass




################
# TWO POINTERS #
################
#def isSubsequence(s, t):
#    slow = 0
#    if s=="":
#        return True
#        
#
#    for fast in range(len(t)):
#        if slow==len(s):
#            break
#          
#        if s[slow] == t[fast]:
#            slow+=1
#    if slow == len(s):
#        return True
#    
#    return False




if __name__ == '__main__':
     s = "abc"
     t = "ahbgdc"
     print(isSubsequence(s,t)) # -> True