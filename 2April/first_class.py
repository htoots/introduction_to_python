

def factor_print():
	print "Enter the number to check factors of"
	x = int(raw_input())
	print("Factors of ", x, " are: ")
	for i in range(1, x+1):
		if x % i == 0:
			print(i)

factor_print()

def align_right():
	word=[20, 30, 40]
	print "Enter the right-align width"
	n = raw_input()
	#line_new = '{:>{n}}'.format(word[0], n=n), '{:>{n}}'.format(word[1], n=n), '{:>{n}}'.format(word[2],n=n)
	line_new = '{0:> {n}} {1:> {n}} {2:> {n}}'.format( word[0], word[1], word[2], n=n)
	print line_new
	

align_right()

'''
Shell code for printing first 16 powers of 2

for n in range(1, 17):
	print (2**n)
'''
