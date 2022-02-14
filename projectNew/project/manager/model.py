from unicodedata import name
from mysql.connector import MySQLConnection, Error

def connect():
    db_config = {
        'host': 'localhost',
        'port':'3306',
        'database': 'employee',
        'user': 'root',
        'password': '12345'
    }
    conn = None
    try:
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            return conn
    except Error as e:
        print(e)
    return conn
#get data full by idtranscript
def get_full_by_idtranscript(idtranscript):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select * from bangdiem join kidanhgia on bangdiem.idKiDanhGia = kidanhgia.idTime where idtranscript=%s'
    cursor.execute(query,(idtranscript,))
    infor = cursor.fetchall()
    for i in infor:
        i['timeStart'] = str(i['timeStart'])
        i['timeEnd'] = str(i['timeEnd'])

    query = 'select * from target'
    cursor.execute(query)
    target = cursor.fetchall()

    for i in target:
        query = 'select sumScoreUser,sumResultManager,nameStandard,scoreStandard,TuDanhGia,QLDanhGia,NhanXet, idtranscript,idtarget from (bangdiem join tieuchi on bangdiem.idtranscript = tieuchi.idBangDiem) join standard on tieuchi.idstandard=standard.id where idtranscript=%s and idtarget=%s'%(idtranscript, i['idtarget'])
        cursor.execute(query)
        standard = cursor.fetchall()
        i['standard'] = standard
        query = 'select count(*) as count from standard where idtarget=%s'
        cursor.execute(query,((i['idtarget']),))
        i['count'] = cursor.fetchall()[0]['count'] + 1
    conn.close()
    return {'infor': infor,'target': target}

# filter transcript manager
def get_transcript_of_manager(pagination, limit, nameTime, status, sumScoreUser, sumResultManager, sort):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select * from bangdiem join user on bangdiem.iduser=user.iduser where activeStatus=1'
    data ={}
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
    if sort == 'nameTranscript':
        query += ' order by nameTranscript'
    elif sort == 'sumUserAsc':
        query += ' order by sumScoreUser ASC'
    elif sort == 'sumUserDesc':
        query += ' order by sumScoreUser DESC'
    elif sort == 'sumManagerAsc':
        query += ' order by sumResultManager ASC'
    elif sort == 'sumManagerAsc':
        query += ' order by sumResultManager DESC'
    elif sort == 'username':
        query += ' order by username ASC'
    elif sort == 'status':
        query += ' order by status '
    cursor.execute(query, data)
    count = cursor.fetchall()
    count = 0 if count == [] else len(count)
    pagination = int(limit)*int(pagination)
    query +=  ' limit %(pagination)s, %(limit)s'
    data['pagination'] = pagination
    data['limit'] = limit
    cursor.execute(query, data)
    db = cursor.fetchall()
    for i in db:
        i['birthday'] = str(i['birthday'])
        i['timetoken'] = str(i['timetoken'])
        i['timework'] = str(i['timework'])
        i['timeworkend'] = str(i['timeworkend'])
        i['count'] = count
    conn.close()
    return {'data': db, 'count':count}

# update transcript of manager
def update_trancript_of_manager(status, sumResultManager, ghichu, id):
    conn = connect()
    cursor = conn.cursor()
    query = 'update bangdiem set status=%s, sumResultManager=%s, ghichu=$s where idtranscript=%s'
    cursor.execute(query,(status, sumResultManager, ghichu, id,))
    conn.commit()
    conn.close()
    
# update standard of manager
def update_standard_od_manager(QLDanhGia, NhanXet, id, idstandard):
    conn = connect()
    cursor = conn.cursor()
    if NhanXet == "":
        query = "update tieuchi set QLDanhGia=%s where idBangDiem=%s and idstandard=%s".format(QLDanhGia, id, idstandard)
        cursor.execute(query,(QLDanhGia, id, idstandard))
    else: 
        query = "update tieuchi set QLDanhGia=%s,NhanXet=%s where idBangDiem=%s and idstandard=%s"
        cursor.execute(query,(QLDanhGia, NhanXet, id, idstandard,))
    conn.commit()
    conn.close()