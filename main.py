from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def querry():
    # connect to DB

    # Querry value

    # format result

    # return to user

    return render_template('index.html')