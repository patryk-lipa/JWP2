from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<p>Witaj w mojej aplikacji Flask!</p>"

@app.route('/about')
def about():
   return 'Zaprogramowano przez <b>Patryk Lipa</b>'

@app.route('/contact')
def contact():
   return 'Email: kontakt@example.com.'

if __name__ == '__main__':
   app.run(debug=True)
