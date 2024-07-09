# app.py
from flask import Flask, jsonify, request
from flask_mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
from models import db, Meal

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sua_senha_mysql'
app.config['MYSQL_DB'] = 'seu_banco_de_dados'
mysql = MySQL(app)
db.init_app(app)


@app.route('/meals', methods=['POST'])
def create_meal():
    data = request.json
    new_meal = Meal(
        name=data['name'],
        description=data.get('description'),
        datetime=data['datetime'],
        is_within_diet=data.get('is_within_diet', True)
    )
    db.session.add(new_meal)
    db.session.commit()
    return jsonify({'message': 'Meal created successfully', 'meal_id': new_meal.id}), 201


@app.route('/meals/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    meal_data = {
        'id': meal.id,
        'name': meal.name,
        'description': meal.description,
        'datetime': meal.datetime,
        'is_within_diet': meal.is_within_diet
    }
    return jsonify(meal_data), 200


@app.route('/meals', methods=['GET'])
def get_all_meals():
    meals = Meal.query.all()
    meals_data = []
    for meal in meals:
        meal_data = {
            'id': meal.id,
            'name': meal.name,
            'description': meal.description,
            'datetime': meal.datetime,
            'is_within_diet': meal.is_within_diet
        }
        meals_data.append(meal_data)
    return jsonify(meals_data), 200


@app.route('/meals/<int:meal_id>', methods=['PUT'])
def update_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    data = request.json
    meal.name = data['name']
    meal.description = data.get('description')
    meal.datetime = data['datetime']
    meal.is_within_diet = data.get('is_within_diet', True)
    db.session.commit()
    return jsonify({'message': 'Meal updated successfully'}), 200


@app.route('/meals/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    db.session.delete(meal)
    db.session.commit()
    return jsonify({'message': 'Meal deleted successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)
