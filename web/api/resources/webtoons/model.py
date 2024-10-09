from datetime import datetime
from web.api.resources.webtoons import utils
from mongoengine import Document, StringField, DateTimeField, ListField


class Webtoon(Document):
    prepend_string = 'webtoons'

    webtoons_id = StringField(required=True)
    title = StringField(required=True, max_length=100)
    description = StringField(required=True)
    characters = ListField(StringField(), required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    @classmethod
    def generate_id(cls):
        return utils.generate_id(cls.prepend_string)

    @classmethod
    def to_dict(cls, self):
        return {
            'id': self.webtoons_id,
            'title': self.title,
            'description': self.description,
            'characters': self.characters,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
