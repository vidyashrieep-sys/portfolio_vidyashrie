from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db():
    return psycopg2.connect(DATABASE_URL)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():

    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name,email,message) VALUES (%s,%s,%s)",
        (name,email,message)
    )

    conn.commit()

    cur.close()
    conn.close()

    return "Message sent successfully!"

if __name__ == "__main__":
    app.run(debug=True)