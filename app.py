
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import config
import psycopg2

app = Flask(__name__)


# View all data on Index Page

@app.route('/')
def Index():

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        data = cur.fetchall()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return render_template('index.html', data=data)


# Insert/Add employee route

@app.route('/insert', methods = ['POST'])
def insert():
    
    conn = None
    stud_id = None

    try:

        name = request.form['name']
        email = request.form['email']

        if name and email and request.method == 'POST':
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            sql = "INSERT INTO students(stud_name, stud_email) VALUES  (%s, %s) RETURNING stud_id";
            data = (name, email)
            cur.execute(sql, data)
            stud_id = cur.fetchone()[0]
            conn.commit()
            cur.close()

            return redirect(url_for('Index'))

    except (Exception, psycopg2.DatabaseError) as error:

        print(error)
    finally:

        if conn is not None:
            conn.close()

    return stud_id

        

        

    

























if __name__ == '__main__':
    app.run(debug=True)