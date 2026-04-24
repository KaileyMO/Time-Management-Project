from flask import Blueprint, render_template, request, redirect
import db
from db import sqlite3

notes_blueprint = Blueprint('notes_blueprint', __name__)

@notes_blueprint.route('/notes', methods=['GET', 'POST'])
def mainNotes():
    if request.method == 'POST':
        db.update_notes(request.form['writing'])
        return redirect(request.referrer)

    body = db.get_note()

    return render_template('notesPage/notes.html', body = body[0][1])