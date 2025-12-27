# server/app.py

from flask import Flask, request, jsonify
from flask_migrate import Migrate

from models import db, Plant

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

db.init_app(app)
migrate = Migrate(app, db)


with app.app_context():
    db.create_all()

    
    import seed




@app.route("/plants", methods=["GET"])
def plants_index():
    plants = Plant.query.all()
    return jsonify([plant.to_dict() for plant in plants]), 200


@app.route("/plants/<int:id>", methods=["GET"])
def plants_show(id):
    plant = Plant.query.get(id)
    return jsonify(plant.to_dict()), 200


@app.route("/plants", methods=["POST"])
def plants_create():
    data = request.get_json()

    plant = Plant(
        name=data["name"],
        image=data["image"],
        price=data["price"]
    )

    db.session.add(plant)
    db.session.commit()

    return jsonify(plant.to_dict()), 201


if __name__ == "__main__":
    app.run(port=5555, debug=True)
