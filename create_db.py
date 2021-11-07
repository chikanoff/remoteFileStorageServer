from conduit.app import create_app, db


def main():
    app = create_app()

    with app.app_context():
        # pylint: disable=W0611
        from conduit.models.user import User

        db.drop_all()
        db.create_all()

<<<<<<< HEAD
        with open("sql/users.sql", "r", encoding="utf-8") as f:
            for line in f.readlines():
                # pylint: disable-no-member
                db.session.execute(line)
                db.session.commit()
=======
        
>>>>>>> main


if __name__ == "__main__":
    main()
