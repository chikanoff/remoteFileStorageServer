from conduit.database import Column, String, Model, create_fk, relationship


class File(Model):
    __tablename__ = "files"
    name = Column(String(256), nullable=False, unique=True)
    description = Column(String(256), nullable=True)
    # readonly / private / public
    mode = Column(String(64), nullable=False, default="readonly")
    path = Column(String(256), nullable=False, unique=True)
    owner_id = create_fk("users")
    ownner = relationship("User")


