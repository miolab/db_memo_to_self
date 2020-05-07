# from MySQLdb import _mysql
import MySQLdb


def mysql_exec():
    # connect cb
    db = MySQLdb.connect(
        user = 'root',
        passwd = '',
        host = 'localhost',
        db = 'mydb_test',
        charset = 'utf8'
    )
    cursor = db.cursor()

    # execute db
    sql = "select * from menu"

    cursor.execute(sql)

    rows = cursor.fetchall()

    for r in rows:
        print(r)




    # disconnect db
    cursor.close
    db.close


if __name__ == "__main__":
    mysql_exec()