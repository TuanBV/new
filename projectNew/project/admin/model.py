from manager.model import connect
from transcript.model import get_standard

# get list user user
def get_user(pagination, limit, position, year, name, sort):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select * from user join position on user.idposition = position.idposition where activeStatus=1'
    data = {}
    if position != 'all':
        query += ' and user.idposition=%(position)s'
        data['position'] = position
    if year != '':
        query += ' and birthday like "%%(year)s%"'
        data['year'] = int(year)
    if name != '':
        query += ' and fullname like %(name)s'
        data['name'] = '%'+name+'%'
    query += ' order by fullname ASC' if sort == "fullname" else ' order by name ASC'
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
    conn.close()
    return {'data': db, 'count': len(count)}

# user join position where activeStatus=1
def get_all_user():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('select * from user join position on user.idposition = position.idposition where activeStatus=1 order by iduser limit 20')
    db = cursor.fetchall()
    for i in db:
        i['birthday'] = str(i['birthday'])
        i['timetoken'] = str(i['timetoken'])
    conn.close()
    return db
# get id transcript by iduser
def get_idtranscript_by_iduser(id):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select idtranscript from bangdiem where iduser=%s order by idtranscript DESC limit 1'
    cursor.execute(query, (id,))
    db = cursor.fetchall()
    conn.close()
    return db[0]['idtranscript']

#get user by usename
def get_user_by_username(username):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "select * from user join position on user.idposition = position.idposition where activeStatus=1 and username=%s"
        cursor.execute(query,(username,))
        db = cursor.fetchall()
    except Exception as e:
        print(e)
    for i in db:
        i['birthday'] = str(i['birthday'])
        i['timetoken'] = str(i['timetoken'])
    conn.close()
    return db

#get user by email
def get_user_by_email(email):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select * from user join position on user.idposition = position.idposition where activeStatus=1 and email=%s'
    cursor.execute(query, (email,))
    db = cursor.fetchall()
    for i in db:
        i['birthday'] = str(i['birthday'])
        i['timetoken'] = str(i['timetoken'])
    conn.close()
    return db

#get user by iduser
def get_user_by_iduser(iduser):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select * from user join position on user.idposition = position.idposition where activeStatus=1 and iduser=%s'
    cursor.execute(query, (iduser,))
    db = cursor.fetchall()
    for i in db:
        i['birthday'] = str(i['birthday'])
        i['timetoken'] = str(i['timetoken'])
    conn.close()
    return db
#validate username and email
def validate_username(username):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select username from user where username=%s'
    cursor.execute(query, (username,))
    db = cursor.fetchall()
    conn.close()
    return db

def validate_email(email):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select email from user where email=%s'
    cursor.execute(query, (email,))
    db = cursor.fetchall()
    conn.close()
    return db

# -------------Time rate------------
# get data timerate
def get_timerate():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("select * from kidanhgia")
    db = cursor.fetchall()
    for i in db:
        i['timeStart'] = str(i['timeStart'])
        i['timeEnd'] = str(i['timeEnd'])
    conn.close()
    return db
# get idtranscript by idtimerate
def get_idtranscript_by_timerate(idtimerate):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select idtranscript from bangdiem where idKiDanhGia=%s'
    cursor.execute(query, (idtimerate,))
    db = cursor.fetchall()
    conn.close()
    return db
#get time rate by idtime
def get_timerate_by_idtime(idtime):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select * from kidanhgia where idtime=%s'
    cursor.execute(query, (idtime,))
    db = cursor.fetchall()
    for i in db:
        i['timeStart'] = str(i['timeStart'])
        i['timeEnd'] = str(i['timeEnd'])
    conn.close()
    return db
# get idtime of record_end KiDanhGia
def get_record_end_of_timerate():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('select idtime from kidanhgia order by idtime DESC limit 1')
    recordid = cursor.fetchall()
    conn.close()
    return recordid
# get idKiDanhGia from table bangdiem
def get_idKiDanhGia_from_bangdiem():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('select idtranscript from bangdiem')
    db = cursor.fetchall()
    conn.close()
    return db
# get id user
def get_iduser_from_user():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("select iduser from user")
    db = cursor.fetchall()
    conn.close()
    return db
# get time rate by name time
def get_timerate_by_nameTime(nameTime):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select * from kidanhgia where nameTime=%s'
    cursor.execute(query, (nameTime,))
    db = cursor.fetchall()
    for i in db:
        i['timeStart'] = str(i['timeStart'])
        i['timeEnd'] = str(i['timeEnd'])
    conn.close()
    return db
# get iduser at table bangdiem
def get_iduser_new():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("select iduser from user order by iduser DESC limit 1")
    db = cursor.fetchall()
    conn.close()
    return db[0]['iduser']
# get id transcript
def get_idtranscript_from_bangdiem():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('select idtranscript from bangdiem')
    db = cursor.fetchall()
    conn.close()
    return db
# filter pagination time rate
def get_timerate_of_admin(pagination, limit,nameTime, sort):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select * from kidanhgia where 1=1'
    data = {}
    if nameTime != "":
        query += ' and nameTime like %(nameTime)s'
        data['nameTime'] = "%"+nameTime+"%"
    if sort == 'nameTimeAsc':
        query += ' order by nameTime ASC'
    if sort == 'nameTimeDesc':
        query += ' order by nameTime DESC'
    if sort == 'timeStartAsc':
        query += ' order by timeStart ASC'
    if sort == 'timeStartDesc':
        query += ' order by timeStart DESC'
    if sort == 'timeEndAsc':
        query += ' order by timeEnd ASC'
    if sort == 'sumManagerAsc':
        query += ' order by timeEnd DESC'
    cursor.execute(query, data)
    count = cursor.fetchall()
    pagination = int(limit)*int(pagination)
    query +=  ' limit %(pagination)s,%(limit)s'
    data['pagination'] = pagination
    data['limit'] = limit
    cursor.execute(query, data)
    db = cursor.fetchall()
    for i in db:
        i['timeStart'] = str(i['timeStart'])
        i['timeEnd'] = str(i['timeEnd'])
        # statistics time rate
        query = 'select count(*) as count1 from bangdiem join user on bangdiem.iduser=user.iduser where activeStatus=1 and idKiDanhGia=%s'
        cursor.execute(query,(i['idtime'],))
        count1 = cursor.fetchall()
        i['count1'] = count1[0]['count1']

        query = 'select count(*) as count2 from bangdiem where idKiDanhGia=%s and status=2'
        cursor.execute(query,(i['idtime'],))
        count2 = cursor.fetchall()
        i['count2'] = count2[0]['count2']

    conn.close()
    return {'data': db, 'count': len(count)}

# filter transcript detail time rate
def get_transcritp_detailtimerate(idtimerate, pagination, limit, status, sumScoreUser, sumResultManager, sort):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    data = {}
    query = 'select * from bangdiem join user on bangdiem.iduser=user.iduser where activeStatus=1 and idKiDanhGia=%(idtimerate)s'
    data['idtimerate'] = (idtimerate)
    if status != "all":
        query += ' and status=%(status)s'
        data['status'] = status
    if sumScoreUser != '':
        query += ' and sumScoreUser>%(sumScoreUser)s'
        data['sumScoreUser'] = sumScoreUser
    if sumResultManager != '':
        query += ' and sumScoreUser>%(sumResultManager)s'
        data['sumResultManager'] = sumResultManager
    if sort == 'sumUserAsc':
        query += ' order by sumScoreUser ASC'
    if sort == 'sumUserDesc':
        query += ' order by sumScoreUser DESC'
    if sort == 'sumManagerAsc':
        query += ' order by sumResultManager ASC'
    if sort == 'sumManagerDesc':
        query += ' order by sumResultManager DESC'
    if sort == 'username':
        query += ' order by username asc'
    if sort == 'status':
        query += ' order by status '
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
        i['count'] = len(count)
    conn.close()
    return db
# get manager by censor
def get_manager_by_censor(censor):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select username, email from user where username=%s'
    cursor.execute(query,(censor,))
    db = cursor.fetchall()
    conn.close()
    return db

# forgot password send email
def get_email():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("select email from user")
    db = cursor.fetchall()
    conn.close()
    return db
# update information user
def update_user(fullname, birthday, address, idposition, iduser):
    conn = connect()
    cursor = conn.cursor()
    query = 'update user set fullname=%s, birthday=%s, address=%s, idposition=%s where iduser=%s'
    cursor.execute(query,(fullname, birthday, address, idposition, iduser,))
    conn.commit()
    conn.close()

# delete user logic
def delete_user(iduser):
    conn = connect()
    cursor = conn.cursor()
    query = 'update user set activeStatus=0 where iduser=%s'
    cursor.execute(query,(iduser,))
    conn.commit()
    conn.close()

# update information timerate
def update_timerate(nameTime, timeStart, timeEnd, idtime):
    conn = connect()
    cursor = conn.cursor()
    query = "update kidanhgia set nameTime=%s, timeStart=%s, timeEnd=%s where idtime=%s"
    cursor.execute(query,(nameTime, timeStart, timeEnd, idtime,))
    conn.commit()
    conn.close()
    try:
        conn = connect()
        cursor = conn.cursor()
        query = "update bangdiem set nameTranscript=%s where idKiDanhGia=%s"
        cursor.execute(query,(nameTime, idtime,))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

# delete timerate
def delete_timerate(idtime):
    conn = connect()
    cursor = conn.cursor()
    try:
        # Delete at table tieuchi
        idtranscripts = get_idtranscript_by_timerate(idtime)
        conn = connect()
        cursor = conn.cursor()
        try: 
            for i in idtranscripts:   
                query = "delete from tieuchi where idBangDiem=%s"              
                cursor.execute(query,(i['idtranscript'],))
                conn.commit()
        except Exception as e:
            print(e)
        # Delete at table bangdiem
        cursor.execute("delete from bangdiem where idKiDanhGia=%s",(idtime,))
        conn.commit()                    
        # Delete at table kidanhgia
        cursor.execute("delete from kidanhgia where idtime=%s",(idtime,))
        conn.commit()
    except Exception as e:
        print(e)
    conn.commit()
    conn.close()

# create user new
def create_user_new(fullname, username, password, email, birthday, address, idposition):
    conn = connect()
    cursor = conn.cursor()
    query = "insert into user (fullname, username, password, email, birthday, address, idposition, activeStatus) values (%s, %s, %s, %s, %s, %s, %s, 1)"
    cursor.execute(query,(fullname, username, password, email, birthday, address, idposition,))
    conn.commit()
    conn.close()

# add time rate for user new
def add_timerate_for_user_new(nameTime, idtime, iduser_new):
    conn = connect() 
    cursor = conn.cursor()  
    #insert data to the table bangdiem
    query = "insert into bangdiem (nameTranscript, status, sumScoreUser, sumResultManager, idKiDanhGia,iduser) values (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query,(nameTime, 0, 0, 0, idtime,iduser_new,))
    conn.commit()
    conn.close()
    try:
        #insert data to the tieuchi
        idtranscript_new = get_idtranscript_by_iduser(iduser_new)
        conn = connect() 
        cursor = conn.cursor()  
        standards = get_standard()
        for standard in standards:
            query = "insert into tieuchi (nameStandard, scoreStandard, TuDanhGia, QLDanhGia, idBangDiem, idstandard) values (%s, %s, %s, %s, %s, %s)"                    
            cursor.execute(query,(standard['standard'], standard['score'], 0, 0, idtranscript_new, standard['id'],))
            conn.commit()
        conn.close()
    except Exception as e:
        print(e)

# create time rate new
def create_timerate_new(nameTimeNew, timeStartNew, timeEndNew):
    conn = connect() 
    cursor = conn.cursor()           
    query = "insert into kidanhgia (nameTime, timeStart, timeEnd) values (%s, %s, %s)"
    cursor.execute(query,(nameTimeNew, timeStartNew, timeEndNew,))
    conn.commit()
    conn.close()

# add transcript for user
def add_transcript_user(nameTime, idtranscript, iduser):
    conn = connect() 
    cursor = conn.cursor()           
    query = "insert into bangdiem (nameTranscript,status,sumScoreUser, sumResultManager, idKiDanhGia,iduser) values (%s, 0, 0, 0, %s, %s)"
    cursor.execute(query,(nameTime, idtranscript, iduser,))
    conn.commit()
    conn.close()
# insert data for table tieuchi
def insert_tieuchi_for_transcript(nameStandard, scoreStandard, idtranscript,idstandard):
    conn = connect() 
    cursor = conn.cursor()           
    query = "insert into tieuchi (nameStandard, scoreStandard, TuDanhGia, QLDanhGia, idBangDiem, idstandard) values (%s, %s, 0, 0, %s, %s)"
    cursor.execute(query,(nameStandard, scoreStandard, idtranscript,idstandard,))
    conn.commit()
    conn.close()
