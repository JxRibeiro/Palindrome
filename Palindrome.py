# Script to check if word is a palindrome

def checkPalindrome(txt):

	inverted = txt[::-1]
	if txt == inverted:
	   	print(f'{txt} is a palindrome!')
	else:
	   print(f'{txt} is not a palindrome!')
    

txt = str(input('Type a word and I will check if it is a palindrome: ')).lower()
checkPalindrome(txt)
