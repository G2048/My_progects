character = '*'
rows_number = 5

if not (character.endswith(' ')):
	character += ' '

for i in range(rows_number):
	print(" "*i + character*(rows_number - i))

for j in range(1, rows_number + 1):
	print(" "*(rows_number - j) + character * j)
