'''
Given an integer array nums, calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

'''

class NumArray:
	def __init__(self, nums):
		self.sums = [] # the sum of elements from index 0 to index i
		self.processSumsFromZero(nums)

	#Store all elements of the array
	def processSumsFromZero(self, nums):
		"""Create the sum of all the indices"""
		for i, num in enumerate(nums):
			if i == 0:
				self.sums.append(num)
			else:
				self.sums.append(self.sums[i-1] + num)
		

	def sumRange(self, left, right):
		if left == 0:
			return self.sums[right]
		return self.sums[right] - self.sums[left-1]


if __name__ == "__main__":
	nums= [4,3,0,1,7, -3, -2]
	left =1
	right = 4
	obj = NumArray(nums)
	result = obj.sumRange(left,right)
	print(nums)
	print("Sum between index "+str(left) +"-"+str(right)+" = "+str(result))

