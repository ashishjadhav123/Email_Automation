import imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com')

email = input("Please enter your email address: ")
password = input("Please enter your password: ")

M.login(email, password)

print(M.list())

typ, data = M.search(None, 'FROM "jadhavashish028@gmail.com"')
print(data)