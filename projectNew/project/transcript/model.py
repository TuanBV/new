from asyncio import QueueEmpty
from manager.model import connect
# ------------------- not injection 
#transcript user
def get_transcript(username,pagination, limit,nameTime, status, sumScoreUser,sumResultManager, sort):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    data = {}
    query = 'select * from bangdiem join user on bangdiem.iduser=user.iduser where username="%s"'%username
    if nameTime != "all":
        query += ' and nameTranscript=%(nameTime)s'
        data['nameTime'] = nameTime
    if status != "all":
        query += ' and status=%(status)s'
        data['status'] = int(status)
    if sumScoreUser != '':
        query += ' and sumScoreUser>%(sumScoreUser)s'
        data['sumScoreUser'] = int(sumScoreUser)
    if sumResultManager != '':
        query += ' and sumScoreUser>%(sumResultManager)s'
        data['sumResultManager'] = int(sumResultManager)
    if sort == 'nameTranscriptAsc':
        query += ' order by nameTranscript ASC'
    if sort == 'nameTranscriptDesc':
        query += ' order by nameTranscript DESC'
    if sort == 'sumUserAsc':
        query += ' order by sumScoreUser ASC'
    if sort == 'sumUserDesc':
        query += ' order by sumScoreUser DESC'
    if sort == 'sumManagerAsc':
        query += ' order by sumResultManager ASC'
    if sort == 'sumManagerAsc':
        query += ' order by sumResultManager DESC'
    cursor.execute(query, data)
    count = cursor.fetchall()
    pagination = int(limit)*int(pagination)
    query +=  ' limit %(pagination)s,%(limit)s'
    data['pagination'] = pagination
    data['limit'] = limit

    cursor.execute(query, data)
    db = cursor.fetchall()
    for i in db:
        i['birthday'] = str(i['birthday'])
        i['timetoken'] = str(i['timetoken'])
        i['timework'] = str(i['timework'])
        i['timeworkend'] = str(i['timeworkend'])
    conn.close()
    return {'data': db, 'count': len(count)}
#Standard
def get_standard():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('select * from standard')
    db = cursor.fetchall()
    conn.close()
    return db
#target
def get_target():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('select * from target')
    db = cursor.fetchall()
    conn.close()
    return db
# get information receiver
def get_manager():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select * from user where idposition=2'
    cursor.execute(query)
    db = cursor.fetchall()
    for i in db:
        i.pop('password')
        i.pop('idtoken')
        i.pop('timetoken')
        i['birthday'] = str(i['birthday'])
    conn.close()
    return db
# get data from bangdiem - kidanhgia - position
def get_transcript_join_timerate():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('select * from ((bangdiem join user on bangdiem.iduser = user.iduser) join kidanhgia on bangdiem.idKiDanhGia = kidanhgia.idTime) join position on user.idposition = position.idposition')
    db = cursor.fetchall()
    conn.close()
    for i in db:
        i['birthday'] = str(i['birthday'])
        i['timeStart'] = str(i['timeStart'])
        i['timeEnd'] = str(i['timeEnd'])
        i['timetoken'] = str(i['timetoken'])
        i['timework'] = str(i['timework'])
        i['timeworkend'] = str(i['timeworkend'])
    return db
# get information user by idtranscript
def get_user_by_idtranscript(idtranscript):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select * from bangdiem join user on bangdiem.iduser=user.iduser where idtranscript=%s'
    cursor.execute(query,(idtranscript,))
    db = cursor.fetchall()
    conn.close()
    return db
# update tieuchi
def update_tieuchi(TuDanhGia, idtranscript, idstandard):
    conn = connect()
    cursor = conn.cursor()
    query = "update tieuchi set TuDanhGia=%s where idBangDiem=%s and idstandard=%s"
    cursor.execute(query,(TuDanhGia, idtranscript, idstandard,))
    conn.commit()
    conn.close()

# update censor and status of transcript
def update_transcript(censor, status, idtranscript):
    conn = connect()
    cursor = conn.cursor()
    data = {}
    query = 'update bangdiem set status=%(status)s'
    data['status'] = int(status)
    if censor!= "":
        query += ',censor=%(censor)s'
        data['censor'] = censor
    query += ' where idtranscript=%(idtranscript)s'
    data['idtranscript'] = idtranscript
    cursor.execute(query,data)
    conn.commit()
    conn.close()
# user confirm transcript
def user_confirm_transcript(sumScoreUser, timework, timeworkend, idtranscript):
    conn = connect()
    cursor = conn.cursor()
    query = 'update bangdiem set sumScoreUser=%s, timework=%s, timeworkend=%s where idtranscript=%s'
    cursor.execute(query,(sumScoreUser, timework, timeworkend, idtranscript,))
    conn.commit()
    conn.close()

# user confirm transcript
def user_complete_transcript(opinion, idtranscript):
    conn = connect()
    cursor = conn.cursor()
    query = 'update bangdiem set opinion=%s where idtranscript=%s'
    cursor.execute(query,(opinion, idtranscript,))
    conn.commit()
    conn.close()
