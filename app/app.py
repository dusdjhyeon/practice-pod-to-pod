from flask import Flask
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    user='root',
    password='password',
    host='db',
    port=3306,
    db='mydelivery',
    charset='utf8'
)

@app.route("/api/external/data/tracking", methods=['GET'])
def tracking():
    cursor = db.cursor()

    sql = f"SELECT RESULT FROM delivery"
    
    cursor.execute(sql)
    status = cursor.fetchall()
    print(status)
    cursor.close()

    return "All"

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
