from sqlalchemy import Column, Integer, String, Boolean
from util.orm import Base


# 创建单表
class Topic(Base):
    __tablename__ = 'topic'

    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    url = Column(String(512))
    like_count = Column(Integer)
    like_it = Column(Boolean)

    def __init__(self, title, url, like_count, like_it):
        self.title = title
        self.url = url
        self.like_count = like_count
        self.like_it = like_it
