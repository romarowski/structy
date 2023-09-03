import pdb
def compress(s):
  
  ans = ''
  i=0
  j=1
  count=1
  while j < len(s):
    current_letter = s[i]
    next_letter = s[j]
    
    if current_letter == next_letter:
      count+=1
    else:
      if count>1:
        ans+=str(count)+current_letter
      else:
        ans+=current_letter
      i=j
      count=1
    j+=1

  if count>1:
    ans+=str(count)+current_letter
  else:
    ans+=current_letter
  

  
  return ans

if __name__ == '__main__':
    print(compress('ccaaatsss'))
    print(compress('ssssbbz'))
