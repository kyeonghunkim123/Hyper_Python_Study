import pymysql

def get_dev_ps():
    filename = "C:/tilburg_club/tilburg.txt"
    with open(filename) as f:
        root_ps = f.read().strip()
    dev_ps = root_ps + 'dev'
    return dev_ps


def select_insert_mysql(request, db, sql, model):

    dev_ps = get_dev_ps()

    if sql.strip()[:6]=="select":
        conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db=db,
                               charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
        result = cur.execute(sql)
        rows = cur.fetchall()
        question_list = []
        for row in rows:
            question = model(**row)
            question_list.append(question)
        cur.close()
        return {'question_list' : question_list, 'result' : result}
    elif sql[:6]=="insert":
        conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db=db, charset='utf8')
        cur = conn.cursor()
        result = cur.execute(sql)
        cur.commit()
        cur.close()
        return {'result' : result}
    else : return None
