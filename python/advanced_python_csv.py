from advanced_python_regex import emails

f = open('./emails.csv', 'w')

for email in emails:
	f.write(email + str('\n'))

f.close()