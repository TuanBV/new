import base64
import json
import falcon
import falcon.asgi
from admin.model import connect

from admin.model import get_all_user, delete_user, update_user
from admin.model import get_user_by_iduser
from hook.permission import Permission

class User:
    # get user by iduser
    async def on_get(self, req, resp, username, iduser):
        user = get_user_by_iduser(iduser)
        if user == []:
            resp.text = json.dumps({'error': 'ID user not found'})
        else:
            user[0].pop("password")
            resp.text = json.dumps(user)
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_OK

    # update user
    @falcon.before(Permission("admin"), is_async=True)
    async def on_put(self, req, resp, username, iduser):
        user = get_user_by_iduser(iduser)
        if user == []:
            resp.text = json.dumps({'error': 'ID user not found'})
        else:
            param = await req.media
            fullname = param['fullname']
            birthday = param['birthday'] if param['birthday'] else '0000-00-00'      
            address = param['address']
            idposition = param['idposition']
            update_user(fullname, birthday, address, idposition, iduser)
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_OK
        resp.text = json.dumps({'status': resp.status})

    # delete user
    # @falcon.before(Permission("admin"), is_async=True)
    async def on_delete(self, req, resp, username, iduser):
        user = get_user_by_iduser(iduser)
        if user == []:
            resp.status = falcon.HTTP_400
            resp.text = json.dumps({'error': 'ID user not found'})
        else:            
            delete_user(iduser)
            resp.status = falcon.HTTP_200
            resp.text = json.dumps({'status': resp.status})
        resp.content_type = falcon.MEDIA_JSON
