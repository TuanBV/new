from manager.model import connect
# ------------------- not injection 
#transcript user
def get_transcript(username,pagination, limit,nameTime, status, sumScoreUser,sumResultManager, sort):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select * from bangdiem join user on bangdiem.iduser=user.iduser where username="%s"'%username
    if nameTime != "all":
        query += ' and nameTranscript="{}"'.format(nameTime)
    if status != "all":
        query += ' and status={}'.format(status)
    if sumScoreUser != '':
        query += ' and sumScoreUser>{}'.format(sumScoreUser)
    if sumResultManager != '':
        query += ' and sumScoreUser>{}'.format(sumResultManager)
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
    cursor.execute(query)
    count = cursor.fetchall()
    pagination = int(limit)*int(pagination)
    query +=  ' limit {},{}'.format(pagination, limit)
    cursor.execute(query)
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
        i['birthday'] = str(i['birthday'])
        i['timetoken'] = str(i['timetoken'])
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
def get_user_by_idrranscipt(idtranscript):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select * from bangdiem join user on bangdiem.iduser=user.iduser where idtranscript=%s'
    cursor.execute(query,(idtranscript,))
    db = cursor.fetchall()
    for i in db:
        i['birthday'] = str(i['birthday'])
        i['timetoken'] = str(i['timetoken'])
        i['timework'] = str(i['timework'])
        i['timeworkend'] = str(i['timeworkend'])
    conn.close()
    return db
# update standard
def update_tieuchi(TuDanhGia, id, idstandard):
    conn = connect()
    cursor = conn.cursor()
    query = "update tieuchi set TuDanhGia=%s where idBangDiem=%s and idstandard=%s"
    cursor.execute(query,(TuDanhGia, id, idstandard,))
    conn.commit()
    conn.close()
# update censor and status of transcript
def update_transcript(censor, status, id):
    conn = connect()
    cursor = conn.cursor()
    if censor == "":
        query = 'update bangdiem set status=%s where idtranscript=%s'
        cursor.execute(query,(status, id,))
    else:
        query = 'update bangdiem set censor=%s ,status=%s where idtranscript=%s'
        cursor.execute(query,(censor, status, id,))
    conn.commit()
    conn.close()
# user confirm transcript
def user_confirm_transcript(sumUser, timework, timeworkend, id):
    conn = connect()
    cursor = conn.cursor()
    query = 'update bangdiem set sumScoreUser=%s, timework=%s, timeworkend=%s where idtranscript=%s'
    cursor.execute(query,(sumUser, timework, timeworkend, id,))
    conn.commit()
    conn.close()
# user confirm transcript
def user_complete_transcript(opinion, id):
    conn = connect()
    cursor = conn.cursor()
    query = 'update bangdiem set opinionMember=%s where idtranscript=%s'
    cursor.execute(query,(opinion, id,))
    conn.commit()
    conn.close()
