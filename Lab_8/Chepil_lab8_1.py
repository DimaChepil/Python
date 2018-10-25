# Створення прикладних програм на мові Python
# Лабораторна робота 8_1
# Chepil Dmytro, 15
print ('Створення прикладних програм на мові Python, Лабораторна 8_1')
print ('Chepil Dmytro, 15')

def vezhi(n, a, b, c) :
  if (n == 0) : return
  vezhi(n-1,a,c,b)
  print('Кружок',n,'переміщений з', a, 'на' ,b)
  vezhi(n-1,c,b,a)
n = int(input('Введіть N = '))
vezhi(n,1,2,3)
print('Переміщень N =', n, ' ==> ',2**n-1)
