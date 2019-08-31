from util.orm import Base, engine
from .topic import Topic

Base.metadata.create_all(engine)
