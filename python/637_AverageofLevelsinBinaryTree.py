'''
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.

Input: root = [3,9,20,null,15,7]
Output: [3,14.5,11]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.

3
|\
9  20
	|\
	15 7
'''

#Approach #1 Using Depth First Search 
#Approach #2 Breadth First Search
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
	def PrintTree(self):
		if self.left:
			 self.left.PrintTree()
		print(self.val),
		if self.right:
			 self.right.PrintTree()

import queue

class Solution:
	def averageOfLevels(self, root):
		q = queue.Queue()
		q.put(root)
		# putting a None to mark the ending of each level
		q.put(None)
		ans = []
		s, c = 0, 0
		while not q.empty():
			curr = q.get()
			if curr is None:
				ans.append(s/c)
				s = 0
				c = 0
				if q.qsize() != 0:
					q.put(None)
				else:
					break
			else:
				s += curr.val
				c += 1
				if curr.left is not None:
					q.put(curr.left)
				if curr.right is not None:
					q.put(curr.right)
		return ans

def creatBTree(data, index):
	pNode = None
	if index < len(data):
		if data[index] == None:
			return
		pNode = TreeNode(data[index])
		pNode.left = creatBTree(data, 2 * index + 1) # [1, 3, 7, 15, ...]
		pNode.right = creatBTree(data, 2 * index + 2) # [2, 5, 12, 25, ...]
	return pNode 


if __name__ == "__main__":
	#lst = [5,4,8,11,None,13,4,7,2,None,None,None,1]
	lst = [3,9,20,None,15,7]
	root = creatBTree(lst, 0)
	root.PrintTree()
	
	obj = Solution()
	result = obj.averageOfLevels(root)
	print("Average of Tree Levels : ")
	print(result)

