'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Example :

Input: x = 120
Output: 21
Input: x = -123
Output: -321
Input: x = 123
Output: 321

'''

# Solution #1
def reverse1(x: int) -> int:
	nums=0
	max_int = 2**31-1
	min_int = -2**31
	y = abs(x)
	while(y>0):
		nums = nums*10 + y%10
		y //= 10
	if x<0:
		nums *= -1
	if nums > max_int or nums < min_int:
		return 0
	return nums

# Solution 2
def reverse2(x: int) -> int:
	sign = -1 if x<0 else 1
	max_int = 2**31-1
	min_int = -2**31
	result = int(str(x*sign)[::-1])*sign
	if result < min_int or result > max_int:
		return 0
	return result


if __name__ == "__main__":
	x1= 123
	x2= -456
	print("Reverse number 1  = " +str(reverse1(x1)))
	print("Reverse number 2  = " +str(reverse1(x2)))

