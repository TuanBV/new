import json
import falcon
import falcon.asgi
from hook.permission import Permission
from admin.model import get_timerate_of_admin
from admin.model import get_record_end_of_timerate, get_idKiDanhGia_from_bangdiem, get_iduser_from_user, create_timerate_new, add_transcript_user, insert_tieuchi_for_transcript
from transcript.model import get_standard
from admin.model import get_timerate
import falcon
import falcon.asgi
# get list time rate
class ListTimeRate:
    # get list time rate of admin
    @falcon.before(Permission("admin"), is_async=True)
    async def on_get(self, req, resp, username):
        param = req.params
        nameTime = param['name']
        pagination = int(param['page'])-1
        limit = param['limit']
        sort = param['sort']
        try:
            data = get_timerate_of_admin(pagination, limit, nameTime, sort)
            if data != []:
                resp.status = falcon.HTTP_200
                resp.text = json.dumps(data)
            else: 
                resp.status = falcon.HTTP_404
                resp.text = json.dumps({'status': resp.status})
        except Exception as e:
            print(e)
        resp.content_type = falcon.MEDIA_JSON
        
    # add time rate new
    # @falcon.before(Permission("admin"), is_async=True)
    async def on_post(self, req, resp, username):
        dbTimeRate = get_timerate()
        timerate_new = await req.media
        nameTimeNew = timerate_new['nameTime']
        timeStartNew = timerate_new['timeStart']
        timeEndNew = timerate_new['timeEnd']
        if len(nameTimeNew) == 0 or len(nameTimeNew) > 200:
            resp.content_type = falcon.MEDIA_JSON
            resp.status = falcon.HTTP_400
            resp.text = json.dumps({'status': resp.status, 'content': 'Please enter no more than 200 characters'})             
        if timeStartNew == '':
            resp.content_type = falcon.MEDIA_JSON
            resp.status = falcon.HTTP_400
            resp.text = json.dumps({'status': resp.status, 'content': 'Please choose time start'})
        if timeEndNew == '' :
            resp.content_type = falcon.MEDIA_JSON
            resp.status = falcon.HTTP_400
            resp.text = json.dumps({'status': resp.status, 'content': 'Please choose time end more than time start'})
        if  len(nameTimeNew) > 0 and len(nameTimeNew) < 200 and timeStartNew != '' and timeEndNew != '':
            filter_nameTime = list(filter(lambda x : x['nameTime'] == str(nameTimeNew), dbTimeRate))
            if filter_nameTime == []:
                create_timerate_new(nameTimeNew, timeStartNew, timeEndNew)
                data = get_timerate()
                idTimeRate = get_record_end_of_timerate()
                b = idTimeRate[0]['idtime']
                try:
                    dbidtranscritp_old = get_idKiDanhGia_from_bangdiem()
                    #insert data to the table bangdiem
                    db = get_iduser_from_user()
                    for i in db:
                        a = i['iduser']
                        add_transcript_user(nameTimeNew,b,a)
                except Exception as e:
                    print(e)   
                try:
                    #insert data to the tieuchi 
                    dbidtranscript_new = get_idKiDanhGia_from_bangdiem()
                    dbstandard = get_standard()
                    for i in dbidtranscript_new:
                        if i not in dbidtranscritp_old:
                            idtranscript = i['idtranscript']
                            for k in dbstandard:
                                idstandard = k['id']
                                nameStandard = k['standard']
                                scoreStandard = k['score']
                                insert_tieuchi_for_transcript(nameStandard, scoreStandard, idtranscript,idstandard)
                except Exception as e:
                    print(e)
                resp.content_type = falcon.MEDIA_JSON
                resp.status = falcon.HTTP_OK
                resp.text = json.dumps({'status': resp.status})
            else:
                resp.content_type = falcon.MEDIA_JSON
                resp.status = falcon.HTTP_400
                resp.text = json.dumps({'status': resp.status})