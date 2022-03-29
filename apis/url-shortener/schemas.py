from extensions import ma

from models import Link

from marshmallow import fields, ValidationError

def validateUrl(url):
    if not url.startswith(("http://", "https://")):
        raise ValidationError("Invalid URL format")

class LinkSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Link
        include_fk = True

    url = fields.String(required=True, validate=validateUrl)