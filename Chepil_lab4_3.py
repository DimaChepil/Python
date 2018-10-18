a = int(input ('Input: a = '))

x1 = 2

eps = 10E-4

if a < 0:

	print('The number should be positive!')

else:

	while True:

		x2 = (x1 + a / x1) / 2

		if abs(x2 - x1) < eps:

			break

		else:

			x1 = x2

print("The root of 'a' according to the iterative formula of Geron: а = ", x2)

