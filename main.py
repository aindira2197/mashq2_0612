#list2
words = ["dasturlash", "kitob", "shunday", "kompyuter", "ilm", "maktab"]
indx = []

for i in words:
    indx.append(len(i))

max_1 = indx.index(max(indx))
print(f"1-chi eng uzun so‘z: {words[max_1]}")
words.pop(max_1)
indx.pop(max_1)

max_2 = indx.index(max(indx))
print(f"2-chi eng uzun so‘z: {words[max_2]}")

#string
soz = input("Soz kirit: ")

for i in range(len(soz)):
    print(f"{i+1}-{soz[i]}")

#string slice
soz = input("Soz kirit: ")
new = ''

for i in range(len(soz)):
    if soz[i] == soz[0] or soz[i] == soz[-1]:
        new += soz[i]
    else:
        new += "X"

print(new)
