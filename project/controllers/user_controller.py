from project import app
from project.controllers.forms import SignupForm, LoginForm
from project.models.User import User
from flask import Flask, render_template, redirect, url_for, request, flash


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = User(form.username.data, form.password.data, None)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        return redirect('home')
    return render_template('login.html', form=form)

'''
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        user.update_user(request.form['firstname'], request.form['lastname'], request.form['income'])
        return redirect(url_for('home'))
    return render_template('settings.html')
'''
