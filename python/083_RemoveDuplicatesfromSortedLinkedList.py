'''
Delete all duplicates of a sorted linked list such that each element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2,3,3]
Output: [1,2,3]

See also problem 021 for other linked list related question
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


def deleteDuplicates(head: Node) -> Node:
    current = head
    while current.nextval: # iterate until n-1
        if(current.dataval == (current.nextval).dataval):
            current.nextval = (current.nextval).nextval
        else:
            current = current.nextval
    return head

if __name__ == "__main__":
    head = make_list([1,1,2,3,3]) #create LinkedList
    print("id head: " + str(id(head)))
    listprint(head)
    print("After removing duplicates = ")
    head = deleteDuplicates(head) # use head as both input arg and output
    print("id new_list: " + str(id(head)))
    print("Size: "+str(get_size(head)))
    listprint(head)


