'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

'''

# Solution #1 to reverse digits
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

# Solution 2 to reverse digits
def reverse2(x: int) -> int:
	sign = -1 if x<0 else 1
	max_int = 2**31-1
	min_int = -2**31
	result = int(str(x*sign)[::-1])*sign
	if result < min_int or result > max_int:
		return 0
	return result

# Final checking
def isPalindrome(x: int) -> bool:
	x_reverse1 = reverse1(x)
	x_reverse2 = reverse1(x_reverse1)
	if x_reverse1 == x_reverse2:
		return True
	else:
		return False
	


if __name__ == "__main__":
	x1 = 123
	x2 = -456
	print("Reverse of: " + str(x1) + " is " + str(reverse1(x1)))
	print("Reverse of: " + str(x2) + " is "+ str(reverse1(x2)))
	
	print("--------------------------")
	x4 = 4567
	x5 = 451154	 # a palindrome with even digits
	x6 = 32523	 # a palindrome with odd digits
	# From here we can check if a number is a palindrome
	print(str(x4) + " is a palindrome : " + str(isPalindrome(x4)))
	print(str(x5) + " is a palindrome : " + str(isPalindrome(x5)))
	print(str(x6) + " is a palindrome : " + str(isPalindrome(x6)))
	

