# from MySQLdb import _mysql
import MySQLdb


def mysql_exec():
    # Connect db
    conn = MySQLdb.connect(
        user = 'root',
        passwd = '',
        host = 'localhost',
        db = 'mydb_test',
        charset = 'utf8'
    )
    cursor = conn.cursor()


    def sql_create_record(name, score, star):
        """ Execute SQL / create
        Fields
            | (id) | name | score | star |
        Expected result
            (1, 'math', 120.2, 10)
            (2, 'english', 88.1, 8)
            (3, 'physics', 90.5, 8)
            (4, 'name', score, star) -> new inserted
        """
        na, sc, st = name, score, star
        sql = f"insert into menu values( \
            null, '{na}', {sc}, {st} \
            )"
        cursor.execute(sql)


    def sql_update_record(score):
        """ Execute SQL / update
        docs omitted
        """
        sc = score
        sql = f"update menu set score = {sc} \
                where name = 'database'"
        cursor.execute(sql)


    def sql_delete_record(name):
        """ Execute SQL / read
        docs omitted
        """
        na = name
        sql = f" \
            delete from menu \
            where name = '{na}'"
        cursor.execute(sql)


    def sql_read_record():
        """ Execute SQL / read
        docs omitted
        """
        # sql = 'show databases'
        # sql = "select user()"
        sql = "select * from menu"
        cursor.execute(sql)

        rows = cursor.fetchall()

        for r in rows:
            print(r)


    try:
        # sql_create_record("security", 80.8, 5)

        # sql_update_record(150.9)

        sql_delete_record("security")

        # Save data
        conn.commit()

        # Read table
        sql_read_record()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        # Disconnect db
        cursor.close()
        conn.close()


if __name__ == "__main__":
    mysql_exec()
