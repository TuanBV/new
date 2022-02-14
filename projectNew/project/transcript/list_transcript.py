import json
import re
import falcon
import falcon.asgi
from transcript.model import get_transcript
# get list transcript
class ListTranscript:
    async def on_get(self, req, resp, username):
        param = req.params
        nameTime = param['nameTime']
        status = param['status']
        sumScoreUser = param['scoreUser']
        sumResultManager = param['scoreManager']
        
        pagination = int(param['page'])-1
        limit = int(param['limit'])
        sort = param['sort']
        try:
            data = get_transcript(username, pagination, limit, nameTime, status, sumScoreUser, sumResultManager, sort)
            if data != []:
                resp.status = falcon.HTTP_200
                for i in data['data']: 
                    i.pop('password')
                resp.text = json.dumps(data)
            else: 
                resp.status = falcon.HTTP_404
                resp.text = json.dumps({'status': resp.status})
        except Exception as e:
            print(e)
        resp.content_type = falcon.MEDIA_JSON