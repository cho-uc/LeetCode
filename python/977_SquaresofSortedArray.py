'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
'''

def sortedSquares(nums):
	result= nums.copy()
	for i in range(len(nums)):
		result[i] = nums[i]*nums[i]
	result.sort()
	return result


if __name__ == "__main__":
	nums= [-4,-1,0,3,10]
	result = sortedSquares(nums)
	print("Original array = ")
	print(nums)
	print("Squares of array = ")
	print(result)

