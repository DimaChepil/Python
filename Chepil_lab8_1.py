# Створення прикладних програм на мові Python
# Лабораторна робота 8_1
# Chepil Dmytro, 15
print ('Створення прикладних програм на мові Python, Лабораторна 8_1')
print ('Chepil Dmytro, 15')

def vezhi(n, d_1, d_2, d_3) :
  if (n == 0) : return
  vezhi(n-1,d_1,d_3,d_2)
  print('Кружок',n,'переміщений з', d_1, 'на' ,d_2)
  vezhi(n-1,d_3,d_2,d_1)
n = int(input('Введіть N = '))
vezhi(n,1,2,3)
print('Переміщень N =', n, ' ==> ',2**n-1)
