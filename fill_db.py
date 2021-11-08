import json

from conduit.app import create_app, db
from conduit.models.user import User


def insert_from_json(path, cls_):
    app = create_app()
    with app.app_context():

        with open(path) as f:
            args_list = json.loads(f.read())
            for args in args_list:
                db.session.add(cls_(**args))
            db.session.commit()


def fill_db():
    insert_from_json('insert_data/users.json', User)
