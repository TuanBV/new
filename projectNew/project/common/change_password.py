from asyncio import log
import json
import falcon
import falcon.asgi
from admin.model import get_user_by_username
from helper.functions import make_pw_hash
from common.model import update_password_new
#get data user by username
class ChangePassword:
    async def on_put(self, req, resp, username):
        search_user = get_user_by_username(username)

        if search_user == []:
            resp.status = falcon.HTTP_404
            resp.text = json.dumps({'status': resp.status,'content': "Not found username"})
        else:
            try:
                param = await req.media
                print(param)
                pwnow = param['password_now']
                pwnew = param['password_new']
                if make_pw_hash(pwnow) == search_user[0]['password']:
                    update_password_new(make_pw_hash(pwnew), search_user[0]['email'])
                    resp.status = falcon.HTTP_200
                    resp.text = json.dumps({'status': resp.status})
                else:
                    resp.status = falcon.HTTP_404
                    resp.text = json.dumps({'status': resp.status,'content': 'Invalid password'})
            except Exception as e:
                print(e)
        resp.content_type = falcon.MEDIA_JSON
