from sqlalchemy import Column, Integer, ForeignKey, Text, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    post_user = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    date = Column(String, nullable=False)
    url = Column(Text, nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    answer_id = Column(Integer, ForeignKey("answers.id"), nullable=True)

    group = relationship("Group")
    user = relationship("User")
    answer = relationship("Answer")
