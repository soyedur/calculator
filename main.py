con = True

while con:
	first = float(input('first number: '))
	oper = input('operator (+ - * /): ')
	sec = float(input('second number: '))

	if (oper == '+'):
		print(f'{first} + {sec} =', first + sec)
	elif (oper == '-'):
		print(f'{first} - {sec} =', first - sec)
	elif (oper == '*'):
		print(f'{first} * {sec} =', first * sec)
	elif (oper == '/'):
		print(f'{first} / {sec} =', first / sec)
	else:
		print('invalid input')
	
	con = input('again? (y/n) ')
	if (con == 'n'):
		con = False

print('goodbye')
