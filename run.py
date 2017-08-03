from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/b20840')
def hello_world():
	return render_template('b20840.html')


@app.route('/B18355')
def B18355():
	return render_template('B18355.html')


if __name__ == '__main__':
    app.run(debug=True)