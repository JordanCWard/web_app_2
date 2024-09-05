import streamlit as st

st.set_page_config(layout="wide")

# creating two columns
column1, column2 = st.columns(2)

with column1:
    st.image("images/Profile Picture.jpg", width=400)

with column2:
    st.title("Jordan Ward")
    content = """
    Hi, I’m Jordan, a data enthusiast with a master’s in mathematics education.
    I enjoy data analysis, problem-solving and effective communication.
    Beyond work, I enjoy spending time with my wife and our dog, mountain biking, 
    snowboarding, traveling and playing chess.
    """

    # can use .info or .write, two different backgrounds for the text
    st.info(content)

info_about_apps = """
    Below you can find some of the apps I have built in Pythin. Feel free to contact me!
    """

st.write(info_about_apps)