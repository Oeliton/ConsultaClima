from Data import connectdb

cur = connectdb.getCursor()
con = connectdb.getConnection()

def save(name):
    
    sql = 'select 1 from city where name = %s'
    cur.execute(sql, [name])
    
    idCity = cur.fetchone()
    
    #Gravar cidade caso nao exista no banco
    if type(idCity) != tuple:
        sql = 'insert into city (name) values (%s)'
        cur.execute(sql, [name])
        con.commit()
    
    cur.execute('select id from city order by id desc')
    idCity = cur.fetchone()
    
    return idCity

def select():
    cur.execute('select * from city')
    recset = cur.fetchall()
    for rec in recset:
        print(rec)