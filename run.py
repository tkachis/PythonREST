from app import app
from db import db

db.init_app(app)

# Создание БД перед первым запросом на основании данных из него
@app.before_first_request
def create_tables():
    db.create_all()
