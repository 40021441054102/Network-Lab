# openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
from flask import Flask, request, render_template

app = Flask(__name__)

# - Route to Display the Login Form
@app.route('/')
def index():
    return render_template('index.html')

# - Method to Login the User
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username'] 
    password = request.form['password']
    return render_template("home.html")

if __name__ == '__main__':
    # - Run the Server on localhost, Port 5000
    app.run(host = '0.0.0.0', port = 5000, debug = True, ssl_context = ('cert.pem', 'key.pem'))
