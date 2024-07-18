from os import path
from flask import Flask, render_template, redirect, url_for, request, flash
from datetime import date

nee = Flask(__name__)
#app.config['SECRET_KEY'] = 'IMustNotFearFearIsTheMindKiller

@nee.route('/')
def indexPage():

    return render_template('index.html', title = 'North East Event')

@nee.route('/register.html')
def register():
    show_link = date.today() >= date(2024, 10, 1)
    return render_template('register.html', title = 'Registration Information', show_link=show_link)

@nee.route('/schedule.html')
def schedule():
    return render_template('schedule.html', title = 'Meeting Schedules')

@nee.route('/covid.html')
def covid():
    return render_template('covid.html', title = 'COVID-19 Policy')

@nee.route('/hotels.html')
def hotels():
    return render_template('hotels.html', title = 'Hotel Site Information')

@nee.route('/general.html')
def generalinfo():
    return render_template('general.html', title = 'General Event Information')

if __name__ == '__main__':
    nee.run(debug=True)
