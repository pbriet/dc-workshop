from flask import Flask
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
mysql = MySQL(app)

for env_variable in ('MYSQL_USER', 'MYSQL_PASSWORD', 'MYSQL_HOST', 'MYSQL_DB'):
    app.config[env_variable] = os.getenv(env_variable)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT version()")
    row = cur.fetchone()
    print(row)
    return "(Python) version is %s" % row[0]

def create_table(cur):

    cur.execute("""
        CREATE TABLE IF NOT EXISTS entries (
        entry_id INT AUTO_INCREMENT PRIMARY KEY,
        value TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )  ENGINE=INNODB;
    """)



@app.route('/add-entry/<value>')
def add_entry(value):
    cur = mysql.connection.cursor()
    create_table(cur)
    cur.execute("INSERT INTO entries (value) VALUES('%s')" % value)
    mysql.connection.commit()
    return "Added entry : %s" % value

@app.route('/entries')
def entries():
    cur = mysql.connection.cursor()
    create_table(cur)

    cur.execute("SELECT created_at, value FROM entries ORDER BY created_at")

    rows = cur.fetchall()

    res = []
    for row in rows:
        res.append("%s: %s" % (row[0], row[1]))

    return "\n".join(res)


if __name__ == '__main__':
    app.run()