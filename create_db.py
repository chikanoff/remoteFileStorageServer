import json
from conduit.app import create_app, db
from conduit.models.user import User

# from conduit.models.file import File


def insert_table_from_json(path, model_cls):
    app = create_app()
    with app.app_context():
        with open(path, "r", encoding="utf-8") as f:
            rows = json.loads(f.read())
            for row in rows:
                db.session.add(model_cls(**row))
            db.session.commit()


def main():
    app = create_app()

    with app.app_context():
        db.drop_all()
        db.create_all()

        # fill the table
        insert_table_from_json("insert_data/users.json", User)
        # insert_table_from_json("insert_data/files.json", File)


if __name__ == "__main__":
    main()
