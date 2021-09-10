'''
Merge two sorted linked lists and return it as a sorted list. 

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
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

def copy_list(head):
	new_head = ListNode(get_node(head,0).data)
	for i in range (1,head.size):
		ptr = new_head
		while ptr.next:
			ptr = ptr.next
		ptr.next = ListNode(get_node(head,i).data)
	new_head.size = head.size
	return new_head

def copy_list2(head):
	val =[]	#store in normal list
	temp=head
	temp_size = head.size
	while temp:
		val.append(temp.data)
		temp=temp.next
	new_head = make_list(val)
	new_head.size = temp_size
	return new_head

			
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
	def mergeTwoLists(self, l1, l2):
		if l1 is None: return l2
		if l2 is None: return l1
		
		l1_size = l1.size
		l2_size = l2.size
		p = l1		#l1 will be mutable
		prev = None

		while 1:
			if l1 is None:
				print("l1 is None")
				
				prev.next = l2
				break

			if l2 is None:
				print("l2 is None")
				break

			if l1.data <= l2.data:
				if l1.next is not None:
					if l1.next.data <= l2.data:
						prev = l1
						l1 = l1.next
						continue

				n = ListNode(l2.data)
				l2 = l2.next

				n.next = l1.next
				l1.next = n

				prev = l1
				l1 = l1.next

			else:
				print("l2 < l1")

				n = ListNode(l2.data)
				n.next = l1
				if prev is not None:
					prev.next = n
				else:
					p = n

				prev = n
				l2 = l2.next
		p.size = l1_size + l2_size		# update size for printing
		return p

if __name__ == "__main__":
	l1 = make_list([1,2,4]) #create LinkedList
	l2 = make_list([1,3,4,6])
	print("1st list = ")
	printLinkedList(l1)
	print("2nd list = ")
	printLinkedList(l2)
	print("Combined list = ")
	obj1 = Solution()
	printLinkedList(obj1.mergeTwoLists(l1,l2))

	#print("Initial l1= ")	#mutable
	#printLinkedList(l1)
	#print("Initial l2= ")	#immutable
	#printLinkedList(l2)

