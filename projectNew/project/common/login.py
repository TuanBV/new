from helper.functions import make_pw_hash
import json
import falcon
import falcon.asgi
from admin.model import get_user_by_username
import jwt
# login
class Login:
    async def on_get(self, req, resp, username):
        user = get_user_by_username(username)
        resp.text = json.dumps(user)
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_200
    async def on_post(self, req, resp, username):
        user = get_user_by_username(username)
        data = await req.media
        pw = make_pw_hash(data['password'])
        if user == []:
            resp.status = falcon.HTTP_404
            resp.text = json.dumps({'status': resp.status, 'message': 'Username does not exist !'})
        else:
            if pw == user[0]['password']:
                # set cookie in server
                try:
                    user[0].pop('password')
                    user[0].pop('idtoken')
                    user[0].pop('timetoken')

                    token = jwt.encode(user[0], "secret", algorithm="HS256")
                    resp.set_cookie('token', token, max_age=600, path='/', domain='localhost',secure=True, http_only=False, same_site=None)

                except Exception as e:
                    print(e)    
                resp.content_type = falcon.MEDIA_JSON
                resp.status = falcon.HTTP_200
                resp.text = json.dumps(user)
            else:  
                resp.status = falcon.HTTP_400
                resp.content_type = falcon.MEDIA_JSON
                resp.text = json.dumps({'status': resp.status, 'message': "Password is invalid !"})