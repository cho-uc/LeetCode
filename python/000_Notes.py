'''
Pointer and reference in python
What concepts that are different from C++

Source : https://nedbatchelder.com/text/names1.html
'''

# using std lib function
def append_twice(a_list, val):
    a_list.append(val)
    a_list.append(val)

#  Unexpected aliasing bugs. Making new lists can avoid these problems
def append_twice_bad(a_list, val):
    a_list = a_list + [val, val]    # a_list is a totally new list
    return # frame is destroyed

def append_twice_good(a_list, val):
    a_list = a_list + [val, val]
    return a_list

def append_here(element, seq=[]):
    seq.append(element)
    return seq


if __name__ == "__main__":
    # Assignment to primitive data type (result: unchanged)
    a01 = 12
    b01 = a01
    print("Before change a01: "+str(a01)+ ", b01: "+ str(b01))
    a01 = 56
    print("After change a01: "+str(a01)+ ", b01: "+ str(b01))
    print("-------------------------")

    # Assignment to list member (result: changed)
    nums = [10, 11, 12, 13]
    xx = nums[1]
    print("Before change xx : "+str(xx) + ", nums[1]: " + str(nums[1]))
    nums[1] = 5
    print("After change xx : "+str(xx) + ", nums[1]: " + str(nums[1]))
    print("-------------------------")

    # Iteration in a list will not change the value
    nums = [1, 2, 3]
    for x in nums:
        x = x * 10
    print("List after using iteration(1) : ")   # no change
    print(nums)
    nums = [ 10*x for x in nums ]
    print("List after using iteration(2) : ")
    print(nums)
    print("-------------------------")

    # Function arguments
    nums = [1, 2, 3]
    append_twice(nums, 7)
    print("List after using append_twice : ")
    print(nums)
    nums = [1, 2, 3]
    append_twice_bad(nums, 7)
    print("List after using append_twice_bad : ")
    print(nums)
    nums = [1, 2, 3]
    nums = append_twice_good(nums, 7)
    print("List after using append_twice_good : ")
    print(nums)
    print("-------------------------")
    
    # Default function arguments
    append_here(1);
    print()