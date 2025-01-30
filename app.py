from flask import Flask, render_template, redirect, url_for, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.config['SECRET_KEY'] = '@Bunny455'

# Database connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            port=3306,
            password='kellen',
            database='animal_shelter_management_system'
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Users WHERE username = %s", (username,))
        user = cursor.fetchone()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Login successful', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
        
        cursor.close()
        conn.close()
    
    return render_template("login.html")

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

# Protecting routes with login required
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper

@app.route('/')
@login_required
def index():
    return render_template("index.html")

# Example of protecting an existing route with login
@app.route('/animals')
@login_required
def animals():
    conn = get_db_connection()
    if conn is None:
        print("Not Connected to MySQL DB")
        return "Database connection error"

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM animal")
    animals = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("animals.html", animals=animals)

# (Other routes here, with @login_required decorator applied where needed)

if __name__ == "__main__":
    app.run(debug=True)
