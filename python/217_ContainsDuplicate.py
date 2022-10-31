'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
nums = [1,1,1,3,3,4,3,2,4,2] -> True
nums = [1,2,3,4] -> False
'''

def containsDuplicate(nums):
    unique_numbers = set(nums)  # storing in a hash set will remove any duplicates
    # because a set will only contain unique values
    if len(unique_numbers) == len(nums):
        return False
    else:
        return True


if __name__ == "__main__":
    nums1= [1,1,1,3,3,4,3,2,4,2]
    nums2 = [1,2,3,4]
    result1 = containsDuplicate(nums1)
    print(nums1)
    print("" +str(result1))

    result2 = containsDuplicate(nums2)
    print(nums2)
    print("" +str(result2))
