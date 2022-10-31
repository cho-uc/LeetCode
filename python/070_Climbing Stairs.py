'''
When climbing a staircase, it takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example:

Input: n = 4
Output: 5
Explanation: There are five ways to climb to the top.
1. 1 step + 1 step + 1 step+ 1 step
2. 1 step + 2 steps+ 1 step
3  2 steps + 1 step+ 1 step
4. 1 step + 1 step+ 2 steps
5. 2 steps + 2 steps

Input: n = 5
Output: 8
1+1+1+1+1
1+2+2  2+2+1  2+1+2
1+2+1+1  1+1+1+2  1+1+2+1  2+1+1+1

Input: n = 6
Output: 13
1+1+1+1+1+1
2+2+2
1+1+2+2  2+2+1+1  2+1+2+1  1+2+1+2  2+1+1+2  1+2+2+1
2+1+1+1+1  1+2+1+1+1  1+1+2+1+1  1+1+1+2+1 1+1+1+1+2

This is an example of calculating Fibonacci sequence
    Num of step 1  2  3  4  5  6
    Num of way  1  2  3  5  8  13
'''

def climbStairs(n):
    # number of path from nth stair to nth stair is 1 (do not move)
    dp = [0] * (n+2)
    dp[n] = 1;

    #go from n-1 stair to 0th stair
    for i in range (n-1,-1,-1):  #(start, stop, step)
        #number of paths from i to n will be, number of paths from i+1 to n + number of paths from i+2 to n
        dp[i] = dp[i+1] + dp[i+2]

    #return the number of paths from 0th stair to nths stair
    return dp[0];

# Alternative solution
def climbStairs2(n):
    num_of_steps = 0
    n_minus_one = 2
    n_minus_two = 1
    
    if(n == 1):
        return 1
    if(n == 2):
        return 2
    
    for i in range (3, n+1): # starting from stair with 3 steps
        num_of_steps = (n_minus_one + n_minus_two)
        n_minus_two = n_minus_one
        n_minus_one = num_of_steps

    return num_of_steps


if __name__ == "__main__":
    num = 4
    result = climbStairs(num)
    print("Number of ways to climb stairs with " +str(num)+" steps = "+str(result))
    num = 5
    result = climbStairs(num)
    print("Number of ways to climb stairs with " +str(num)+" steps = "+str(result))
    print("------Using alternative method-------")
    num = 4
    result = climbStairs2(num)
    print("Number of ways to climb stairs with " +str(num)+" steps = "+str(result))
    num = 5
    result = climbStairs2(num)
    print("Number of ways to climb stairs with " +str(num)+" steps = " + str(result))
    num = 6
    result = climbStairs2(num)
    print("Number of ways to climb stairs with " +str(num)+" steps = "+str(result))

