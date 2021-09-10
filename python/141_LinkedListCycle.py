'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
True :
3->2->0->4
	^	|
	|---v
False :
9->6->0->1
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

class Solution(object):
	def hasCycle(self, head):
		hashS = set()
		while head:
			if head in hashS:
				return True
			hashS.add(head)
			head = head.next
		return False


if __name__ == "__main__":
	head = make_list([5,3,2,0,-4,7]) #create LinkedList
	# Create cycle
	last_node = get_node(head, 5)
	pos = 1
	last_node.next = get_node(head, pos)

	ob1 = Solution()
	print("Linked List is cyclic = ")
	print(ob1.hasCycle(head))

