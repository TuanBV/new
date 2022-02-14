import falcon.asgi
import base64
import falcon
import logging
from admin.model import get_user_by_username, get_user_by_email
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Middleware():
    async def process_request(self, req, resp):
        pass
        # if req.method != "OPTIONS":
        #     if '/forgot-password'in req.path or '/updatepwnew' in req.path or '/checkotp' in req.path:
        #         token = req.get_header('email')
        #         message = base64.b64decode(token)
        #         message = message.decode('ascii')
        #         auth = get_user_by_email(message)
        #         if auth == []:
        #             description = 'Auth token required'
        #             raise falcon.HTTPUnauthorized(description)
        #     else:
                
        #         token = req.get_header('authorization').split(' ')
        #         message_bytes = base64.b64decode(base64_bytes)
        #         message = message_bytes.decode('ascii')
        #         auth = get_user_by_username(message)
        #         if auth == []:
        #             description = 'Auth token required'
        #             raise falcon.HTTPUnauthorized(description)
    
    async def process_response( self , req , resp , resource , req_succeeded):
        if req.method != "OPTIONS":
            dataResponse = resp.text
            logger.info('{0} | {1} | {2} | {3} | {4}'.format('[RESPONSE]', req.method, req.path, dataResponse , resp.status[:3]))
