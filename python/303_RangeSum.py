'''
Given an integer array nums, calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

'''

def sumRange(nums: list[int], left: int, right: int):
    sums = [] # the sum of elements from index 0 to index i
    
    # Create the sum of all the indices
    for i, num in enumerate(nums):
        if i == 0:
            sums.append(num)
        else:
            sums.append(sums[i-1] + num)
            
    print("sums: ")
    print(sums)
    
    if left == 0:
        return sums[right]
    return sums[right] - sums[left-1]


if __name__ == "__main__":
    nums= [4,3,0,1,7, -3, -2]
    left = 1
    right = 4
    print(nums)
    result = sumRange(nums, left, right)
    print("Sum between index "+str(left) +"-"+str(right)+" = "+str(result))
