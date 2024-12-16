from sqlalchemy import ForeignKey
from .. import db

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, ForeignKey('planet.id'), nullable=True)
    favorite_type = db.Column(db.String(50), nullable=False)  # 'planet', 'character' o 'vehicles' 
    date_added = db.Column(db.Date, nullable=False)

    user = db.relationship('User', backref='favorites')
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "favorite_type": self.favorite_type,
            "date_added": self.date_added.isoformat(),
        }
