import falcon
import logging
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class LogMiddleware():
    async def process_request(self, req, resp):
        if req.method != "OPTIONS":
            if req.method == "POST":
                dataRequest = (await req.media).copy()
                if 'password' in dataRequest.keys(): 
                    dataRequest.pop('password')
            else: 
                dataRequest = req.params
            logger.info('{0} | {1} | {2} | {3} | {4}'.format('[REQUEST]', req.method, req.relative_uri, dataRequest, resp.status[:3]))    
    async def process_response( self , req , resp , resource , req_succeeded):
        if req.method != "OPTIONS":
            dataResponse = resp.text
            logger.info('{0} | {1} | {2} | {3} | {4}'.format('[RESPONSE]', req.method, req.path, dataResponse , resp.status[:3]))

