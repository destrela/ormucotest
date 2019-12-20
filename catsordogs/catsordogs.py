from flask import Flask, render_template, request
import mysql.connector
import os

app_path = os.path.dirname(os.path.abspath(__file__))
template_path=os.path.join(app_path, 'templates')

app = Flask("Cats or Dogs", template_folder=template_path)

insert_clause = "INSERT INTO catsordogs (name, color, pet) VALUES (%s, %s, %s)"
config = {'user': os.getenv('COD_USER'), 'password': os.getenv('COD_PASSWORD'), 'host': os.getenv('COD_HOST'), 'database': os.getenv('COD_DATABASE')}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def insertData():
    form_data = (request.form['name'], request.form['color'], request.form['pet'])
    con = mysql.connector.connect(user=config['user'], password=config['password'], host=config['host'], database=config['database'])
    cursor = con.cursor()
    cursor.execute(insert_clause, form_data)
    con.commit()
    cursor.close()
    con.close()
    return render_template('insert_response.html', name=form_data[0], color=form_data[1], pet=form_data[2])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
