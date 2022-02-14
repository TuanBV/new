import json
import falcon
import falcon.asgi

import mail_template.user_complete
from manager.model import connect
from transcript.model import get_manager
from manager.model import get_full_by_idtranscript
from transcript.model import get_user_by_idrranscipt
from admin.model import get_manager_by_censor_email
from helper.functions import send_email
import mail_template.user_confirm
#Standard
from transcript.model import get_target, get_standard, update_tieuchi, update_transcript, user_confirm_transcript, user_complete_transcript
#Target
class Target:
    async def on_get(self, req, resp):
        dbtarget = get_target()
        resp.text = json.dumps(dbtarget)
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_OK
class Standard: 
    async def on_get(self, req, resp):
        dbstandard = get_standard()
        resp.text = json.dumps(dbstandard)
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_200
#----------------------------------------------------------- 
class StandardResource: 
    async def on_get(self, req, resp, id):
        dbstandard = get_standard()
        filter_standard = list(filter(lambda x : x['idtarget'] == int(id), dbstandard))
        resp.text = json.dumps(filter_standard)
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_200
#  load receiver
class Receiver:
    async def on_get(self, req, resp):
        manager = get_manager()
        resp.text = json.dumps(manager)
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
#----------------------------------------------------------- 
#get data transcript by idtranscript
# Transcript
class Transcript:
    # get information transcript of member
    async def on_get(self, req, resp, username, idtranscript):
        transcript = get_full_by_idtranscript(idtranscript)
        resp.text = json.dumps(transcript)
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_OK

    # send transcript for manager or save transcript
    async def on_put(self, req, resp, username, idtranscript):
        param = await req.media
        standards = param['db']
        id = param['id']
        sumUser = param['sumUser']
        opinion = param['opinion']
        censor_email = param['censor']
        status = param['status']
        timework = param['timework']
        timeworkend = param['timeworkend']
        # update standard
        transcript = get_full_by_idtranscript(id)
        try:
            for standard in standards:
                idstandard = standard['id']
                TuDanhGia = standard['TuDanhGia']
                update_tieuchi(TuDanhGia, id, idstandard)
        except Exception as e:
            print(e)  
        # update opinion when manager confirm transcript
        if opinion == "":
            user_confirm_transcript(sumUser, timework, timeworkend, id)
        else:
            user_complete_transcript(opinion, id)
            try: 
                data = get_user_by_idrranscipt(id)
                # send email
                receiver_email = "tuanbv@saisystem.vn"
                title = "Employee Complete Assessment"
                text = mail_template.user_complete.BODY_TEXT.format(data[0]['iduser'], data[0]['username'], data[0]['fullname'], data[0]['nameTranscript'])
                send_email(receiver_email, title, text)
            except Exception as e:
                print(e)  
        # send email for manager
        manager_by_censor_email = get_manager_by_censor_email(censor_email)
        try:
            if status == 1:
                update_transcript(manager_by_censor_email[0]['username'], status, id)
                # send email
                receiver_email = censor_email
                title = "Pending Transcipt!"
                text = mail_template.user_confirm.BODY_TEXT.format(transcript[0]['iduser'], transcript[0]['username'], transcript[0]['fullname'], transcript[0]['nameTranscript'])
                send_email(receiver_email, title, text)
            elif status == 4:
                if censor_email != '':
                    update_transcript(manager_by_censor_email[0]['username'], status, id)
                else:
                    censor = ''
                    update_transcript(censor,status, id)
        except Exception as e:
            print(e)
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_OK
        resp.text = json.dumps({'status': resp.status})