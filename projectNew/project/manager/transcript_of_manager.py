from distutils.log import info
import json
import falcon
import falcon.asgi
from manager.model import get_transcript_of_manager, update_trancript_of_manager, update_tieuchi_od_manager
from transcript.model import get_user_by_idtranscript
from helper.functions import send_email
from hook.permission import Permission
import mail_template.manager_reject
import mail_template.manager_confirm
class TranscriptOfManager:
    # get list transcript for manager
    # @falcon.before(Permission('manager'), is_async=True)
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
            data = get_transcript_of_manager(pagination, limit, nameTime, status, sumScoreUser, sumResultManager, sort)
            if data != []:
                resp.status = falcon.HTTP_200
                resp.text = json.dumps(data)
            else: 
                resp.status = falcon.HTTP_404
                resp.text = json.dumps({'status': resp.status})
        except Exception as e:
            print(e)
        resp.content_type = falcon.MEDIA_JSON
    # confirm or reject transcript
    # @falcon.before(Permission('manager'), is_async=True)
    async def on_put(self, req, resp, username):
        param = await req.media
        infors = param['infors'][0]
        targets = param['targets']
        # infor transcript
        idtranscript = infors['idtranscript']
        status = infors['status']
        sumResultManager = infors['sumResultManager']
        ghichu = infors['ghichu']
        # score targets
        member = get_user_by_idtranscript(idtranscript)
        if status == 3:
            # send email for user when manager reject transcript
            receiver_email =  member[0]['email']
            title = "The Transcript Not Approved !!"
            text = mail_template.manager_reject.BODY_TEXT.format(idtranscript, member[0]['username'], member[0]['fullname'], infors['nameTranscript'])
            send_email(receiver_email, title, text)
        if status == 2:
            # send email for user when manager confirm transcript
            receiver_email = member[0]['email']
            title = "Your Transcript Approved!!"
            text = mail_template.manager_confirm.BODY_TEXT.format(idtranscript, member[0]['username'], member[0]['fullname'], infors['nameTranscript'])
            send_email(receiver_email, title, text)
        # update status (sumResultManager, ghichu) of transcript
        update_trancript_of_manager(status, sumResultManager, ghichu, idtranscript)
        # update score QLDanhGia, NhanXet of manager
        for target in targets:
            for standard in target['standard']:
                update_tieuchi_od_manager(standard['TuDanhGia'], standard['QLDanhGia'], standard['NhanXet'], idtranscript, standard['idstandard'])
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_OK
        resp.text = json.dumps({'status':resp.status})
