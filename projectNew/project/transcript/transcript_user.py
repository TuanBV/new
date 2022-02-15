import json
import falcon
import falcon.asgi
import mail_template.user_complete
from transcript.model import get_manager
from manager.model import get_full_by_idtranscript
from transcript.model import get_user_by_idtranscript
from admin.model import get_manager_by_censor
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
        infors = param['infors']
        targets = param['targets']
        # infor transcript
        status = int(infors[0]['status'])
        sumScoreUser = int(infors[0]['sumScoreUser'])
        censor = infors[0]['censor']
        opinion = infors[0]['opinion']
        timework = infors[0]['timework']
        timeworkend = infors[0]['timeworkend']
        # score targets
        targets = param['targets']
        for target in targets:
            # update tieuchi
            for standard in target['standard']:
                update_tieuchi(standard['TuDanhGia'], idtranscript, standard['idstandard'])
        transcript = get_full_by_idtranscript(idtranscript)
        manager_by_censor = get_manager_by_censor(censor)
        if opinion == "" or opinion == None:
            # update sumScoreUser, timework, timeworkend when user confirm transcript
            user_confirm_transcript(sumScoreUser, timework, timeworkend, idtranscript)
        else:
            # update opinion when manager confirm transcript
            user_complete_transcript(opinion, idtranscript)
            try: 
                data = get_user_by_idtranscript(idtranscript)
                # send email for mail system when user update opinion 
                receiver_email = "tuanbv@saisystem.vn"
                title = "Employee Complete Assessment"
                text = mail_template.user_complete.BODY_TEXT.format(data[0]['iduser'], data[0]['username'], data[0]['fullname'], data[0]['nameTranscript'])
                send_email(receiver_email, title, text)
            except Exception as e:
                print(e)  
        if status == 1:
            # update status and censor transcript
            update_transcript(manager_by_censor[0]['username'], status, idtranscript)
            # send email for manager when user confirm transcript
            receiver_email = manager_by_censor[0]['email']
            title = "Pending Transcipt!"
            text = mail_template.user_confirm.BODY_TEXT.format(transcript[0]['iduser'], transcript[0]['username'], transcript[0]['fullname'], transcript[0]['nameTranscript'])
            send_email(receiver_email, title, text)
        elif status == 4:
            if censor != '':
                update_transcript(manager_by_censor[0]['username'], status, idtranscript)
            else:
                censor = ''
                update_transcript(censor,status, idtranscript)
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_200
        resp.text = json.dumps({'status': resp.status})