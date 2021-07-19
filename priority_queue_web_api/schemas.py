from flask_marshmallow.fields import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import Job


class JobSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Job
        load_instance = True

    id = fields.Int(required=False)
    created_at = fields.DateTime(required=False)


job_schema = JobSchema()
