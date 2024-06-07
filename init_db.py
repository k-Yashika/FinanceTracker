from app import app, db
from app.models import User, Transaction

with app.app_context():
    db.create_all()
    print("Database Initialized")