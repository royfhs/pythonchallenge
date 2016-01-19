a=[]
i=0
s="map"
# s="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
while i<len(s):
	if ord(s[i])>96 and ord(s[i])<123:
		a.append(chr((ord(s[i])+2-97)%26+97))
	i+=1
print ''.join(a)
