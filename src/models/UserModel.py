from flask_mysqldb import MySQL
mysql = MySQL()

def User(searcValue, row, rowperPage):
    sql = "select * from user WHERE 1 "
    arr_key = []
    if searcValue != '':
        cari = "%"+searcValue+"%"
        sql += " and nama LIKE %s OR email LIKE %s OR nohp LIKE %s "
        arr_key.extend([cari, cari, cari])
    
    sql += " ORDER BY nama asc limit %s, %s"
    arr_key.extend([row, rowperPage])

    cur = mysql.connection.cursor()
    cur.execute(sql, arr_key)
    data = cur.fetchall()
    cur.close()

    return data

def countUser(searcValue, row, rowperPage):
    sql = "select count(*) as allcount from user WHERE 1 "
    arr_key = []
    if searcValue != '':
        cari = "%"+searcValue+"%"
        sql += " and nama LIKE %s OR email LIKE %s OR nohp LIKE %s "
        arr_key.extend([cari, cari, cari])
    
    sql += " ORDER BY nama asc limit %s, %s"
    arr_key.extend([row, rowperPage])

    cur = mysql.connection.cursor()
    cur.execute(sql, arr_key)
    data = cur.fetchone()
    cur.close()

    return data


