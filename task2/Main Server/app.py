from flask import Flask, request, render_template, redirect, url_for, session, make_response
from flask_cors import CORS  # Import Flask-CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

app.secret_key = 'your_secret_key'
app.config['SESSION_COOKIE_SECURE'] = True  # Use secure cookies (HTTPS only)
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevent client-side JavaScript from accessing cookies

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    if 'username' in session:
        return 'Logged in as ' + session['username']
    return redirect(url_for('login'))

@app.route('/change_username')
def change_username():
    print("Cookies: ",request.cookies)
    print("Session: ", session)
    if 'username' in session:
        new_username = request.args.get('new_username')
        if new_username:
            session['username'] = new_username
            response = make_response("Username changed successfully")
            response.headers['Access-Control-Allow-Origin'] = 'http://192.168.0.113:80'  # Allow requests from attack server origin
            return response
        else:
            return "Error: 'new_username' parameter is missing or invalid"
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

