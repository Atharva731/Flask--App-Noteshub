from flask import Flask, render_template, request, redirect
import MySQLdb

app = Flask(__name__)

# Database Connection
import time

while True:
    try:
        db = MySQLdb.connect(
            host="mysql",
            user="noteshub",
            passwd="password123",
            db="noteshub"
        )
        print("Database connected")
        break

    except MySQLdb.OperationalError:
        print("Waiting for database...")
        time.sleep(5)
cursor = db.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
)
""")
db.commit()


@app.route("/")
def home():
    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    notes = cursor.fetchall()
    return render_template("index.html", notes=notes)


@app.route("/add", methods=["POST"])
def add_note():
    title = request.form["title"]
    content = request.form["content"]

    cursor.execute(
        "INSERT INTO notes (title, content) VALUES (%s, %s)",
        (title, content)
    )

    db.commit()

    return redirect("/")

@app.route("/delete/<int:id>")
def delete_note(id):

    cursor.execute("DELETE FROM notes WHERE id = %s", (id,))
    db.commit()

    return redirect("/")


@app.route("/edit/<int:id>")
def edit_note(id):

    cursor.execute("SELECT * FROM notes WHERE id=%s", (id,))
    note = cursor.fetchone()

    return render_template("edit.html", note=note)

@app.route("/update/<int:id>", methods=["POST"])
def update_note(id):

    title = request.form["title"]
    content = request.form["content"]

    cursor.execute(
        """
        UPDATE notes
        SET title=%s,
            content=%s
        WHERE id=%s
        """,
        (title, content, id)
    )

    db.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
