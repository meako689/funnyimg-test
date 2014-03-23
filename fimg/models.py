from fimg import app, db
from sqlalchemy.orm import validates

class FunnyImage(db.Model):
    """Really funny image"""
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    img_url = db.Column(db.String(255))
    vendor_id = db.Column(db.String(255))

    def __repr__(self):
           return '<Funnyimg %i>' % id
