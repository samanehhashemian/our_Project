
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

languages = {
    "Persian": "fa-IR",
    "English": "en-GB",
    "German": "de-DE",
    "French": "fr-FR",
    "Spanish": "es-ES",
    "Arabic": "ar-SA",
    "Turkish": "tr-TR",
    "Italian": "it-IT",
    "Russian": "ru-RU",
    "Chinese": "zh-CN"
}

text = st.text_area("Enter your text:")

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

if st.button("Translate"):
    if text:
        if source_lang == target_lang:
            st.warning("Please select two different languages.")
        else:
            try:
                translator = MyMemoryTranslator(
                    source=languages[source_lang],
                    target=languages[target_lang]
                )

                translated_text = translator.translate(text)

                st.success("Translation completed!")
                st.subheader("Translated Text:")
                st.write(translated_text)

            except Exception as e:
                st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text first.")
