from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/b20840')
def hello_world():
	return render_template('b20840.html')
    

if __name__ == '__main__':
    app.run(debug=True)