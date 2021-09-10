'''
Delete all duplicates of a sorted linked list such that each element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2,3,3]
Output: [1,2,3]
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
	def deleteDuplicates(self, head):
		new_size = head.size
		tmp = head
		while tmp:
			if(tmp.next is not None and tmp.data==(tmp.next).data):
				tmp.next = (tmp.next).next
				new_size -=1
			else:
				tmp = tmp.next
		head.size = new_size
		return head


if __name__ == "__main__":
	head = make_list([1,1,2,3,3]) #create LinkedList
	printLinkedList(head)
	ob1 = Solution()
	print("After removing duplicates = ")
	printLinkedList(ob1.deleteDuplicates(head))
	print("Initial linked list = ")
	printLinkedList(head)

