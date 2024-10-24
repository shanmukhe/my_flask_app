from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    conn.commit()
    conn.close()

init_db()

# Home page to display form
@app.route('/')
def index():
    return render_template('index.html')

# Add data to database
@app.route('/add', methods=['POST'])
def add_data():
    name = request.form['name']
    age = request.form['age']

    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO data (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

    return redirect('/show')

# Show data from database
@app.route('/show')
def show_data():
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    rows = c.fetchall()
    conn.close()
    return render_template('show.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
