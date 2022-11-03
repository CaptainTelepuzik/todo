from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


from classes.EngineConnect import EngineConnect

app = Flask(__name__)
app.config.from_object('Config.common')

db = SQLAlchemy(app)
Model = db.Model
migrate = Migrate(app, db)

engine = EngineConnect()

from routes import *


if __name__ == '__main__':
    app.run()
