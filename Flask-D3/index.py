from flask import Flask,json,request, render_template
from flaskext.mysql import MySQL


# Config
app = Flask(__name__)
# Config mysql datbase
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)




def my_jsonify(db_fetch):
    rowarray_list = []
    for row in db_fetch:
        t = (row.Open, row.High)
        rowarray_list.append(t)
    return json.dumps(rowarray_list)


@app.route('/')
def index():
     return render_template('index.html')


@app.route('/calander_data.json')
def hi():
    conn = mysql.connect()
    cursor =conn.cursor()

    cursor.execute("SELECT * from calendar")
    # data = cursor.fetchone()
    data = cursor.fetchall()

    empList = []
    for emp in data:
        empDict = {
        'Date':str(emp[0]),
        'Open':str(emp[1]),
        'High':str(emp[2]),
        'Low':str(emp[3]),
        'Close':str(emp[4]),
        'Volume':str(emp[5]),
        'Adj':str(emp[6])
        }
        empList.append(empDict)
    return json.dumps(empList)
