from flaskblog.models import User, Post
from flask import flash, redirect, render_template, url_for
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm


posts = [
    {
        'author': 'Afsar Khan',
        'title': 'Baghi roohe',
        'content': 'First post content',
        'date_posted': 'April 20, 2024'
    },
    {
        'author': 'Jibran Khalil Jibran',
        'title': 'The broken wings',
        'content': 'Second post content',
        'date_posted': 'December 23, 2024'
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ka484564@gmail.com' and form.password.data == 'afsar1':
            flash('You have been logged In!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessfull. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
