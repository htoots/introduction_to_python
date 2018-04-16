import sys

'''Caesar cipher'''


def translate(keysize, mode):

	plaintext = raw_input('Enter plain text message: ')

	translated = ''
	textvar = 'encrypted'
	if mode == 0:
		textvar = 'decrypted'
		keysize = -keysize

	for each in plaintext:
		if each.isalpha():
			num = ord(each)+keysize

			if each.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26

			elif each.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26

			translated += chr(num)
		else:
			translated += each
	if mode == 0:
		print 'Your ' + textvar + ' text message is: ' + translated
	else:
		print 'Your ' + textvar + ' text message is: ' + translated


def main(argv):
	if(len(sys.argv) != 3):
		sys.exit('Usage: cipher.py <key size 1-26> <(e)ncrypt or (d)ecrypt>')
	elif sys.argv[2] == 'e' and int(sys.argv[1]) >= 1 and int(sys.argv[1]) <= 26:
		translate(int(sys.argv[1]), 1)
	elif sys.argv[2] == 'd' and int(sys.argv[1]) >= 1 and int(sys.argv[1]) <= 26:
		translate(int(sys.argv[1]), 0)
	else:
		sys.exit('Error in arguments, use none for guide.')

if __name__ == "__main__":
	main(sys.argv[1:])