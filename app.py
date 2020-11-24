import sqlite3
from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

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

@app.route('/htmlForm/')
def htmlForm():
	return render_template('htmlForm.html')

@app.route('/cssIntro/')
def cssIntro():
	return render_template('cssIntro.html')

@app.route('/cssSelectors/')
def cssSelectors():
	return render_template('cssSelectors.html')

@app.route('/cssBackgrounds/')
def cssBackgrounds():
	return render_template('cssBackgrounds.html')

@app.route('/cssMarginPadding/')
def cssMarginPadding():
	return render_template('cssMarginPadding.html')

@app.route('/cssText/')
def cssText():
	return render_template('cssText.html')

@app.route('/jsIntro/')
def jsIntro():
	return render_template('jsIntro.html')

@app.route('/jsVars/')
def jsVars():
	return render_template('jsVars.html')

@app.route('/jsArrays/')
def jsArrays():
	return render_template('jsArrays.html')

@app.route('/jsConditions/')
def jsConditions():
	return render_template('jsConditions.html')

@app.route('/jsLoops/')
def jsLoops():
	return render_template('jsLoops.html')

@app.route('/jsFunctions/')
def jsFunctions():
	return render_template('jsFunctions.html')

@app.route('/contacts/',methods=['POST'])
def test():
	mess=request.form['body']
	return redirect('mailto:mon4eto@abv.bg'+str(mess))

@app.route('/contacts/')
def contacts():
	return render_template('contacts.html')

@app.route('/discussion/')
def discussion():
	conn = get_db_connection()
	posts = conn.execute('SELECT * FROM posts ORDER BY id DESC').fetchall()
	conn.close()
	return render_template('discussion.html', posts=posts)

def get_db_connection():
	conn = sqlite3.connect('database.db')
	conn.row_factory = sqlite3.Row
	return conn

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']

        if not name:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (name, comment) VALUES (?, ?)',
                         (name, comment))
            conn.commit()
            conn.close()
            return redirect(url_for('discussion'))

    return render_template('create.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
