import json
import falcon
import falcon.asgi
from manager.model import get_transcript_of_manager, get_full_by_idtranscript, connect, update_trancript_of_manager, update_standard_od_manager
from transcript.model import get_user_by_idrranscipt
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
        limit = param['limit']
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
        standards = param['db']
        sumResultManager = param['sumManager']
        ghichu = param['ghichu']
        status = param['status']
        censor = param['censor']
        id = param['id']
        transcript = get_full_by_idtranscript(id)
        if status == 3:
            member = get_user_by_idrranscipt(id)
            try: 
                # send email for user
                receiver_email =  member[0]['email'] # Enter receiver address
                title = "The Transcript Not Approved !!"
                text = mail_template.manager_reject.BODY_TEXT.format(transcript[0]['nameTranscript'], transcript[0]['username'], transcript[0]['fullname'], transcript[0]['nameTranscript'])
                send_email(receiver_email, title, text)
            except Exception as e:
                print(e)
        if status == 2:
            member = get_user_by_idrranscipt(id)
            # send email
            receiver_email = member[0]['email']
            title = "Your Transcript Approved!!"
            text = mail_template.manager_confirm.BODY_TEXT.format(transcript[0]['iduser'], transcript[0]['username'], transcript[0]['fullname'], transcript[0]['nameTranscript'])
            send_email(receiver_email, title, text)
        try: 
            update_trancript_of_manager(status, sumResultManager, ghichu, id)
            for standard in standards:
                idstandard = standard['id']
                QLDanhGia = standard['QLDanhGia'] 
                if standard['NhanXet'] == "":
                    NhanXet = ""
                    update_standard_od_manager(QLDanhGia,NhanXet, id, idstandard)
                else:
                    NhanXet = standard['NhanXet']
                    update_standard_od_manager(QLDanhGia, NhanXet, id, idstandard)
        except Exception as e:
            print(e)
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_OK
        resp.text = json.dumps({'status':resp.status})
