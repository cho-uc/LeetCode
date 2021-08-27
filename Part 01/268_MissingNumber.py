'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Input: nums = [4,3,0,1]
Output: 2

See problem no 448
'''

def missingNumber(nums):
	n = len(nums)
	sum=n*(n+1)/2		#use math concept
	for i in range (0,len(nums)):
		sum= sum -nums[i];
	return sum;


if __name__ == "__main__":
	nums= [4,3,0,1]
	result = missingNumber(nums)
	print(nums)
	print("Missing number = " +str(result))

