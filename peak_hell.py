import pickle 
a = pickle.load(open('banner.p'))
for lst in a:
	for item in lst:
		print item[0] * item[-1],
	print ""