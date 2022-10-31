'''
Remove all the nodes of the linked list that has Node.val == val.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
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


def removeElements(head, val):
    p = head        # a copy of head for return value
    current = head  # a copy of head for iteration

    while current.nextval: # iterate until n-1
        if current.dataval == val:
            current = current.nextval # removing this element
            p = current               # if first element has to be removed
        elif current.nextval.dataval == val:
            current.nextval = current.nextval.nextval # removing this element
            # if middle element has to be removed
        else:
            current = current.nextval
    
    return p


if __name__ == "__main__":
    head = make_list([1,2,3,5,2,4,1,2,4]) #create LinkedList
    ori = head
    print("id: " + str(id(head)))
    listprint(head)

    removedElement = 2
    print("After removing all elements = "+ str(removedElement)+" including element in the middle")
    result = removeElements(head, removedElement)
    print("result: " + str(id(result)))
    listprint(result)

    print("-------------------")
    head = make_list([1,2,3,5,2,4,1,2,4]) #create LinkedList
    ori = head
    print("id: " + str(id(head)))
    listprint(head)

    removedElement = 1
    print("After removing elements = "+ str(removedElement)+" including element in the beginning")
    result = removeElements(head, removedElement)
    print("result: " + str(id(result)))
    listprint(result)

    print("-------------------")
    head = make_list([1,2,3,5,2,4,1,2,4]) #create LinkedList
    ori = head
    print("id: " + str(id(head)))   # id will be changes because first element is gone now
    listprint(head)

    removedElement = 4
    print("After removing elements = "+ str(removedElement)+" including element in the end")
    result = removeElements(head, removedElement)
    print("result: " + str(id(result)))
    listprint(result)