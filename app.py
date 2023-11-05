from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Set a secret key for session management

users = {
    'vanshika.s@trashcon.in': 'password',
    'john@example.com': 'secure123',
    'sarah@example.com': 'p@ssw0rd!',
    'bob@example.com': 'pass0rd123',
    'emily@example.com': '12345678',
    'saurabh@trashcon.in': 'trash@123',
    'admin@trashcon.in': 'admin-password'
}


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        if users.get(email) == password:
            session['logged_in'] = True  # Set the session variable
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html', error=error)

    return render_template('login.html', error=None)


@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):  # Check if the user is logged in
        return redirect(url_for('login'))

    return render_template('dashboard.html')


@app.route('/logout')
def logout():
    session['logged_in'] = False  # Set the session variable to False
    return redirect(url_for('login'))  # Redirect to the login page


@app.route('/customer.html')
def customer_page():
    return render_template('Customer.html')


@app.route('/input-analysis.html')
def input_page():
    return render_template('input-analysis.html')


@app.route('/material.html')
def raw_material():
    return render_template('Material.html')


@app.route('/input-stock.html')
def input_stock():
    return render_template('input-stock.html')


@app.route('/output.html')
def output_analysis():
    return render_template('output.html')


@app.route('/output-stock.html')
def output_stock():
    return render_template('output-stock.html')


@app.route('/machine-status.html')
def machine_status():
    return render_template('machine-status.html')


@app.route('/component-status.html')
def component_status():
    return render_template('component-status.html')


@app.route('/profile.html')
def profile_staus():
    return render_template('profile.html')


@app.route('/your-target-page.html')
def sale_pro():
    return render_template('your-target-page.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_files = request.files.getlist('myfile')

    for file in uploaded_files:
        file.save(file.filename)

    return "Files uploaded successfully!"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
