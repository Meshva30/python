def calc_power(N, p):
	if p == 0:
		return 1
	return N * calc_power(N, p-1)

print(calc_power(4, 2))
