p = 'aaaa0000'
i = 3
while i > 0:
	f = input('請輸入密碼')
	if f == p:
		print('log in successfully')
		break	
	else:
		i = i - 1
		print('fail to log in, please re try')
		print('you still have', i, 'times')
print('program stop')