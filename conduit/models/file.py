from conduit.database import Column, String, Model, create_fk, relationship


class File(Model):
    __tablename__ = "files"
    name = Column(String(256), nullable=False, unique=True)
    description = Column(String(256), nullable=True)
    # readonly / private / public
    mode = Column(String(64), nullable=False, default="readonly")
    path = Column(String(256), nullable=False, unique=True)
    owner_id = create_fk("users")
    owner = relationship("User")

    @classmethod
    def create(cls, name, desc, mode, path, owner_id):
        instance = cls(
            name = name, 
            description = desc, 
            mode = mode, 
            path = path, 
            owner_id = owner_id
        )
        return instance.save()

    @classmethod
    def getAdminFiles(cls):
        files = cls.query.all()
        return files

    @classmethod
    def getUserFiles(cls, user_id):
        files = cls.query.filter(cls.owner_id == user_id).all()
        return files

    @classmethod
    def getPublicFiles(cls):
        files = cls.query.filter(cls.mode == "public").all()
        return files

    @classmethod
    def getOne(cls, file_id):
        file = cls.query.filter(cls.id == file_id).first_or_404()
        return file
