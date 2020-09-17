import MySQLdb

config = {'host':'127.0.0.1', 'user':'root', 'password':'1111', 'database':'pywin',
          'port':3306, 'charset':'utf8', 'use_unicode':True}

try:
    conn = MySQLdb.connect(**config)
    cur = conn.cursor()

    sql = "select code, prudouct_name, prudouct_count, prudouct_price from poduct"
    cur.execute(sql)

    for row in cur:
        print("%s %s %s %s" %row)

except Exception as err:
    print("에러: ",err )
    conn.rollback()
finally:
    conn.close()

