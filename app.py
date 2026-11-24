
import streamlit as st
from deep_translator import MyMemoryTranslator

st.set_page_config(
    page_title="Python Translator",
    page_icon="🌐",
    layout="centered"
)

# Theme Settings
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# Theme Colors
if st.session_state.dark_mode:
    bg_color = "#0E1117"
    text_color = "#FFFFFF"
    box_color = "#262730"
else:
    bg_color = "#FFFFFF"
    text_color = "#000000"
    box_color = "#F0F2F6"

st.markdown(f"""
<style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}

    h1, h2, h3, p, label, span {{
        color: {text_color};
    }}

    div[data-testid="stTextArea"] textarea {{
        background-color: {box_color};
        color: {text_color};
    }}

    div[data-testid="stSelectbox"] div {{
        background-color: {box_color};
        color: {text_color};
    }}

    .stButton button {{
        border-radius: 10px;
        font-weight: bold;
    }}
</style>
""", unsafe_allow_html=True)


col1, col2 = st.columns([4, 1])

with col2:
    if st.session_state.dark_mode:
        st.button("☀️ Light Mode", on_click=toggle_theme)
    else:
        st.button("🌙 Dark Mode", on_click=toggle_theme)


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
    "Chinese": "zh-CN",
    "Persian": "fa",
    "English": "en",
    "German": "de",
    "French": "fr",
    "Spanish": "es",
    "Arabic": "ar",
    "Turkish": "tr",
    "Italian": "it",
    "Russian": "ru",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Greek": "el",
    "Swedish": "sv",
    "Polish": "pl",
    "Ukrainian": "uk",
    "Hindi": "hi",
    "Urdu": "ur",
    "Hebrew": "he",
    "Indonesian": "id",
    "Vietnamese": "vi",
    "Thai": "th",
    "Danish": "da",
    "Norwegian": "no",
    "Finnish": "fi",
    "Romanian": "ro",
    "Czech": "cs",
    "Hungarian": "hu"

}

text = st.text_area("Enter your text:")
st.caption(f"Characters: {len(text)}")

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
                st.code(translated_text, language=None)

                st.code(translated_text, language=None)

                st.button(
                    "📋 Copy Translation",
                    on_click=st.write,
                    args=(translated_text,)
                )


            except Exception as e:
                st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text first.")
