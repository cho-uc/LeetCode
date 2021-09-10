'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

The algorithm must has O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

'''

class Solution:
	def binarySearch(self, nums, target):
		l=0
		r=len(nums)-1
		mid=0
		while l<=r:
			mid=(l+r)//2
			if nums[mid]<target:
				l=mid+1
			elif nums[mid]>target :
				r=mid-1
			else:
				return mid
		return -1


if __name__ == "__main__":
	my_list=[1,2,3,4,5,7,9]
	val = 5
	print(my_list)
	ob1 = Solution()
	print("Found value "+str(val)+" in index = "+str(ob1.binarySearch(my_list, val)))

