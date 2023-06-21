from sqlalchemy import create_engine,String,ForeignKey,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
import random

Base = declarative_base()
class ChatRoom(Base):
	__tablename__ = "ChatRoom"
	postId1 = Column("Id",String,primary_key=True,default=str(uuid.uuid4()), unique=True)
	Chat = Column("Chat",String)

	"""docstring for ClassName"""
	def __init__(self, Chat):
		self.Chat = Chat


class Blog(Base):
	__tablename__ = "Blog"
	postId2 = Column("Id",String,primary_key=True,default=str(uuid.uuid4()))
	Title = Column("Title",String)
	Image = Column("Image",String)
	BlogText = Column("BlogText",String)

	"""docstring for ClassName"""
	def __init__(self, Title,Image,BlogText):
		self.Title = Title
		self.Image = Image
		self.BlogText = BlogText 


class FeedBack(Base):
	__tablename__ = "FeedBack"
	postId2 = Column("Id",String,primary_key=True,default=str(uuid.uuid4()))
	Name = Column("Name",String)
	Email = Column("Email",String)
	FeedBack = Column("FeedBack",String)

	"""docstring for ClassName"""
	def __init__(self, Name,Email,FeedBack):
		self.Name = Name
		self.Email = Email
		self.FeedBack = FeedBack 

class Movies(Base):
	__tablename__ = "Movies"
	postId2 = Column("Id",String,primary_key=True,default=str(uuid.uuid4()))
	Name = Column("Name",String)
	Link = Column("Link",String)
	Category = Column("Category",String)

	def __init__(self, Name,Link,Category):
		self.Name = Name
		self.Link = link
		self.Category = Category 



db = "sqlite:///database/Sylvanusdb.db"
engine = create_engine(db)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()