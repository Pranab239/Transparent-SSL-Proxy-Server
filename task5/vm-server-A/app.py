#from flask import Flask

# create a server instance
#app = Flask(__name__)

#app.route('/')
#def index():
#    return "Hello World!!!"

# run the server
#app.run(host="0.0.0.0", port=5000, debug=True, ssl_context=('certA.pem', 'keyA.pem'))

from flask import Flask, render_template, request, jsonify
import json
import html  # Import html module for escaping HTML characters

app = Flask(__name__)

# File to store user messages
USER_DATA_FILE = 'user_data.json'

# Load existing user data from JSON file or initialize if file not found
try:
    with open(USER_DATA_FILE, 'r') as f:
        user_data = json.load(f)
except FileNotFoundError:
    user_data = []

@app.route('/')
def home():
    return render_template('index.html', messages=user_data)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        message = request.form['message']
        print(message)

        # Store the message in user_data
        user_data.append(message)

        # Save updated user data to JSON file
        with open(USER_DATA_FILE, 'w') as f:
            json.dump(user_data, f, indent=4)

        # Return a response that includes the message for potential XSS execution
#        return f"<script>alert('{html.escape(message)}');</script>"

    return home()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, ssl_context=('certA.pem', 'keyA.pem'))

