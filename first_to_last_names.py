first_names = ['Shan', 'Dao Ming', 'Hua Ze', 'Xi', 'Mei']
last_names = ['Cai', 'Si', 'Lei', 'Men', 'Zuo']
ctr = 0
fullname = []
for x in last_names:
	fullname.append(first_names[ctr] + " " + x)
	ctr+=1
print fullname
