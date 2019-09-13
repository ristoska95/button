# get user input
# input sender email address and password:
from_addr = input('From: ')
password = input('Password: ')
# input receiver email address.
to_addr = input('To: ')
# input smtp server ip address:
smtp_server = input('SMTP server: ')

# email object that has multiple part:
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = Header('hello world from smtp server', 'utf-8').encode()

# attache a MIMEText object to save email content
msg_content = MIMEText('send with attachment...', 'plain', 'utf-8')
msg.attach(msg_content)

# to add an attachment is just add a MIMEBase object to read a picture locally.
with open('/Users/jerry/img1.png', 'rb') as f:
    # set attachment mime and file name, the image type is png
    mime = MIMEBase('image', 'png', filename='img1.png')
    # add required header data:
    mime.add_header('Content-Disposition', 'attachment', filename='img1.png')
    mime.add_header('X-Attachment-Id', '0')
    mime.add_header('Content-ID', '<0>')
    # read attachment file content into the MIMEBase object
    mime.set_payload(f.read())
    # encode with base64
    encoders.encode_base64(mime)
    # add MIMEBase object to MIMEMultipart object
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()