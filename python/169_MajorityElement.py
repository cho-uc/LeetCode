'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than (n/2) times.

Input: nums = [3,2,3]
Output: 3
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

def majorityElement(nums: list[int]) -> int:
	nums.sort()
	return nums[len(nums)//2]


if __name__ == "__main__":
	nums= [2,2,1,1,1,2,2]
	result = majorityElement(nums)
	print("Majority Element = "+ str(result))

