'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
True :
3->2->0->4
    ^   |
    |---v
False :
9->6->0->1
'''

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

def make_list(elements: list):
    head = Node(elements[0])
    current = head
    for item in elements[1:]:
        current.nextval = Node(item)
        current = current.nextval     # update for next iteration
    
    # head will still point to the first element, but current will iterate through the whole elements
    return head

def get_node(head: Node, pos: int) -> Node:
    current = head 
    # start from head+1 since we already process head
    for i in range (1, pos + 1): 
        current = current.nextval
    return current


def isCyclic(head):
    hashS = set()    # create a hash set (no duplicate elements) to store the node elements
    while head:
        print(head.dataval)
        if head in hashS:
            return True
        hashS.add(head)
        head = head.nextval
    return False


if __name__ == "__main__":
    head = make_list([5,3,2,0,-4,-3, -2]) #create LinkedList
    # Create cycle by linking the last element of the list to other element in the middle
    last_node = get_node(head, 6)
    pos = 1
    last_node.nextval = get_node(head, pos)

    print("Linked List is cyclic = ")
    print(isCyclic(head))
    print("\n")

    head2 = make_list([15,13,12]) #create LinkedList
    print("Linked List is cyclic = ")
    print(isCyclic(head2))
