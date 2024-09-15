from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def querry():
    if request.method == "POST":
        print("TEST")
        name = request.form.get("name")
        year = request.form.get("year")

        if name == None or year == None:
            return render_template('index.html')

        data = get_data(name, int(year))
        return render_template('data.html',
                name=name,
                year=year,
                rank=data[1],
                count=data[0],
                labels = data[3],
                data = data[2])

    print("NORMAL DISPLAY")
    return render_template('index.html')

def get_data(name, year):
    # connect to DB
    conn = connect_to_db()
    # Querry value
    data = get_frequancy(name.capitalize(), "Female", conn)

    if data == []:
        print("NO RESULTS")
        return "Name was not found"

    # format result
    index = (2021-year) * 2
    year_frequancy = data[index]
    year_count = data[index + 1]
    # return to user
    info = list(reversed(data[1::2]))
    return year_count, year_frequancy, info , list(range(1996, 2022))

def connect_to_db():
    conn = sqlite3.connect('names.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_frequancy(name, gender, conn):
    data = []
    female_data = []
    male_data = []

    for i in range(((2021-1996)* 2) + 3):
        female_data.append('[x]')
        male_data.append('[x]')

    if gender == "Male" or gender == "Both":
        male_data = conn.execute('SELECT * from boys where Name = ?', (name,)).fetchone()

    if gender == "Female" or gender == "Both":
        female_data = conn.execute('SELECT * from girls where Name = ?', (name,)).fetchone()

    if gender == "Male" and male_data == None:
        return []

    if gender == "Female" and female_data == None:
        return []

    if gender == "Both" and female_data == None and male_data == None:
        return []

    for male, female in zip(male_data, female_data):
        if male == '[x]':
            data.append(female)
        elif female == '[x]':
            data.append(male)
        elif male == name or female == name:
            data.append(name)
        else:
            data.append(int(male) + int(female))

    data = data[1:]
    data = [value.replace("[x]", "0") for value in data]

    return data