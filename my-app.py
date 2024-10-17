from flask import Flask, request, render_template, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']

    # Server-side validation: only allow alphabetic characters
    if not re.match("^[A-Za-z]+$", name):
        flash('Invalid name! Please enter letters only.')
        return redirect(url_for('index'))

    return f'Hello, {name}!'


if __name__ == '__main__':
    app.run(debug=True)

