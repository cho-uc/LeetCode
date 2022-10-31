'''
Reverse linked list

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
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

def listprint(head: Node):
    current = head
    while current:
        print("dataval: "+ str(current.dataval))
        current = current.nextval
    print("")

# Insert new element at the beginning
# Return new linked list
def AtBegining(head: Node, newdata: int) -> Node:
    NewNode = Node(newdata)
    # Update the new nodes next val to existing node
    NewNode.nextval = head
    head = NewNode
    return head

def UpdateValue(head: Node, pos: int, newdata: int):
    current = head
    for i in range (0, pos + 1):
        if (i == pos):
            current.dataval = newdata
        current = current.nextval

def copy_list(ori: Node) -> Node:
    head = Node(ori.dataval)
    current = head
    while ori.nextval: # iterate until n-1
        ori = ori.nextval     # start from head+1 since we already process head
        current.nextval = Node(ori.dataval)
        current = current.nextval
    # head will still point to the first element, but current will iterate through the whole elements
    return head

def get_size(head: Node) -> int:
    size = 0
    current = head
    while current:
        size = size + 1
        current = current.nextval
    return size

def get_node(head: Node, pos: int) -> Node:
    current = head 
    # start from head+1 since we already process head
    for i in range (1, pos + 1): 
        current = current.nextval
    return current

def reverseList(head: Node):
    r = []      #list of nodes
    # store the element in the list
    while head:
        r.append(head) 
        head = head.nextval

    newhead = r[-1] # declare our new head as the last node
    current = r[-1] # for iteration
    
    # Since we already took the last element of r as newhead we will start our iteration from the 2nd last node
    n = len(r)-2
    
    # loop through the r list in reverse
    while n>=0:
        node = r[n]
        node.nextval = None # We set its next pointer to NULL because it was pointing to the node after it. Since we are assigning nodes from reverse, then having next value would create a cycle.
        current.nextval = node
        current = current.nextval
        n-=1

    return newhead

def reverseList2(head: Node):
    r = []      #list of nodes
    # store the element value in the list
    while head:
        r.append(head.dataval)
        head = head.nextval

    newhead = Node(r[-1]) # declare our new head as the last node
    current = newhead     # for iteration
    
    # Since we already took the last element of r as newhead we will start our iteration from the 2nd last node
    start = len(r)-2
    for i in range(start, -1, -1):    # range(start, stop, increment)
        current.nextval = Node(r[i])
        current = current.nextval     # update for next iteration

    return newhead

if __name__ == "__main__":
    head = make_list([1,2,3,4,5]) #create LinkedList
    print("id head: " + str(id(head)))
    listprint(head)
    print("After reversing elements = ")
    result = reverseList(head)
    listprint(result)

    print("-----Using 2nd alternative----------")
    head = make_list([1,2,3,4,5]) #create LinkedList
    print("id head: " + str(id(head)))
    listprint(head)
    print("After reversing elements = ")
    result = reverseList2(head)
    listprint(result)
