import base64
import falcon
import falcon.asgi

from admin.model import get_user_by_username
class Permission:
    def __init__(self, roles):
        self._roles = roles
    async def __call__(self, req, resp, resource, params):
        print(req.headers)
        # username = req.get_header('Authorization').split(' ')
        # base64_bytes = username[1].encode('ascii')
        # message_bytes = base64.b64decode(base64_bytes)
        # message = message_bytes.decode('ascii')
        # auth = get_user_by_username(message)
        # # check position of user
        # if auth[0]['name'] != self._roles:
        #     msg = 'Unauthorized'
        #     raise falcon.HTTPUnauthorized(msg)