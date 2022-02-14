import json
from time import time
import falcon
import falcon.asgi

from manager.model import connect
from hook.permission import Permission

from admin.model import get_timerate_by_idtime, get_timerate_by_nameTime, update_timerate, delete_timerate
# get time rate by id
class Timerate:
    async def on_get(self, req, resp,username, idtime):
        timerate = get_timerate_by_idtime(idtime)
        if timerate == []:
            resp.status = falcon.HTTP_400
            resp.tetx = json.dumps({'status': resp.status})
        else:
            resp.text = json.dumps(timerate)
            resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON

    # @falcon.before(Permission("admin"), is_async=True)
    async def on_put(self, req, resp,username, idtime):
        param = await req.media
        id = param['id']
        timerate = get_timerate_by_idtime(idtime)
        if timerate == []:
            resp.status = falcon.HTTP_404
            resp.text = json.dumps({'message': 'ID time rate not found'})
        else:
            nameTime = param['nameTime']
            timeStart = param['timeStart']
            timeEnd = param['timeEnd']
            update_timerate(nameTime, timeStart, timeEnd, idtime)
            resp.status = falcon.HTTP_200
            resp.text = json.dumps({'status': resp.status})
        resp.content_type = falcon.MEDIA_JSON

    # @falcon.before(Permission("admin"), is_async=True)
    async def on_delete(self, req, resp, username, idtime):
        # param = await req.media
        # id = param['id']
        timerate = get_timerate_by_idtime(idtime)
        if timerate == []:
            resp.status = falcon.HTTP_404
            resp.text = json.dumps({'message': 'ID time rate not found'})
        else:
            # delete time rate
            delete_timerate(timerate[0]['idtime'])
            resp.status = falcon.HTTP_200
            resp.text = json.dumps({'status': resp.status})
        resp.content_type = falcon.MEDIA_JSON
    
# check name time alreadly exist
class NameTime:
    async def on_get(self, req, resp):
        param = req.params
        nameTime = param['nameTime']
        idtime = param['idtime']
        filter_nameTime = get_timerate_by_nameTime(nameTime)
        if filter_nameTime == []:
            resp.text = json.dumps({'status': resp.status})
            resp.status = falcon.HTTP_200 
        else:
            if int(idtime) == int(filter_nameTime[0]['idtime']):
                resp.status = falcon.HTTP_200
                resp.text = json.dumps({'status': resp.status})
            else: 
                resp.status = falcon.HTTP_400 
                resp.text = json.dumps({'status': resp.status})
        resp.content_type = falcon.MEDIA_TEXT 
from admin.model import get_timerate
class NameTimeOfTimerate:
    async def on_get(self, req, resp):
        data = get_timerate()
        resp.status = falcon.HTTP_200
        resp.text = json.dumps(data)
        resp.content_type = falcon.MEDIA_TEXT 