from flask import Flask, request, jsonify
import psycopg2
import redis
import time

app = Flask(__name__)

# PostgreSQL Connection

while True:
    try:
        conn = psycopg2.connect(
            host="postgres",
            database="visitors",
            user="admin",
            password="admin123"
        )

        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS visitors(
            id SERIAL PRIMARY KEY,
            visitor_id VARCHAR(20),
            name VARCHAR(100),
            purpose VARCHAR(100)
        )
        """)

        conn.commit()
        break

    except:
        print("Waiting for PostgreSQL...")
        time.sleep(5)

# Redis Connection

while True:
    try:
        r = redis.Redis(
            host="redis",
            port=6379,
            decode_responses=True
        )

        r.ping()
        break

    except:
        print("Waiting for Redis...")
        time.sleep(5)

@app.route("/")
def home():

    visits = r.incr("homepage_visits")

    return jsonify({
        "message":"Visitor Management System",
        "homepage_visits":visits
    })

@app.route("/visitor", methods=["POST"])
def add_visitor():

    data = request.get_json()

    cur.execute(
        """
        INSERT INTO visitors(visitor_id,name,purpose)
        VALUES(%s,%s,%s)
        """,
        (
            data["visitor_id"],
            data["name"],
            data["purpose"]
        )
    )

    conn.commit()

    return jsonify({
        "message":"Visitor Added Successfully"
    })

@app.route("/visitor", methods=["GET"])
def get_visitors():

    cur.execute(
        """
        SELECT visitor_id,name,purpose
        FROM visitors
        """
    )

    rows = cur.fetchall()

    visitors=[]

    for row in rows:

        visitors.append({
            "visitor_id":row[0],
            "name":row[1],
            "purpose":row[2]
        })

    return jsonify(visitors)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
