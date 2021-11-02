from conduit.extensions import db
from conduit.models.base_model import BaseModel


# Aliases
session = db.session
Table = db.Table
Model = BaseModel
Column = db.Column
relationship = db.relationship
drop_all = db.drop_all
create_all = db.create_all


# Type aliases
Integer = db.Integer
String = db.String
Boolean = db.Boolean
Numeric = db.Numeric
DateTime = db.DateTime
Interval = db.Interval


# Utils
def create_fk(tablename, pk="id", nullable=False, **kwargs):
    """Create a FK column

    :param tablename: fk target table name
    :param pk: fk target pk
    :param nullable: is fk nullable
    :param kwargs: any parameters that can be passed
                   to sqlalchemy.sql.schema.ForeignKey
    :return: sqlalchemy.sql.schema.Column
    """
    return Column(
        Integer,
        db.ForeignKey(f"{tablename}.{pk}"), nullable=nullable, **kwargs
    )
