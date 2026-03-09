s = input("Enter a string: ")

result = ""
for ch in s:
    if ch == " ":          # əgər boşluq varsa
        result += "%20"    # %20 əlavə et
    else:
        result += ch       # yoxsa simvolu olduğu kimi yaz

print(result)
