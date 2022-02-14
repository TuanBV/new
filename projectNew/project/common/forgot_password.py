import json
import datetime
from time import time
import falcon
import falcon.asgi
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from helper.functions import send_email, create_OTP, make_pw_hash
from admin.model import get_email, get_user_by_email
from common.model import check_token, create_token, update_password_new
import mail_template.forgot_password
# forgot password
class ForgotPassword:
    async def on_post(self, req, resp):
        db = get_email()
        data = await req.media
        email = data["email"]
        if email == "":
            resp.status = falcon.HTTP_400
            resp.text = json.dumps({'status': resp.status,'content':'Please enter your email'})
        else:
            filter_email = get_user_by_email(email)
            if filter_email == []:
                description = 'Email not authenticated'
                resp.status = falcon.HTTP_401
                resp.text = json.dumps({'status': resp.status,'content': description})
                resp.conetnt = falcon.MEDIA_JSON
            else:
                try:
                    # create token
                    tokenOTP = create_OTP()
                    timetoken = datetime.datetime.now()
                    create_token(tokenOTP, timetoken, email)
                    # send email
                    receiver_email = email  
                    title = "Personal email confirmation!!"
                    link = 'http://127.0.0.1:5500/view/forgot-password.html'+'?email='+receiver_email
                    text = mail_template.forgot_password.BODY_TEXT.format(tokenOTP, link)
                    send_email(receiver_email, title, text)
                except Exception as e:
                    print(e)
                resp.status = falcon.HTTP_200
                resp.text = json.dumps({'status': resp.status})
        resp.content_type = falcon.MEDIA_JSON

# check OTP
class CheckOTP:
    async def on_post(self, req, resp):
        param = await req.media
        email = param['email']
        idtoken = param['numberOTP']        
        filter_user = check_token(email, idtoken)
        t = datetime.datetime.strptime(filter_user[0]['timetoken'], '%Y-%m-%d %H:%M:%S')
        if filter_user == []:
            resp.status = falcon.HTTP_400
            resp.text = json.dumps({'status': resp.status})
        else:
            if datetime.datetime.timestamp(datetime.datetime.now()) - datetime.datetime.timestamp(t) > 300:
                resp.status = falcon.HTTP_404
                resp.text = json.dumps({'status': resp.status, 'content':'Time OTP over time'})
            else:
                resp.status = falcon.HTTP_200
                resp.text = json.dumps({'status': resp.status})
        resp.content_type = falcon.MEDIA_JSON

# update password new for user
class UpdatePasswordNew:
    async def on_post(self, req, resp):
        param = await req.media
        password = param['passwordnew']
        email = param['email']
        update_password_new(make_pw_hash(password), email)
        resp.status = falcon.HTTP_200
        resp.text = json.dumps({'status': resp.status})
        resp.content_type = falcon.MEDIA_JSON  
