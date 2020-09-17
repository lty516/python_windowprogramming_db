import sqlite3

def Process(dbname):
    try:
        conn = sqlite3.connect(dbname) # DB생성
        cur = conn.cursor()

        sql = "drop table if exists emp"
        cur.execute(sql)

        sql = "create table if not exists emp(id integer primary key, name text)"
        cur.execute(sql)

        # 데이터 입력
        cur.execute("insert into emp values(1, '홍길동')")
        cur.execute("insert into emp values(?, ?)", (2, "임꺽정"))

        tddata = (3, "김 수한무")
        cur.execute("insert into emp values(?, ?)", tddata)

        tlist =((4,"유비"), (5, "관우"), (6, "장비"))
        cur.executemany("insert into emp values(?, ?)", tlist)   #execute : 트렌잭션 한번 / executemany : 동시에 여러번의 실행 시 사용

        ldata =[7, "강감찬"]
        cur.execute("insert into emp values(?, ?)", ldata)

        cur.execute("insert into emp values(:sabun, :irum)", {"sabun" : "8", "irum" : "관창"})
        cur.execute("insert into emp values(:sabun, :irum)", {"irum":"김유신", "sabun":"9"})

        conn.commit() # DML명령어 실행 후 commit 필수

        #데이터 조회
        cur.execute("select * from emp")
        for row in cur.fetchmany(3):
            print(row)

        print("---------------------------------------------")

        cur.execute("select count(*) from emp")
        print(cur.fetchone())

    except sqlite3.Error as err:
        print("에러 : ", err)
        conn.rollback()
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    Process("nice.db")