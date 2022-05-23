def choose_func(lst, func1, func2):
    switch = 0
    for i in lst:
        if i < 0:
            switch = 1
    if switch == 1:
        return func2(lst)
    else:
        return func1(lst)

# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]