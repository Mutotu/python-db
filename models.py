from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Dino(db.Model):
    __tablename__ = 'dinos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    type = db.Column(db.String, nullable=False,)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    
    def to_json(self):
        return {
            "name": self.name,
            "type": self.type,
        }
class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    dinos_abc = db.relationship('Dino')