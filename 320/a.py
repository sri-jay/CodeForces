data = raw_input()

data = data.replace("144","zzz").replace("14","zz").replace("1","z")

if len(data) == data.count("z"):
	print "YES"
else :
	print "NO"