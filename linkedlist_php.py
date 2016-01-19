import urllib
s='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
b='63579'
while 1:
	a = urllib.urlopen(s+b).read()
	h = a.split()
	b = h[-1]
	print a