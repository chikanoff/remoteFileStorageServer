from conduit.app import create_app, db
from fill_db import fill_db


def main():
    app = create_app()

    with app.app_context():
        # pylint: disable=W0611

        db.drop_all()
        db.create_all()

        fill_db()


if __name__ == "__main__":
    main()
