import pdb
def five_sort(nums):
  pdb.set_trace()
  count = 0
  i = 0
  while i < (len(nums)-count):
    num = nums[i]
    if num == 5:
      index = (-1-count)
      temp = nums[index]
      nums[index] = num
      nums[i] = temp
      count = count + 1
    i +=1
  return nums

five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5])


