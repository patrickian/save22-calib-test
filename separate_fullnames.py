full_names = ['Nobita Nobi', 'Shizuka Minamoto', 'Takeshi Goda', 'Suneo Honekawa']
last_names = []
first_names = []
for x in full_names:
	a,b = x.split()
	last_names.append(b)
	first_names.append(a)
print first_names
print last_names
