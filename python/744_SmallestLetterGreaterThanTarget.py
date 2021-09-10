'''
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Input: letters = ["c","f","j"], target = "g"
Output: "j"
'''

class Solution:
	def nextGreatestLetter(self, letters, target):
		for letter in letters:
			if letter > target:
				return letter
		return letters[0]


if __name__ == "__main__":
	letters = ["c","f","j"]
	target = "c"
	ob1 = Solution()
	result = ob1.nextGreatestLetter(letters,target)
	print("The next greatest letter of "+target+ " = "+result)

