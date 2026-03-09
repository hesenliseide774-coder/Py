# Massivləri daxil edirik
a = list(map(int, input("a massivini daxil edin: ").split()))
b = list(map(int, input("b massivini daxil edin: ").split()))

# Kəsişməni tapırıq
if set(a) & set(b):
    print(False)  # Ortak element var
else:
    print(True)   # Ortak element yoxdur
