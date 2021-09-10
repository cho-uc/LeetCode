'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Input: nums = [4,3,0,1,7]
Output: [2,5,6]

See problem no 268
'''

def missingNumbers(nums):
	result = []
	map = set(nums)		#store all elements as keys in hashmap
	max_num = max(nums)
	start = 0;
	while (start <= max_num) :	# check elements from map.
		if not (start in map):
			result.append(start);
		start= start+1

	return result;


if __name__ == "__main__":
	nums= [4,3,0,1,7]
	result = missingNumbers(nums)
	print(nums)
	print("Missing numbers = " +str(result))

