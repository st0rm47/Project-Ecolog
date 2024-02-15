from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '#412saqwerT'  # Replace with a secret key for session encryption

# login page route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')


# dashboard route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    devices = ['Ecolog1', 'Ecolog2', 'Ecolog3']
    if 'logged_in' not in session or not session['logged_in']:
        return redirect('/')

    if request.method == 'POST' and 'button' in request.form:
        return redirect('/live')
    
    return render_template('dashboard.html', deviceharu= devices)


# live route
@app.route('/live', methods=['GET', 'POST'])
def live():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect('/')
    
    return render_template('live.html')


# logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')


@app.route('/trigger')
def trigger():
    return render_template('trigger-page.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
