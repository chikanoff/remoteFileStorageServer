from conduit.app import create_app, db


def main():
    app = create_app()

    with app.app_context():
        from conduit.models.user import User

        db.drop_all()
        db.create_all()

        with open('sql/users.sql') as f:
            for line in f.readlines():
                db.session.execute(line)
                db.session.commit()


if __name__ == '__main__':
    main()
