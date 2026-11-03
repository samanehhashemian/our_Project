import streamlit as st
from deep_translator import MyMemoryTranslator


st.set_page_config(
    page_title="Python Translator",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 Python Translator")

st.write("Welcome to our university project!")

st.subheader("Translate your text")

text = st.text_area("Enter your text:")



col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        ["fa", "en"],
        format_func=lambda x: "Persian" if x == "fa" else "English"
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        ["en", "fa"],
        format_func=lambda x: "English" if x == "en" else "Persian"
    )

if st.button("Translate"):
    if text:
        try:
            translator = MyMemoryTranslator(
            source="fa-IR" if source_lang == "fa" else "en-GB",
            target="fa-IR" if target_lang == "fa" else "en-GB"
        )
        
            translated_text = translator.translate(text)

            st.success("Translation completed!")
            st.subheader("Translated Text:")
            st.write(translated_text)

        except Exception as e:
            st.error(f"Translation failed: {e}")

    else:
        st.warning("Please enter some text first.")