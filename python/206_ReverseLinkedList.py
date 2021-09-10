'''
Reverse linked list

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
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
	def reverseList(self, head):
		if not head:
			return None
		r = []		#list of nodes
		size_r = head.size	#save var size

		while head:
			r.append(head)
			head = head.next
		
		# This is what we obtain inside the list r. We get 5 nodes and all of them are given below:
		# ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
		# ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
		# ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
		# ListNode{val: 4, next: ListNode{val: 5, next: None}}
		# ListNode{val: 5, next: None}

		#declare our new head as the last node we captured in r because that would be the starting node when the list is reversed.
		newhead = r[-1]
		
		# Since we already took the last element of r as newhead we will start our iteration from the 2nd last node
		n = len(r)-2
		
		# loop through the r list in reverse
		while n>=0:
			node = r[n] # This is the first node that would be consider after taking last as newhead. This will update based on value of n
			node.next = None # We set its next pointer to NULL because it was pointing to the node after it. Since we are assigning nodes from reverse, then having next value would create a cycle. As an example if next of 4 points to 5 and 5, which is the new head, has its head pointing to 4, then there would be loop formed. Hence we make the next pointer of 4 as NULL
			newhead.next = node # Finally, after making the next pointer NULL to remove cycle, we assign the pointer to the next of the newhead. So, as an example, if newhead is 5 which points to null initially, it will now point to 4. 4 which previously pointed to 5 will now point to NULL to prevent cycle
			
			newhead = newhead.next # After assignment, we now change our head to next of the newhead. 
			#This is done because the same would now point to other nodes as they come through the while loop. 
			#In this case, the newhead will be 4, which will now be pointing to NULL until a new node is assigned to it in the next cycle of while. 
			#In the next cycle, the new node would be three and we would do the exact steps. 
			#We would remove the next pointer of 3 pointing to 4 to remove cycle. 
			#We will assign it to 'next' of 4 and then make 3 the newhead. 
			#This will continue till we go till first element of 'r' (we are going reverse if you remember)
			
			n-=1
		
		r[-1].size = size_r
		return r[-1] #return the last node of 'r' list

if __name__ == "__main__":
	head = make_list([1,2,3,4,5]) #create LinkedList
	printLinkedList(head)
	print("After reversing elements = ")
	obj1 = Solution()
	printLinkedList(obj1.reverseList(head))

	#print("Initial = ")	#head is no longer available
	#printLinkedList(head)

