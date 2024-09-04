import streamlit as st

st.set_page_config(layout="wide")

# creating two columns
column1, column2 = st.columns(2)

with column1:
    st.image("images/Profile Picture.jpg", width=500)

with column2:
    st.title("Jordan Ward")
    content = """
    Hi, my name is Jordan!
    """

    # can use .info or .write, two different backgrounds for the text
    st.info(content)