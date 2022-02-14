import falcon
import falcon.asgi
from middleware.middleware import Middleware
from middleware.log import LogMiddleware
from common.login import Login
from common.forgot_password import ForgotPassword, CheckOTP, UpdatePasswordNew
from common.change_password import ChangePassword
from transcript.list_transcript import ListTranscript
from transcript.transcript_user import Standard, StandardResource, Target, Receiver
from transcript.transcript_user import Transcript
from manager.transcript_of_manager import TranscriptOfManager
from admin.list_user import CheckUsername, CheckEmail, ListUser
from admin.user import User
from admin.timerate import NameTime, NameTimeOfTimerate, Timerate
from admin.detail_timerate import TranscriptByTimerate
from admin.list_timerate import ListTimeRate

app = falcon.asgi.App(cors_enable=True)
app = falcon.asgi.App(middleware=[falcon.CORSMiddleware(allow_origins='*', allow_credentials='*', expose_headers='Authorization'), LogMiddleware(), Middleware()])
# app = falcon.asgi.App()
# login
app.add_route('/users/login/{username}', Login())
#transcript #------------member---------------
app.add_route('/user/{username}/transcript', ListTranscript())
app.add_route('/user/{username}/transcript/{idtranscript}', Transcript())
app.add_route('/standard', Standard())
app.add_route('/standard/{id}', StandardResource())
app.add_route('/target', Target())
app.add_route('/receiver',Receiver())
#change password
app.add_route('/user/{username}/change-password', ChangePassword())
# forgot password
app.add_route('/forgot-password', ForgotPassword())
app.add_route('/checkotp', CheckOTP())
app.add_route('/updatepwnew', UpdatePasswordNew())
#------------manager---------------
app.add_route('/manager/{username}/transcript', TranscriptOfManager())
# user #------------admin---------------
app.add_route('/admin/{username}/users', ListUser())
app.add_route('/admin/{username}/users/{iduser}', User())
# check username
app.add_route('/check-username', CheckUsername())
app.add_route('/check-email', CheckEmail())
# get list transcript by time rate
app.add_route('/admin/{username}/timerate/{idtime}/transcript', TranscriptByTimerate())
# time rate
app.add_route('/admin/{username}/timerate', ListTimeRate())
app.add_route('/admin/{username}/timerate/{idtime}', Timerate())
#check name time
app.add_route('/nametime', NameTime())
# condition name time of time rate
app.add_route('/condition-nametime', NameTimeOfTimerate())

