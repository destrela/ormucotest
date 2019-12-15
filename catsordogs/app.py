from flask import Flask, render_template, request

app = Flask("Cats or Dogs")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def insertData():
    userName = request.form['userName']
    favoriteColor = request.form['favoriteColor']
    catsOrDogs = request.form['catsOrDogs']
    return render_template('insert_response.html', userName=userName, favoriteColor=favoriteColor, catsOrDogs=catsOrDogs)


if __name__ == '__main__':
    app.run(debug=True)