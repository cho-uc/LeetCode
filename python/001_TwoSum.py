'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Because nums[0] + nums[1] == 9.
'''


def twoSum(nums, target):
	visited = {}		# store index in a set
	for index, number in enumerate(nums):
		difference = target - number
		if difference in visited:
			return [visited[difference], index] 
		else:
			visited[number] = index


if __name__ == "__main__":
	nums= [0, 1, 2,7,11,15]
	target = 9
	result = twoSum(nums, target)
	print(nums)
	print("Indices where the sum = " +str(target)+" is "+str(result))

