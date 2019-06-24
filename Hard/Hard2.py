#Good morning! Here's your coding interview problem for today.

#This problem was asked by Stripe.

#Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

#You can modify the input array in-place.

nums1 = [3,4,-1,1]
nums2 = [1,2,0]
nums3 = [5,6,6,8]
posNums = []

def test_func(nums):
    posNums = [i for i in nums if i>=0]
    posNums.sort()
    check = posNums[0]
    for x in posNums:
        if check+1 in posNums:
            check += 1
        else:
            return check+1

print(test_func(nums1))
print(test_func(nums2))
print(test_func(nums3))