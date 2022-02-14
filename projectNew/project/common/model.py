from manager.model import connect
# check OTP
def check_token(email, idtoken):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    query = 'select * from user join position on user.idposition = position.idposition where activeStatus=1 and email=%s and idtoken=%s'
    cursor.execute(query,(email, idtoken,))
    db = cursor.fetchall()
    for i in db:
        i['birthday'] = str(i['birthday'])
        i['timetoken'] = str(i['timetoken'])
    conn.close()
    return db

# create token
def create_token(tokenOTP, timetoken, email):
    conn = connect()
    cursor = conn.cursor()
    query = "update user set idtoken=%s , timetoken=%s where email=%s"
    cursor.execute(query,(tokenOTP, timetoken, email,))
    conn.commit()
    conn.close()
# update password new
def update_password_new(password, email):
    conn = connect()
    cursor = conn.cursor()
    query = "update user set password=%s where email=%s"
    cursor.execute(query,(password, email,))
    conn.commit()
    conn.close()

