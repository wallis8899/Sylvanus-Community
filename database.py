from sqlalchemy import create_engine,String,ForeignKey,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
import random

Base = declarative_base()
class ChatRoom(Base):
	__tablename__ = "ChatRoom"
	Id = Column("Id",String,primary_key=True)
	Chat = Column("Chat",String)

	"""docstring for ClassName"""
	def __init__(self, Chat,Id):
		self.Chat = Chat
		self.Id = Id


class Blog(Base):
	__tablename__ = "Blog"
	Id = Column("Id",String,primary_key=True)
	Title = Column("Title",String)
	Image = Column("Image",String)
	BlogText = Column("BlogText",String)

	"""docstring for ClassName"""
	def __init__(self, Title,Image,BlogText,Id):
		self.Title = Title
		self.Image = Image
		self.BlogText = BlogText
		self.Id = Id


class FeedBack(Base):
	__tablename__ = "FeedBack"
	Id = Column("Id",String,primary_key=True)
	Name = Column("Name",String)
	Email = Column("Email",String)
	FeedBack = Column("FeedBack",String)

	"""docstring for ClassName"""
	def __init__(self, Name,Email,FeedBack,Id):
		self.Name = Name
		self.Email = Email
		self.FeedBack = FeedBack
		self.Id = Id

class Movies(Base):
	__tablename__ = "Movies"
	Id = Column("Id",String,primary_key=True)
	Name = Column("Name",String)
	Link = Column("Link",String)
	Category = Column("Category",String)

	def __init__(self, Name,Link,Category,Id):
		self.Name = Name
		self.Link = Link
		self.Category = Category
		self.Id = Id



db = "sqlite:///database/Sylvanusdb.db"
engine = create_engine(db)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
