import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# creating a server and connecting to mail service provider with name and port
server = smtplib.SMTP('smtp.gmail.com', 25)

#starting the server
server.ehlo()

# the best practice to save the password in decrypted form in a test file and then read from that file to login
# with open('password.txt','r') as f:
#     password = f.read()

# now we are going to login in our gmail account
server.login('asifasif@student.iul.ac.in','gr8king@8423')

#now we are going to create a message
msg = MIMEText
msg['from'] = "WebdevAsif"
msg['To'] = 'asifasif@student.iul.ac.in'
msg['subject'] = 'Message through Python'

#reading the message from a text file
with open('msg.txt','r') as f:
    message = f.read()

#attaching the message to msg

msg.attach(MIMEText(message, 'plain'))

# attaching a image file with email
image = 'img.png'

#reading the image file in binary mode we cant use it as image
attachment = open(image, 'rb')

#creating a payload object using MIMEBase
p = MIMEBase('application', 'octet-stream')

p.set_payload(attachment.read())

encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachment; filename{image}')

msg.attach(p)

# getting whole thing as a string to send the mail
text = msg.as_string

server.sendmail('asifasif@student.iul.ac.in', 'mdasif08737@gmail.com')