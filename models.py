import psycopg2
from config import config

def create_table():
    
    sql = '''   CREATE TABLE students (
                stud_id SERIAL PRIMARY KEY,
                stud_name VARCHAR(255) NOT NULL,
                stud_email VARCHAR(255) NOT NULL
        )'''

    conn = None
    
    try:
        
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.commit()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_table()