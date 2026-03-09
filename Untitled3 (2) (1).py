# Massivi klaviaturadan daxil edirik (rəqəmləri boşluqla ayıraraq)
arr = list(map(int, input("Massivi daxil et: ").split()))

# k ədədini daxil edirik
k = int(input("k ədədini daxil et: "))

# Funksiya
def contains_nearby_duplicate(arr, k):
    last_seen = {}  # elementin son indeksini saxlayır
 
    for i, num in enumerate(arr):
        if num in last_seen and i - last_seen[num] <= k:
            return "Yes"
        last_seen[num] = i

    return "No"

# Nəticəni çap edirik
print(contains_nearby_duplicate(arr, k))
