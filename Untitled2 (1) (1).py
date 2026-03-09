# a ədədini daxil edirik və rəqəmlərə çeviririk
a = list(map(int, list(input("a massivinin elementlərini daxil edin: ").strip())))

# b ədədini daxil edirik və rəqəmlərə çeviririk
b = list(map(int, list(input("b massivinin elementlərini daxil edin: ").strip())))

# kəsişmə (təkrarlar nəzərə alınmır)
intersection = list(set(a) & set(b))

print("Nəticə:", intersection)
