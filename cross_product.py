A = {'a','b'}
B = {'1','2'}
A_cross_B = set()
for a in A:
	for b in B:
		A_cross_B.add(tuple([a,b]))

A_cross_B
C = {'x','y'}
A_cross_B_cross_C = set()
for a in A:
	for b in B:
		for c in C:
			A_cross_B_cross_C.add(tuple([a,b,c]))


A_cross_B_cross_C

