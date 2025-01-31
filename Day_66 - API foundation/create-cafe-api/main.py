from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import os, random
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

@app.route('/random')
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

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
