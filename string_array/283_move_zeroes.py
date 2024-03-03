"""
283. Move Zeroes
Easy

Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

def moveZeroes(nums):

    slow = 0
    for fast in range(len(nums)):
        val_fast = nums[fast]
        val_slow = nums[slow]
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        # wait while we find a non-zero element to
        # swap with you
        if nums[slow] != 0:
            slow += 1


#    cur1 = 0
#    cur2 = len(nums)-1
#
#    while cur1 < cur2:
#        val1 = nums[cur1]
#        val2 = nums[cur2]
#
#        if val1==0:
#            if val2 !=0:
#                nums[cur1], nums[cur2] = nums[cur2], nums[cur1]
#            else:
#                cur2 -=1
#        else:
#            cur1 +=1

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    moveZeroes(nums)
    print(nums) # ->[1,3,12,0,0]