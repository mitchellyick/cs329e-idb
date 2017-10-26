from flask import Flask
from flask import render_template
app = Flask(__name__)
	
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')
@app.route('/about')
def about():
	return render_template('about.html')
@app.route('/author')
def author():
	return render_template('author.html')
@app.route('/title')
def title():
	return render_template('title.html')
@app.route('/publisher')
def publisher():
	return render_template('publisher.html')			

if __name__ == '__main__':
	app.run()
#host='127.0.0.1',port=8080,debug=True