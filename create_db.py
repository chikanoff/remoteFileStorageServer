from conduit.app import create_app, db
import json


def main():
    app = create_app()

    with app.app_context():
        from conduit.models.user import User

        db.drop_all()
        db.create_all()

        f = open('testData.json',)

        # load json file with data
        data = json.load(f)

        # fill db users
        for i in data['users']:
            user = User.create(i['firstName'], i['lastName'], i['email'],
                               i['username'], i['password'], i['role'])
            db.session.add(user)
            db.session.commit()


if __name__ == '__main__':
    main()
