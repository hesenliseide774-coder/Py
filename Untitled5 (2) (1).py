def find_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1  # Nəzəri olaraq lazım deyil, çünki 1 təkrarlanan element var

# Misallar
print(find_duplicate([1, 3, 2, 3, 4]))       # 3
print(find_duplicate([1, 5, 1, 2, 3, 4]))   # 1
