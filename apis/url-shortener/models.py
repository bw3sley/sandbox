from database import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    original_url = db.Column(db.String(2048), nullable=False)
    short_url = db.Column(db.String(16), unique=True, nullable=False)

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    expires_at = db.Column(db.DateTime, nullable=False)