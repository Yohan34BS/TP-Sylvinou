from flask import Flask, jsonify
import pymysql
import os

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def home():
    return "<h1>Bienvenue Sylvain !</h1><p></p>"

@app.route('/data')
def get_data():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT DATABASE() as db, USER() as user")
            result = cursor.fetchone()
        conn.close()
        return jsonify({
            "status": "success",
            "database": result['db'],
            "connected_as": result['user']
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)