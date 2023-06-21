import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import uuid
import sqlite3
from database import ChatRoom,Blog,FeedBack
from database import session



st.set_page_config(page_title="Sylvanus Community", layout="centered")
st.sidebar.title("Sylvanus Community")
rad = option_menu(options=["ChatRoom","BlogWriting","MovieRoom","GiveFeedBack"], menu_title="Sylvanus Community",orientation="horizontal")
st.sidebar.markdown("---")
st.markdown("""
	<style>
		.css-14xtw13{
			visibility: hidden;
		}
		.css-cio0dv{
			visibility: hidden;
		}
		.css-nahz7x{
			font-style: italic;
		}
		.e16nr0p34{
			font-size: 10px;
		}""", unsafe_allow_html=True)


if rad == "ChatRoom":
	for p in session.query(ChatRoom):
		st.success(p.Chat)
		

		def chatside():
			chat = st.sidebar.text_input(label="ChatHere")
			submit_but_for_chatroom = st.sidebar.button("Submit")

			if submit_but_for_chatroom:		
				chatter = ChatRoom(Chat=chat)
				session.add(chatter)
				session.commit()
				session.rollback()
	chatside()

if rad == "BlogWriting":
	for p in session.query(Blog):
		st.header(p.Title)
		st.text(p.BlogText)
		st.markdown("---")		
	title = st.sidebar.text_input(label="TitleHere") 
	Main_Blog = st.sidebar.text_area(label="BlogText")
	sub_blog = st.sidebar.button("Submit")
	if sub_blog:
		Blogger = Blog(Title=title,BlogText=Main_Blog,Image="None")
		session.add(Blogger)
		session.commit()


		pass


		
if rad == "MovieRoom":
	st.title("Sorry still on Development")
	MovieName = st.sidebar.text_input(label="MovieName")
	pass






if rad == "GiveFeedBack":	

	with st.form(key="form2"):
			
		Name = st.text_input(label="Name")
		Email = st.text_input(label="Email")
		Solution = st.text_area(label="Feedback")
		sub_feed = st.form_submit_button("Submit")
	if sub_feed:
		if Name and Email and Solution != "":
			feeder = FeedBack(Name=Name,Email=Email,FeedBack=Solution)
			session.add(feeder)
			session.commit()
			success_for_feedback = st.info("Thanks for the feedback")


		else:
			st.error("Input Required")

		
	
