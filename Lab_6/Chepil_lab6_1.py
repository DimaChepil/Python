spysok = input('Введіть список: ').split()
count = 0
for i in spysok:
    if int(i) < 0:
        print(i,end=' ')
        count += 1       
print("\nКількість від'ємних елементів: ", count)


