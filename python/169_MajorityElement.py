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

'''
Reason:
The element with m >(n/2) will always be located in the (n/2+1) element
|--n/2--||--n/2--|
xxxxx|--n/2--|xx
xx|--n/2--|xxxxx
'''
