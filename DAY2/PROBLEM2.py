a = 17391 % 17
b = 546 % 17
c = 934 % 17

if a < b and a < c:
	print ('a small')
elif b < a and b < c:
	print('b small')
elif c < b and c < a:
	print('c small')	 
else:
	print('est odinalovye')
