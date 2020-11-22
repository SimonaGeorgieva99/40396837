from flask import Flask, render_template, url_for, request, redirect
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

@app.route('/htmlLayout/')
def htmlLayout():
	return render_template('htmlLayout.html')

@app.route('/htmlTables/')
def htmlTables():
	return render_template('htmlTables.html')

@app.route('/htmlForms/')
def htmlForms():
	return render_template('htmlForms.html')

@app.route('/contacts/')
def contacts():
	return render_template('contacts.html')

@app.route('/contacts/',methods=['POST'])
def test():
	mess=request.form['body']
	return redirect('mailto:mon4eto@abv.bg'+str(mess))

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
