'''
Given an integer array arr that is guaranteed to be a mountain, return any i such that 
arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Input: arr = [3,4,5,1]
Output: 2
Input: arr = [0,10,5,2]
Output: 1
'''

class Solution:
	def peakIndexInMountainArray(self, arr):
		for i in range(1,len(arr)):
			if arr[i] < arr[i-1]:
				return i-1

if __name__ == "__main__":
	nums= [0,10,5,2]
	obj = Solution()
	result = obj.peakIndexInMountainArray(nums)
	print(nums)
	print("A mountain is in index "+str(result))

