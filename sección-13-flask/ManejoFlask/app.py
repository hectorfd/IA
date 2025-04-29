from flask import Flask, render_template
app = Flask(__name__)
titulo_app = 'Zona Fit HFD'
@app.route('/')
@app.route('/index.html')
def hola_mundo():
    return render_template('index.html', titulo = titulo_app)

if __name__ == '__main__':
    app.run(debug=True)