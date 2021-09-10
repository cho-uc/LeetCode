'''
When climbing a staircase, it takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example:

Input: n = 4
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step+ 1 step
2. 1 step + 2 steps+ 1 step
3  2 steps + 1 step+ 1 step
4. 1 step + 1 step+ 2 steps
5. 2 steps + 1 steps

'''

def climbStairs(n):
	#number of path from nth stair to nth stair is 1 (do not move)
	dp = [0] * (n+2)
	dp[n] =1;

	#go from n-1 stair to 0th stair
	for i in range (n-1,-1,-1):
		#number of paths from i to n will be, number of paths from i+1 to n + number of paths from i+2 to n
		dp[i] = dp[i+1] + dp[i+2]

	#return the number of paths from 0th stair to nths stair
	return dp[0];


if __name__ == "__main__":
	num= 4
	result = climbStairs(num)
	print("Number of ways to climb stairs with " +str(num)+" steps = "+str(result))

