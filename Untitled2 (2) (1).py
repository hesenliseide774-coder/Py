arr = list(map(int, input("Massivi daxil et: ").split()))

distinct = list(dict.fromkeys(arr))

print(distinct)
