'''
Check if a linked list is a Palindrome

Input: head = [1,2,2,1] -> True
Input: head = [1,2,3,4] -> False
'''

class ListNode:
	size =0
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

def make_list(elements):
	head = ListNode(elements[0])
	head.size = len(elements)
	for element in elements[1:]:
		ptr = head
		while ptr.next:
			ptr = ptr.next
		ptr.next = ListNode(element)
	return head

def get_node(head, pos):
	if pos != -1:
		p = 0
		ptr = head
		while p < pos:
			ptr = ptr.next
			p += 1
		return ptr

def printLinkedList(head):
	pos = 0
	while (pos<head.size):
		print(get_node(head, pos).data)
		pos = pos +1

class Solution(object):
	def isPalindrome(self, head):
		slow, fast, head_copy = head, head, head
		while(fast and fast.next):
			slow = slow.next
			fast = fast.next.next
			
		prev = slow
		curr = slow.next
		prev.next = None
		
		while(curr):
			tmp = curr.next
			curr.next = prev
			prev = curr 
			curr = tmp
		
		while(prev != None and head_copy != None):
			if(prev.data != head_copy.data):
				return False
			prev = prev.next
			head_copy = head_copy.next
			
		return True


if __name__ == "__main__":
	head = make_list([1,2,3,3,2,1]) #create LinkedList
	printLinkedList(head)
	ob1 = Solution()
	
	print("Is Linked List a Palindrome = ", str(ob1.isPalindrome(head)))
	

