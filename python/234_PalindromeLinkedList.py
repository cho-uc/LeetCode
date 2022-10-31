'''
Check if a linked list is a Palindrome

Input: head = [1,2,2,1] -> True
Input: head = [1,2,3,4] -> False
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


def isPalindrome(head):
    slow, fast, head_copy = head, head, head
    
    # get pointer slow to the middle of linked list (n/2)
    # using fast pointer that iterate every 2 steps
    while(fast and fast.nextval):
        slow = slow.nextval
        fast = fast.nextval.nextval

    print("--Slow:----")
    listprint(slow)
    print("-----")

    # Create a new linked list half_reverse with element from n/2 to (n) 
    half_reverse = slow
    current = slow.nextval
    half_reverse.nextval = None
    
    while(current):
        tmp = current.nextval
        current.nextval = half_reverse
        half_reverse = current
        current = tmp

    print("-half_reverse:----")
    listprint(half_reverse)
    print("-----")
    while(half_reverse != None and head_copy != None):
        if(half_reverse.dataval != head_copy.dataval):
            return False
        half_reverse = half_reverse.nextval
        head_copy = head_copy.nextval
        
    return True

if __name__ == "__main__":
    head = make_list([1,2,3,3,2,1]) #create LinkedList with even members
    listprint(head)
    print("Is Linked List a Palindrome = ", str(isPalindrome(head)))
    head = make_list([11,21,31,21,11]) #create LinkedList with odd members
    listprint(head)
    print("Is Linked List a Palindrome = ", str(isPalindrome(head)))

    head = make_list([6,7,7,5]) #create LinkedList non palindrome
    listprint(head)
    print("Is Linked List a Palindrome = ", str(isPalindrome(head)))
