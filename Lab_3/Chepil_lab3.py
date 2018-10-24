# Створення прикладних програм на мові Python
# Laboratorna 3
# Dmytro Chepil, Number 15
from math import *
print ('Створення прикладних програм на мові Python, Laboratorna 3')
print ('Dmytro Chepil, Number 15')
print('Введи:')
x = float(input('x = '))
b = float(input('b = '))
if not(2*b) or not(pow(b,2)):
    print('Значення змінних виходять за область визначення функції!')
else:
    result = (sqrt(x-b))/(2*b)-(tan(x)/pow(b,2))
    print('Результат обчислення = ', result)
