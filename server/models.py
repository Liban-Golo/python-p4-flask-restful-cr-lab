from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)


class Plant(db.Model, SerializerMixin):
    __tablename__ = "plants"

    serialize_rules = ()

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)

    def __repr__(self):
        return f"<Plant {self.id}, {self.name}, {self.price}>"
