import datetime
import random
import math
import string
import hashlib
import re
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# create password random
def random_password():
    chars_fixed = string.ascii_letters + string.digits
    password = "".join(random.choice(chars_fixed) for x in range(random.randint(8, 15)))
    return password

# hash password use sha512
def make_pw_hash(password):
    return hashlib.sha512(str.encode(password)).hexdigest()
    
def check_pw_hash(password, hash):
    return True if make_pw_hash(password)==hash else False

#create token
def create_OTP():
    digits = [i for i in range(0, 10)]
    IDtoken = ""
    for i in range(6):
        index = math.floor(random.random() * 10)
        IDtoken += str(digits[index])
    return IDtoken

#check email valid
def check_email(email):
    return True if(re.fullmatch(regex, email)) else False

# check birthday 
def check_birthday(birthday):
    birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')
    return False if birthday > datetime.date.today() else True

def send_email(receiver_email, title, text):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = 'bui.tuan.10051998@gmail.com'  # Enter your address
    # Create a multipart message and set headers
    message = MIMEMultipart("alternative")
    message["Subject"] = title
    message["From"] = sender_email
    message["To"] = receiver_email
    content = MIMEText(text, 'plain')
    message.attach(content)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, "Tuan1005")
        server.sendmail(sender_email, receiver_email, message.as_string())