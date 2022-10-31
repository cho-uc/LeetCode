'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

You must write an algorithm that runs in O(n) time and without using the division operation.


Solution :
1   2   3   4
    ----24--- : 24
-1-     -12-- : 12
--2--     -4- : 8
----6----     : 6

Difficulty: Medium
'''

def productExceptSelf(nums: list[int]) -> list[int]:
    answer = [1, nums[0]]
    backward = [nums[-1]]   # initialize with last element
    
    print("1 answer: --------")
    print(answer)
    print("1 backward: --------")
    print(backward)
    for i, num in enumerate(nums[1:-1]):
        print("i: "+ str(i)+", num: "+str(num), "answer[i+1]: "+ str(answer[i+1]))
        answer.append(num*answer[i+1])
    print("2 answer: --------")
    print(answer)
    print("2 backward: --------")
    print(backward)

    for i, num in enumerate(nums[-2::-1]):
        backward.append(num*backward[i])
        answer[-2-i] = backward[i] * answer[-2-i]
    print("3 answer: --------")
    print(answer)
    print("3 backward: --------")
    print(backward)
    return answer


if __name__ == "__main__":
    nums= [1,2,3,4]
    result = productExceptSelf(nums)
    print("Original array = ")
    print(nums)
    print("Array of product except self = ")
    print(result)

