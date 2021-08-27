'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

#Use sliding window algorithm

def maxSubArray(nums):
	maxSub = nums[0]
	curSum = 0			# current Sum
	
	for n in nums:
		if curSum<0 :	#drop all negative val as it will decrease maxSub
			curSum = 0
		curSum +=n
		maxSub = max(maxSub, curSum)

	return maxSub


if __name__ == "__main__":
	nums= [-2,1,-3,4,-1,2,1,-5,4]
	result = maxSubArray(nums)
	print(nums)
	print("Max value of SubArray = " +str(result))

