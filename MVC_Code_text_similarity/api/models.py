from api import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text
from datetime import datetime


class Text_Similarity_Score(db.Model):

    id = db.Column(db.BigInteger, primary_key=True)
    text_score = db.Column(db.String(120), unique=True)
    create_at = db.Column(
        db.TIMESTAMP,
        default=datetime.utcnow,
        nullable=False
    )

    def __init__(self, text_score):
        self.text_score = text_score
        
    @property
    def serialize(self):

        """
        Return object data in easily serializeable format
        """

        context = {
            'id': self.id,
            'name': self.text_score,
            'create_at': self.create_at,
            }
        return context

    