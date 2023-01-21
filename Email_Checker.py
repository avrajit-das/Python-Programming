email = input("Enter your Email ID: ")
domain = '@gmail.com'
ledo = len(domain)
lema = len(email)
sub = email[lema-ledo:]
if sub == domain:
	if ledo != lema:
		print("It is a valid Email ID: ")
	else:
		print("This is a invalid Email ID: ")
else:
	print("This email ID is either not valid or belongs to some other domain. ")
	