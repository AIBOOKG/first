a = int(input())
b = int(input())
c = int(input())

if a > b and b > c:
	print('A BIG')
elif b > a and b > c:
	print('B BIG')
elif c > b and c > a:
	print('C BIG')
else:
	print('Есть равные числа')
