NUMS = [2, 7, 11, 15]
TARGET = 9


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                return [i, j]
    return []


print(two_sum(NUMS, TARGET))
