'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Input: s = "ab#c", t = "ad#c"
Output: true
Input: s = "ab##", t = "c#d#"
Output: true
'''

def backspaceCompare(s: str, t: str) -> bool:
	def helper(strs):
		stack = []
		
		for i in range(len(strs)):
			if strs[i] == '#':
				if len(stack)>0:
					stack.pop()
			else:
				stack.append(strs[i])
			
		return ''.join(stack)
	
	return helper(s) == helper(t)


if __name__ == "__main__":
	s1= "ab#c"
	s2= "ad#c"
	result = backspaceCompare(s1, s2)
	print("Result =  ", str(result))

