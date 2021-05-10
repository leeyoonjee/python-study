from pymysql import connect, cursors
import datetime

# conn 객체는 쿼리 결과를 튜플로 가져온다.
conn = connect(
    host="localhost",
    user="korea",
    password="korea1234",
    db="koreadb",
    charset="utf8"
)

# conn 객체는 쿼리 결과를 딕셔너리로 가져온다.
cursor = conn.cursor(cursors.DictCursor)

def insert_one():
    data=["title1","content1"]
    insert_sql ="INSERT INTO board(title, content) VALUES(%s, %s)"
    cursor.execute(insert_sql,data)
    conn.commit()

#insert_one()
#주석처리

def select_one():
    data = 1
    select_sql="SELECT * FROM board WHERE id=%s"
    cursor.execute(select_sql,[data])
    row =cursor.fetchone()
    print(row)

#select_one()


def select_today():
    today=datetime.date.today() #오늘 날짜
    #yesterday= today - datetime.timedelta(1) #어제날짜
    select_sql ="SELECT * FROM board WHERE date(createdate) =%s"
    cursor.execute(select_sql,[today])
    rows =cursor.fetchall()
    print(rows)

#select_today()


def update_one():
    #data =["title2","content2",1]
    data ={"id":1,"title":"title2","content":"content2"}
    update_sql='''
        UPDATE board 
        SET title=%(title)s, content=%(content)s 
        WHERE id=%(id)s
    '''
    cursor.execute(update_sql,data)
    conn.commit()

#update_one()

#삭제하기
def delete_one():
    data=1
    delete_sql="DELETE FROM board WHERE id=%s"

    cursor.execute(delete_sql,data)
    conn.commit()

delete_one()
