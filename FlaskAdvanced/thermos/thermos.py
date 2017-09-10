from flask import Flask, render_template, url_for
app = Flask(__name__)

class user:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def initials(self):
        return '%s %s', self.first_name, self.last_name


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='This is the title',
    text=['This is the text1', 'This is the text2', 'This is the text3'],
    user_instance= user('Cristian', 'Turcios'))

@app.route('/add')
def add():
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.debug = True
    app.run()
