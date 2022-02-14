from audioop import add
import base64
from datetime import datetime, date
import json
from lib2to3.pgen2.token import LESS
import falcon
import falcon.asgi
from admin.model import connect
from admin.model import get_user
from admin.model import get_timerate

from admin.model import get_all_user, validate_username, validate_email, get_iduser_new, create_user_new, add_timerate_for_user_new
from admin.model import get_iduser_new
from helper.functions import random_password, make_pw_hash, send_email, check_email
from hook.permission import Permission
import mail_template.create_user
class ListUser:
    #get list user
    # @falcon.before(Permission("admin"), is_async=True)
    async def on_get(self, req, resp, username):
        try:
            param = req.params
            position = param["position"]
            year = param["year"]
            name = param["name"]

            pagination = int(param['page'])-1
            sort = param['sort']
            limit = param['limit']
            data = get_user(pagination, limit, position, year, name, sort)
            if data == []:
                resp.status = falcon.HTTP_404
                resp.text = json.dumps(data)
            else:
                resp.status = falcon.HTTP_200
                for user in data['data']:
                    user.pop("password")
                resp.text = json.dumps(data)
        except Exception as e:
            print(e)
        resp.content_type = falcon.MEDIA_JSON
        
    # add user new
    # @falcon.before(Permission("admin"), is_async=True)
    async def on_post(self, req, resp, username):
        data = await req.media
        fullname = data['fullname']
        username = data['username']
        password = random_password()
        email = data['email']
        birthday = data['birthday'] if data['birthday'] else '0000-00-00'      
        address = data['address']
        idposition = int(data['idposition'])
        # -------
        search_username = validate_username(username)
        search_email = validate_email(email)
        if search_username == [] and search_email == []:
            try:
                # create user new
                create_user_new(fullname, username, make_pw_hash(password), email, birthday, address, idposition)
                # send email for user
                receiver_email = email
                title = "User new !"
                link = 'http://127.0.0.1:5500/view/sign-in.html'
                text = mail_template.create_user.BODY_TEXT.format(username, fullname, password, link)
                send_email(receiver_email, title, text)
                time_add_user_new = datetime.strptime(str(date.today()), '%Y-%m-%d')
                # get time rate
                timerates = get_timerate()
                # get iduser of user new
                iduser_new = get_iduser_new()
                for timerate in timerates:
                    tStart = datetime.strptime(timerate['timeStart'], '%Y-%m-%d')
                    tEnd = datetime.strptime(timerate['timeEnd'], '%Y-%m-%d')
                    if time_add_user_new > tStart and time_add_user_new < tEnd:
                        # add transcript for user new
                        add_timerate_for_user_new(timerate['nameTime'], timerate['idtime'],iduser_new)
            except Exception as e:
                print(e)
            resp.content_type = falcon.MEDIA_JSON
            resp.status = falcon.HTTP_200
            resp.text = json.dumps({'status': resp.status})
        else:
            if search_username : message='Username already exist !'
            if search_email : message='Email already exist !'
            resp.content_type = falcon.MEDIA_JSON
            resp.status = falcon.HTTP_400
            resp.text = json.dumps({'status': resp.status, 'content': message})

# check username --- sua lai ten
class CheckUsername:
    async def on_get(self, req, resp):
        data = req.params
        username = data['username']
        filter_username = validate_username(username)
        if filter_username != []:
            resp.status = falcon.HTTP_400  
            resp.text = json.dumps({'status': resp.status, 'content': 'Username already exist !'})
        else:    
            resp.status = falcon.HTTP_200  
            resp.text = json.dumps({'status': resp.status})
        resp.content_type = falcon.MEDIA_TEXT 

# check email
class CheckEmail:
    async def on_get(self, req, resp):
        data = req.params
        email = data['email']
        filter_email = validate_email(email)
        if filter_email != []:
            resp.status = falcon.HTTP_400  
            resp.text = json.dumps({'status': resp.status, 'content': 'Email already in used !'})
        else:
            resp.status = falcon.HTTP_200  
            resp.text = json.dumps({'status': resp.status})
        resp.content_type = falcon.MEDIA_TEXT       


# if len(fullname) > 100 or len(username) == 0 or len(username) > 30 or len(email) > 100 or check_email(email) or len(idposition) == 0 or len(address) > 200:
#     if len(fullname) > 100 : 
#         message = 'Please enter max 100 characters'
#     if len(username) > 0 or len(username) == 0 : 
#         message = 'Please enter max 100 characters'
#     if len(email) > 100 or check_email(email) == False: 
#         message = 'Please confirm email more than 100 characters'
#     if len(address) > 200 : 
#         message = 'Please confirm address more than 200 characters'
#     if len(idposition) > 100 : 
#         message = 'Please choose position'
#     resp.content_type = falcon.MEDIA_JSON
#     resp.status = falcon.HTTP_400
#     resp.text = json.dumps({'status': resp.status, 'content': message})
