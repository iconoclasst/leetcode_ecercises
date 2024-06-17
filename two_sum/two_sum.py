
nums = [2,7,11,15]
# nums = [3, 2, 4]
nums = [3, 3]
target = 6

def two_sum(nums, target):
    hash = {}
    for i in range(len(nums)):
        complement = target - nums[i]

        if complement not in hash:
            hash[nums[i]] = i
        else:
            return [hash[complement], i]
        
print(two_sum(nums, target))

