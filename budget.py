from flask import Blueprint, render_template, request, redirect
import db
from db import sqlite3

budg_blueprint = Blueprint('budg_blueprint', __name__)

@budg_blueprint.route('/budget', methods=['GET', 'POST'])
def budg_logic():
    if request.method == 'POST':
        cat_arr = []
        try: # get the categories
            i = 0
            while True:
                cat_name = request.form[f'cat-{i}']
                cat_arr.append(cat_name)
                i = i + 1
        except KeyError:
            pass
        
        db.delete_categories()
        itera = 0
        for itera in range(0,len(cat_arr)):
            try:
                cat_price = request.form[f'price-{itera}']
                db.add_categories(cat_arr[itera], cat_price)
            except KeyError:
                pass

        return redirect(request.referrer)

    cats = db.get_categories()

    return render_template('budgetPages/budget.html', 
        category = cats, 
        cat_len = len(cats))
