#Easy - Problem 1

#Good morning! Here's your coding interview problem for today.

#This problem was recently asked by Google.

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?

nums = [10,15,3,7]

def test_func(test,k):
        check = False
        for x in nums:
           for y in nums:
                if x+y == k:
                        check = True  
        if check == True: 
                return True
        elif check == False:
                return False

print(test_func(nums,19))

#for X in Array:
	#if k - X in Array:



