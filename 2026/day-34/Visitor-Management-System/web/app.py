from flask import Flask, jsonify, render_template, request
import psycopg2
import redis
import time

app = Flask(__name__)

# --- PostgreSQL Connection ---
db = None
for _ in range(30):
    try:
        db = psycopg2.connect(
            host="postgres",
            database="visitors",
            user="admin",
            password="admin123"
        )
        print("Connected to PostgreSQL")
        break
    except Exception as e:
        print("Waiting for PostgreSQL...", e)
        time.sleep(2)

if db is None:
    raise Exception("Could not connect to PostgreSQL")

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS visitors (
    id SERIAL PRIMARY KEY,
    visitor_id VARCHAR(50),
    name VARCHAR(100),
    purpose VARCHAR(200)
)
""")
db.commit()

# --- Redis Connection ---
r = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

# --- Routes ---
@app.route("/")
def home():
    return render_template("index.html")   # UI load karega

@app.route("/api/visits")
def visits():
    count = r.incr("homepage_visits")
    return jsonify({"visits": count})

@app.route("/visitor", methods=["POST"])
def add_visitor():
    data = request.get_json()
    cursor.execute(
        "INSERT INTO visitors (visitor_id, name, purpose) VALUES (%s, %s, %s)",
        (data["visitor_id"], data["name"], data["purpose"])
    )
    db.commit()
    return jsonify({"message": "Visitor Added Successfully"})

@app.route("/visitor", methods=["GET"])
def get_visitors():
    cursor.execute("SELECT visitor_id, name, purpose FROM visitors")
    rows = cursor.fetchall()
    visitors = [
        {"visitor_id": r[0], "name": r[1], "purpose": r[2]} for r in rows
    ]
    return jsonify(visitors)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

