def smallest_subarray_k_distinct(arr, k):
    from collections import defaultdict

    count_map = defaultdict(int)
    left = 0
    min_len = float('inf')
    res = (-1, -1)

    for right in range(len(arr)):
        count_map[arr[right]] += 1

        # Pəncərədə k fərqli element varsa
        while len(count_map) >= k:
            if len(count_map) == k and right - left + 1 < min_len:
                min_len = right - left + 1
                res = (left, right)
            # Solu daraldırıq
            count_map[arr[left]] -= 1
            if count_map[arr[left]] == 0:
                del count_map[arr[left]]
            left += 1

    if res == (-1, -1):
        return -1
    else:
        # 1-based index ilə çap etmək istəyirsənsə:
        # return (res[0]+1, res[1]+1)
        return res

# Misal
arr1 = [1, 2, 1, 2, 3]
k1 = 2
print(smallest_subarray_k_distinct(arr1, k1))  # (0,1) => subarray [1,2]
