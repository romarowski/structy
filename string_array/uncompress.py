import pdb
def uncompress(s):
  ans = '' 
  i = 0 
  c = s[i] 
  num = ''
  #letters=
  
  for c in s:
      if not c.isalpha():
          num += c
      else:
          ans += int(num) * c
          num = ''

  pdb.set_trace()

  ans +=  int(num)*c






  return ans
  
if __name__ == '__main__':
  uncompress("3n12e2z")

