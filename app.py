from flask import Flask, render_template, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    # return 'Hello, World!'


@app.route('/contactus/')
def contactus():
    return render_template('contactus.html')


@app.route('/courses/')
def courses():
    return render_template('course.html')


@app.route('/aboutus/')
def aboutus():
    return render_template('aboutus.html')


@app.route('/login/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug = True)

    
