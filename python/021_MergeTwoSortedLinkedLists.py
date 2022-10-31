'''
Merge two sorted linked lists and return it as a sorted linked list.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Note: also include other usual operations for linked list 
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

def mergeTwoLists(list1: Node, list2: Node) -> Node:
    cur = dummy = make_list([None])
    while list1 and list2:
        if list1.dataval < list2.dataval:
            cur.nextval = list1
            list1, cur = list1.nextval, list1
        else:
            cur.nextval = list2
            list2, cur = list2.nextval, list2
            
    if list1 or list2:       # needed when the lengths are different
        cur.nextval = list1 if list1 else list2
        
    return dummy.nextval

if __name__ == "__main__":
    print("Testing multiple pointerst-----------------")
    print("Before changing a list---")
    nums = range(5)
    cur = dummy = make_list(nums)  # pointers referring to the same object
    listprint(cur)
    listprint(dummy)
    print("id cur: " + str(id(cur)))
    print("id dummy: " + str(id(dummy)))

    print("After changing a list---")
    UpdateValue(cur, 0, 45)
    listprint(cur)
    listprint(dummy)   # both curr and dummy will be updated
    print("id cur: " + str(id(cur)))
    print("id dummy: " + str(id(dummy)))

    print("Testing update list-----------------")
    l1 = make_list([4,5,6,7,8,9])
    UpdateValue(l1, 3, 13)
    listprint(l1)

    print("Testing insert value at beginning -----------------")
    l1 = make_list([4,5,6,7,8,9])
    print("Before id l1: " + str(id(l1)))
    l1 = AtBegining(l1, 21)      # use l1 as both arg and return value
    listprint(l1)
    print("After id l1: " + str(id(l1))) # l1 (prev) != l1 (new)

    print("Testing size of linked list -----------------")
    l1 = make_list([1,2,3])
    print("Size of linked list: " + str(get_size(l1)))

    print("Testing get_node()----------------")
    l1 = make_list([10, 11,12,13,14, 15])
    l2 = get_node(l1, 2)
    l3 = get_node(l1, 0)
    print("get_node(2)---")
    listprint(l2)
    print("get_node(0)---")
    listprint(l3)
    print("id l1: " + str(id(l1)))
    print("id l2: " + str(id(l2)))
    print("id l3: " + str(id(l3)))  # l1 == l3

    print("Testing Copy list -----------------")
    l1 = make_list([1,2,3])
    l1_copy = copy_list(l1)
    print("id l1: " + str(id(l1)))
    listprint(l1)
    print("id l1_copy: " + str(id(l1_copy)))
    listprint(l1_copy)
    
    print("Testing Merge 2 list-----------------")
    l1 = make_list([1,2,4])
    l2 = make_list([1,3,4,6])
    print("1st list = ")
    listprint(l1)
    print("2nd list = ")
    listprint(l2)
    print("Combined list = ")
    l3 = mergeTwoLists(l1,l2)
    listprint(l3)