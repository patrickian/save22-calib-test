def add(fno,lno):
	#if not isinstance(fno,int):
       	return fno + lno

def subtract(fno,lno):
        return fno - lno

def multiply(fno,lno):
        return fno * lno

def divide(fno,lno):
        return fno / lno

def operator(fno,lno,op):
        if op == '+': return add(fno,lno)
        elif op == '-': return subtract(fno,lno)
        elif op == '*': return multiply(fno,lno)
        elif op == '/': return divide(fno,lno)
        else: print 'Invalid operator.\n'
        return None

def input1():
	return raw_input("Enter 1st number : ")

def input2():
        return raw_input("Enter 2nd number : ")

def inputope():
        return raw_input("Enter operation : ")

def output(n1,n2,ope,ans):
	return ('{} {} {} = {}').format(n1,ope,n2,ans)

def main():
        n1 = input1()
	n2 = input2()
	ope = inputope()
	ans = operator(n1,n2,ope)
	print output(n1,n2,ope,ans)


if __name__ == '__main__':
  main()

