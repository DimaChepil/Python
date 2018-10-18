number = int(input ('Input number: '))

t = 1

k = 0

while True:

	if number / t < 1:

		break

	else:

		t *= 10

		k += 1

print('Number of digits: ', k)

