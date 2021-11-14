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
    def getAdminFiles(cls):
        files = cls.query.all()
        return files

    @classmethod
    def getPublicFiles(cls):
        files = cls.query.filter(cls.mode == "public").all()
        return files

    @classmethod
    def getOne(cls, file_id):
        file = cls.query.filter(cls.id == file_id).first_or_404()
        return file
