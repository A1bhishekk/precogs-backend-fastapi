
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from db.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func  # Import func for handling timestamps

class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    github_id = Column(Integer, unique=True)
    email = Column(String(50), unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)  # Automatic creation timestamp

    projects = relationship(
        "DbProject",
        back_populates="user",
        cascade="all, delete-orphan"
    )

class DbProject(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    github_url = Column(String(50))
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)  # Automatic creation timestamp

    user = relationship(
        "DbUser",
        back_populates="projects"
    )
