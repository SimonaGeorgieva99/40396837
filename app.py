from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/home/')
def home():
	return render_template('homePage.html')

@app.route('/htmlIntro/')
def htmlIntro():
	return render_template('htmlIntro.html')

@app.route('/htmlAttributes/')
def htmlAttributes():
	return render_template('htmlAttributes.html')

@app.route('/htmlLists/')
def htmlLists():
	return render_template('htmlLists.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
