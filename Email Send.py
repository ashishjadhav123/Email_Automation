import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

print(smtp_object.ehlo())

print(smtp_object.starttls())

email = input("Please enter your email address: ")
password = input("Please enter your password: ")

smtp_object.login(email, password)

from_address = email
to_address = email

subject = input("Enter your subject: ")
body = input("Enter your body: ")
message = "Subject " + subject + "\n" + body

smtp_object.sendmail(from_address, to_address, message)
