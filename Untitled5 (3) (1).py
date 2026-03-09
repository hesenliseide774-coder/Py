def is_subset(a, b):
    set_a = set(a)   # a massivini set-ə çeviririk
    for num in b:
        if num not in set_a:
            return False
    return True

# Misallar
print(is_subset([11, 1, 13, 21, 3, 7], [11, 3, 7, 1]))  # True
print(is_subset([1, 2, 3, 4, 5, 6], [1, 2, 4]))         # True
print(is_subset([10, 5, 2, 23, 19], [19, 5, 3]))        # False
