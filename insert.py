import psycopg2
from config import config


def insert_student():
    sql = '''   INSERT INTO students(stud_name, stud_email)
                VALUES ('studenttest', 'studtest@test.com') RETURNING stud_id;
        '''   
    conn = None
    stud_id = None
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        # get the generated id back
        stud_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return stud_id


if __name__ == '__main__':
    insert_student()