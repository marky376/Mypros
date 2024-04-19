from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/about')
def about():
    return '<h1>About Page!</h1>'

@app.route('/whoami')
def whoami():
    return "<h1> My Name is Mark Munyao Mutua Son of Gregory Mutua Munyao and Ceciia Mueni Mutisya. Brother to Chelsea Ndunge Mutua and Annastacia Kavindu Mutua.</h1>"

if __name__ == '__main__':
    app.run(debug=True)

