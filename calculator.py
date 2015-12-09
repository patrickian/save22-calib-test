def add(fno,lno):
	return int(fno) + int(lno)

def subtract(fno,lno):
	return int(fno) - int(lno)

def multiply(fno,lno):
	return int(fno) * int(lno)

def divide(fno,lno):
	return int(fno) / int(lno)

def funcInput():
	eq = raw_input('Enter your equation(separated with space) : ')
	try:
		fno,op,lno = eq.split()
		if op == '+':
			return add(fno,lno)
		elif op == '-':
			return subtract(fno,lno)
		elif op == '*':
			return multiply(fno,lno)
		elif op == '/':
			return divide(fno,lno)
		else: print 'Invalid operator.\n'
	except:
		print 'Invalid equation.'
	return
	
def main():
	while True:
		ans = funcInput()
		print 'The answer is : ',
		print ans

if __name__ == '__main__':
  main()
