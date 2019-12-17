from flask import Flask, render_template, request
import mysql.connector

app = Flask("Cats or Dogs")

insert_clause = "INSERT INTO catsordogs (name, color, pet) VALUES (%s, %s, %s)"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def insertData():
    form_data = (request.form['name'], request.form['color'], request.form['pet'])
    con = mysql.connector.connect(user='daniel', password='Helo#2009#Isa', host='127.0.0.1', database='catsordogs')
    cursor = con.cursor()
    cursor.execute(insert_clause, form_data)
    con.commit()
    cursor.close()
    con.close()
    return render_template('insert_response.html', name=form_data[0], color=form_data[1], pet=form_data[2])


if __name__ == '__main__':
    app.run(debug=True)
