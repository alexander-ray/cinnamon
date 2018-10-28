from project import app
from flask import Flask, render_template, redirect, url_for, request


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

'''
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        user.update_user(request.form['firstname'], request.form['lastname'], request.form['income'])
        return redirect(url_for('home'))
    return render_template('settings.html')
'''
