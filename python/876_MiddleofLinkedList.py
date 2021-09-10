'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
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
	def middleNode(self, head):
		n=0
		temp=head
		#Calculating length of the Linked List
		while temp:
			n+=1
			temp=temp.next
		n//=2
		if(head.size%2==0):
			half_size = head.size/2
		else:
			half_size = (head.size+1)/2
		#Iterating over n/2 elements
		while n>=0:
			if n==0: 
				return head
			head=head.next
			head.size = half_size
			n-=1
			
		return head


if __name__ == "__main__":
	head = make_list([1,2,3,4,5]) #create LinkedList
	printLinkedList(head)
	ob1 = Solution()
	print("Middle of Linked List = ")
	printLinkedList(ob1.middleNode(head))
	printLinkedList(head)

