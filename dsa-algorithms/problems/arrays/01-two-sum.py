# Problem 1: Two Sum

def twoSum(nums, target):

    seen = set()
    for i in nums:
        rest_data = target-i
        if rest_data in seen:
            return True
        seen.add(i)    

    return False

nums = [2, 7, 11, 15]
target = 9
# Output: True

result = twoSum(nums, target)
print(result)