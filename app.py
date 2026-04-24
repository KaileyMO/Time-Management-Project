from flask import Flask
from calLogic import cal_blueprint
from notes import notes_blueprint
from budget import budg_blueprint

app = Flask(__name__)
app.register_blueprint(cal_blueprint)
app.register_blueprint(notes_blueprint)
app.register_blueprint(budg_blueprint)

if __name__ == '__main__':
    app.run(debug=True)