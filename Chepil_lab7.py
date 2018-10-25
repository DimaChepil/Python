# Створення прикладних програм на мові Python
# Лабораторна робота 7
# Chepil Dmytro, 15
print ('Створення прикладних програм на мові Python, Лабораторна 7')
print ('Chepil Dmytro, 15')

age = 0
price = 1

def showSpisok (**sp):
    for x in sp:
        print ('{} - вік: {}, ціна: {}$'.format(x, sp[x][age], sp[x][price]) )

def SerPrice (*sp):
    aprice = 0
    k = 0
    average = 0
    for x in A:
        if A[x][age] > 6:
            aprice += A[x][price]
            k += 1
            average = aprice / k
    return average
    

A = {
    'Авто1': [4,100],
    'Авто2': [2,2364],
    'Авто3': [6,13256],
    'Авто4': [10,8754],
    'Авто5': [14,1321],
    'Авто6': [1,4465],
    'Авто7': [9,632],
    'Авто8': [3,2346],
    'Авто9': [12,6794],
    'Авто10': [4,3297]
    }

showSpisok(**A)
print('Середня вартість авто старше 6 років: ',SerPrice(*A))


