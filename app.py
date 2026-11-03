import streamlit as st

st.set_page_config(
    page_title="Python Translator",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 Python Translator")

st.write("Welcome to our university project!")

st.subheader("Translate your text")

text = st.text_area("Enter your text:")

if st.button("Translate"):
    if text:
        st.info("Your text will be translated here.")
    else:
        st.warning("Please enter some text first.")