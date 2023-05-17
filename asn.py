from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home page'

@app.route('/loginpage')
def login():
    return 'login page'

@app.route('/logoutpage')
def logout():
    return 'logout page'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if requests.method ='POST'
    user = requests.from['uername']
    session['user'] = user
    return redirect(url_for('user'))
else:
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'you are loged out'
