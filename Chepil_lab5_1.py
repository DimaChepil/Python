# Створення прикладних програм на мові Python
# Лабораторна робота 5
# Chepil Dmytro, 15
print ('Створення прикладних програм на мові Python, Лабораторна 5')
print ('Chepil Dmytro, 15')
N = int(input ('Введіть число: '))
proste = 0
while proste < N:
    proste2 = proste + 6
    x = 0
    y = 0
    for j in range(1,proste+1):
        if proste % j == 0:
            x += j
    if x-1 == proste:
        for j in range(1,proste2+1):
            if proste2 % j == 0:
                y += j
        if y-1 == proste2:
            print('(',proste, proste2, end = ' ) ')
    proste += 1
