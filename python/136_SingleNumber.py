'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Input: nums = [4,1,2,1,2]
Output: 4

See problem no 268
'''

def singleNumber(nums):
	nums.sort()
	i=0
	count = 0
	while(i <(len(nums)-1)):
		if(nums[i]!=nums[i+1]):
			result = nums[i]
			count = 1
			break
		i =i+2

	if(count ==0):
		result = nums[len(nums)-1] # last member of the list
	return result

if __name__ == "__main__":
	nums= [2,1,4,1,2]
	result = singleNumber(nums)
	print(nums)
	print("Missing number = " +str(result))

