'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
'''

def binaryRepresentation(n):
	count = [0]*(n+1)
	for i in range (1, n+1):
		count[i] = count[int(i / 2)] + int(i % 2)
	return count

if __name__ == "__main__":
	nums= 5
	result = binaryRepresentation(nums)
	print("binaryRepresentation of " +str(nums)+ " = "+str(result))

