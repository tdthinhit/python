year = int(input('nam nhuan la: '))
if year % 4 == 0 and year % 400 != 0:
	print('{0} là năm nhuận'.format(year))
else:
	print('{0} không phải năm nhuận'.format(year))