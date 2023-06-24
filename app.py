import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu
from PIL import Image
import uuid
import sqlite3
from database import ChatRoom,Blog,FeedBack
from database import session,Session

st.set_page_config(page_title="Sylvanus Community", layout="centered")
st.sidebar.markdown("""
                      <h1 claSS="kill">Sylvanus Community</h1>
                      <p class="css-nahz7x e16nr0p34">.................Pray for us</p>
                      <style>
					  	.kill{
							font-style: oblique;
							font-family: ui-monospace;
                            font-size: 70px;
                            text-align: center;					
                        }	
                        .css-nahz7x p{
							text-align: center;
							color: bisque;
						}
      
                      </style>
                      """, unsafe_allow_html=True)

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
   			.styles_terminalButton__3xUnY{
      				visibility: hidden;
			}
		</style>
		""", unsafe_allow_html=True)


if rad == "ChatRoom":
	for p in session.query(ChatRoom):
		st.success(p.Chat)
		session.close()

	def chatroom():
		chat = st.sidebar.text_input(label="ChatHere")
		submit_but_for_chatroom = st.sidebar.button("Submit")

		if submit_but_for_chatroom:
			if chat != "":
				Chater = ChatRoom(Chat=chat, Id=str(uuid.uuid4()))
				try:
					session.add(Chater)
					session.commit()
					session.close()
				except Exception:
					session.merge(Chater)
					session.close()
			else:
				st.warning("Input Required")
					

	chatroom()

if rad == "BlogWriting":
	for p in session.query(Blog):
		st.header(p.Title)
		st.text(p.BlogText)
		st.markdown("---")		
	title = st.sidebar.text_input(label="TitleHere") 
	Main_Blog = st.sidebar.text_area(label="BlogText")
	sub_blog = st.sidebar.button("Submit")
	if sub_blog:
		if title and Main_Blog != "":
			Blogger = Blog(Title=title,BlogText=Main_Blog,Image="None",Id=str(uuid.uuid4()))
			try:
				session.add(Blogger)
				session.commit()
				session.close()
			except Exception:
				session.merge(Blogger)
				session.close()
		else:
			st.warning("Input Required")
    	
			

		
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
			feeder = FeedBack(Name=Name,Email=Email,FeedBack=Solution,Id=str(uuid.uuid4()))
			try:
				session.add(feeder)
				session.commit()
				session.close()
				success_for_feedback = st.info("Thanks for the feedback")

			except Exception:
				session.merge(feeder)
				session.close()
				success_for_feedback = st.info("Thanks for the feedback")


		else:
			st.error("Input Required")

		
	
