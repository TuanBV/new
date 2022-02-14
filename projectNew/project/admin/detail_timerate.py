import imp
import json
import falcon
import falcon.asgi
from hook.permission import Permission
from admin.model import get_transcritp_detailtimerate

# get list transcript by time rate of admin
class TranscriptByTimerate:
    @falcon.before(Permission("admin"), is_async=True)
    async def on_get(self, req, resp, username, idtime):
        param = req.params
        idtimerate = param['id']
        status = param['status']
        sumScoreUser = param['scoreUser']
        sumResultManager = param['scoreManager']
        pagination = param['pagination']
        limit = param['limit']
        sort = param['sort']
        try:
            data = get_transcritp_detailtimerate(idtimerate, pagination, limit, status, sumScoreUser, sumResultManager, sort)
            if data != []:
                resp.status = falcon.HTTP_200
                resp.text = json.dumps(data)
            else: 
                resp.status = falcon.HTTP_404
                resp.text = json.dumps({'status': resp.status})
        except Exception as e:
            print(e)
        resp.content_type = falcon.MEDIA_JSON 