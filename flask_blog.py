from flask import Flask, render_template, url_for
from .forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5fef642e91f5d0ff2fac29768c2ae3ab'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

title = "Tomer Title"
@app.route("/home")
@app.route("/")
def hello():
    return render_template("home.html", posts=posts, title=title)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/registration')
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form, title="Register")


@app.route('/login.html')
def login():
    form = LoginForm()
    return render_template('login,html', form=form, title="login")

if __name__ == '__main__':
    app.run(debug=True)