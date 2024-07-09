# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Meal(db.Model):
    __tablename__ = 'meals'
    id = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(100), nullable=False)
    meal_description = db.Column(db.Text)
    meal_type = db.Column(db.String(50), nullable=False)
    meal_datetime = db.Column(db.DateTime, nullable=False)
    meal_in_diet = db.Column(db.Boolean, default=True)
