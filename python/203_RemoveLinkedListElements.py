'''
Remove all the nodes of the linked list that has Node.val == val.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
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

class Solution:
	def removeElements(self, head, val):
		p = head		#head will be modified
		
		while 1:
			if head is None:
				break

			elif head.data == val:
				head = head.next # removing this element
				p = head 
				p.size -=1		#update size

			elif head.next is None:
				break

			elif head.next.data == val:
				head.next = head.next.next # removing this element
				p.size -=1		#update size

			else:
				head = head.next
		
		return p


if __name__ == "__main__":
	head = make_list([1,2,3,5,2,1,2,4]) #create LinkedList
	printLinkedList(head)
	removedElement = 2
	print("After removing elements = ")
	ob1 = Solution()
	result = ob1.removeElements(head, removedElement)
	printLinkedList(result)
	print("Initial = ")
	printLinkedList(head)

