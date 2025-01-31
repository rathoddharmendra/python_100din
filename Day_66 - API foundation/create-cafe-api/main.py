from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import os, random
from typing import Dict, Any
# from flask.json import jsonify


db_path = os.path.join(os.path.dirname(__file__), 'instance/cafes.db')
app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random', methods=['GET'])
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    # construct body
    return jsonify({
        'cafe': {
            'id': random_cafe.id,
            'name': random_cafe.name,
            'map_url': random_cafe.map_url,
            'img_url': random_cafe.img_url,
            'location': random_cafe.location,
            'amenities': {
                'seats': random_cafe.seats,
                'has_toilet': random_cafe.has_toilet,
                'has_wifi': random_cafe.has_wifi,
                'has_sockets': random_cafe.has_sockets,
                'can_take_calls': random_cafe.can_take_calls,
            },
            'coffee_price': random_cafe.coffee_price,
        }
    })
    # return jsonify(random_cafe)

    # cafe = Cafe.query.order_by(db.func.random()).first()
    # return jsonify(cafe)
@app.route('/all', methods=['GET'])
def get_all_cafes():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    response = { 'cafes': [] }
    for cafe in cafes:
        response['cafes'].append({cafe.id : {
            'name': cafe.name,
            'map_url': cafe.map_url,
            'img_url': cafe.img_url,
            'location': cafe.location,
            'seats': cafe.seats,
            'has_toilet': cafe.has_toilet,
            'has_wifi': cafe.has_wifi,
            'has_sockets': cafe.has_sockets,
            'can_take_calls': cafe.can_take_calls,
            'coffee_price': cafe.coffee_price,
        }})
    return jsonify(response)

@app.route('/search', methods=['GET'])
def search_cafe():
    location = request.args.get('loc').title()
    # location = request.form.get('loc')
    # if location is not None:
    #     location = location.title()
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()
    if cafes:
        response = { 'cafes': [] }
        for cafe in cafes:
            response['cafes'].append({
                'id': cafe.id,
                'name': cafe.name,
                'map_url': cafe.map_url,
                'img_url': cafe.img_url,
                'location': cafe.location,
                'seats': cafe.seats,
                'has_toilet': cafe.has_toilet,
                'has_wifi': cafe.has_wifi,
                'has_sockets': cafe.has_sockets,
                'can_take_calls': cafe.can_take_calls,
                'coffee_price': cafe.coffee_price,
            })
        return jsonify(response)
    return jsonify({'error': 'Cafe not found'})

# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name = request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        has_toilet = bool(request.form.get('has_toilet')),
        has_wifi = bool(request.form.get('has_wifi')),
        has_sockets = bool(request.form.get('has_sockets')),
        can_take_calls = bool(request.form.get('can_take_calls')),
        seats = request.form.get('seats'),
        coffee_price = request.form.get('coffee_price')
        )
    print(request.form.to_dict())
    try:
        db.session.add(new_cafe)
        db.session.commit()

        return jsonify({'success': 'Cafe added successfully'})
    except Exception as e:
        return jsonify({'error': f'Error adding cafe with error {e}'})

# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id: int):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = request.args.get('new_price')        
        db.session.commit()
        return jsonify({'success': 'Price updated successfully'})
    return jsonify({'error': 'Cafe not found'})

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    # app.run(debug=True) -- cannot run vscode debug mode with error "No module named main"
    app.run()