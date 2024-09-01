from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('users.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
    cursor.execute("INSERT OR IGNORE INTO users VALUES ('admin', 'password123')")
    conn.commit()
    return conn, cursor

conn, cursor = init_db()

# Sigma rule toggle
sigma_rule_active = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if sigma_rule_active:
        # Secure query with parameterization
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        result = cursor.execute(query, (username, password)).fetchone()
    else:
        # Vulnerable query (DO NOT USE IN PRODUCTION!)
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        result = cursor.execute(query).fetchone()
    
    if result:
        return jsonify({"success": True, "message": "Logged in successfully!"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials."})

@app.route('/toggle_sigma', methods=['POST'])
def toggle_sigma():
    global sigma_rule_active
    sigma_rule_active = not sigma_rule_active
    status = "activated" if sigma_rule_active else "deactivated"
    return jsonify({"success": True, "message": f"Sigma rule {status}", "active": sigma_rule_active})

@app.route('/sigma_status', methods=['GET'])
def sigma_status():
    return jsonify({"active": sigma_rule_active})

if __name__ == '__main__':
    app.run(debug=True)
