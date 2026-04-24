from flask import Blueprint, render_template, redirect, request, url_for
import db
from db import sqlite3
import calendar
from datetime import datetime

cal_blueprint = Blueprint('cal_blueprint', __name__)

DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
HOURS = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # the hours in half a day

@cal_blueprint.route('/')
def calYear():
    full_list = db.full_list()

    # datetime.now().year - gets current year/month/day
    year = datetime.now().year
    curr_month = datetime.now().month
    day = datetime.now().day

    calendar.setfirstweekday(6)
    months = [] # this will hold the name of and full set of weeks per month
    for i in range(1, 13):
        months.append({"name":calendar.month_name[i], "weeks":calendar.monthcalendar(year, i)})
    
    return render_template('calPages/monthView.html', 
        months = months, 
        year = year, 
        DAYS = DAYS,
        curr_day = day,
        curr_month = curr_month,
        all_events = full_list)

@cal_blueprint.route('/<int:month>/<int:day>/<int:year>', methods=['GET', 'POST'])
def calDay(month, day, year):
    display = db.display_item(month, day, year)

    if request.method == 'POST':
        if request.form.get('action') == "delete":
            db.remove_event(request.form['event_id'])
            return redirect(request.referrer)
        else:
            name = request.form['title']
            time = request.form['time']
            twilight = request.form['twilight']
            date = f"{month}-{day}-{year}"

            db.add_event(name, time, twilight, date) # adds submitted information as event object
            return redirect(request.referrer) # refreshes with new event

    return render_template('calPages/dayView.html', 
        month = month, 
        day = day, 
        year = year,
        HOURS = HOURS,
        display = display)
