def func(col,row):
	col = row if col is None else col
	row = col if row is None else row
	return col, row

def swap_eqs(lin_sys, num_of_vars, row, i):
	eq1 = lin_sys[row]
	eq2 = lin_sys[i]
	for j in range(num_of_vars):
		eq1[j], eq2[j] = eq2[j], eq1[j]


def find_nonzero(lin_sys, num_of_vars, num_of_eqs, col = None, row = None):
	col, row = func(col,row)
	if col >= num_of_vars or row >= num_of_eqs
	if lin_sys[row][col] == 0:
		return
	for i in range(row, num_of_eqs):
		if lin_sys[i][col] != 0:
			swap_eqs(lin_sys, num_of_vars, row, i)

def make_one(lin_sys, num_of_vars, num_of_eqs, col = None, row = None):
	func(col, row)

def column_to_zeros(lin_sys, num_of_vars, num_of_eqs, col = None, row = None):
	func(col, row)

def gaussian_eliminations(*args):
	lin_sys, num_of_vars, num_of_eqs = args
	args = lin_sys, num_of_vars+1, num_of_eqs
	i = 0
	while find_nonzero(args, col = i):
		make_one(args, row = i)
		column_to_zeros(args, col = i)
	return lin_sys


			
