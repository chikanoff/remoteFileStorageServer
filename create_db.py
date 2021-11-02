from conduit.app import create_app, db


def main():
    app = create_app()

    with app.app_context():
        from conduit.models.user import User

        db.drop_all()
        db.create_all()
        # TODO
        # User.create()
