n=input("enter the char").lower()
if n in ['a', 'e', 'i', 'o', 'u']:
	print("vowel")
elif '0'<=n<='9':
	print("digit")
elif 'a'<=n<='z':
	print('consonent')
else :
	print("special character")