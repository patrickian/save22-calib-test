def funcName(x):	return x[0]
def funcAge(x): return x[1]

def main():
	listahan = {'Homer':39, 'Bart':45, 'Butters':10, 'Carack':9,'Tiptiptop': 70 , 'Asd':135 , 'Qwe':93 ,'Zxc':56 , 'Brunette': 68,'Latinha':87,'Tektite':100}
	while True:
		print '1. Function sort using name.'
		print '2. Function sort using age.'
		print '3. Lambda sort using name.'
		print '4. Lambda sort using age.'

		inp = input('Input choice:')

		if inp == 1: print sorted(listahan.items() , key = funcName)
		elif inp == 2: print sorted(listahan.items() , key = funcAge)
		elif inp == 3: print sorted(listahan.items() , key =  lambda x : x[0])
		elif inp == 4: print sorted(listahan.items() , key =  lambda x : x[1])
		else: print 'invalid input.\n'

if __name__ == '__main__':
  main()
