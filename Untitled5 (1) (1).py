s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

j = 0  # s1-in indexi

for i in range(len(s2)):
    if j < len(s1) and s2[i] == s1[j]:
        j += 1  # uyğun hərf tapıldı

if j == len(s1):
    print("True")
else:
    print("False")
