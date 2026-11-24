
import streamlit as st
from deep_translator import MyMemoryTranslator

# Page Configuration
st.set_page_config(
    page_title="Python Translator",
    page_icon="🌐",
    layout="centered"
)

# Session State
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

# Theme Function
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

# Custom CSS
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

# Dark / Light Mode Button
col1, col2 = st.columns([4, 1])

with col2:
    if st.session_state.dark_mode:
        st.button("☀️ Light Mode", on_click=toggle_theme)
    else:
        st.button("🌙 Dark Mode", on_click=toggle_theme)

# Application Title
st.title("🌐 Python Translator")
st.write("Welcome to our university project!")
st.subheader("Translate your text")

# Supported Languages
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
    "Japanese": "ja-JP",
    "Korean": "ko-KR",
    "Portuguese": "pt-PT",
    "Dutch": "nl-NL",
    "Greek": "el-GR",
    "Swedish": "sv-SE",
    "Polish": "pl-PL",
    "Ukrainian": "uk-UA",
    "Hindi": "hi-IN",
    "Urdu": "ur-PK",
    "Hebrew": "he-IL",
    "Indonesian": "id-ID",
    "Vietnamese": "vi-VN",
    "Thai": "th-TH",
    "Danish": "da-DK",
    "Norwegian": "nb-NO",
    "Finnish": "fi-FI",
    "Romanian": "ro-RO",
    "Czech": "cs-CZ",
    "Hungarian": "hu-HU"
}

# Text Input
text = st.text_area("Enter your text:")

st.caption(f"Characters: {len(text)}")

# Language Selection
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

# Translation Button
if st.button("Translate", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text first.")

    elif source_lang == target_lang:
        st.warning("Please select two different languages.")

    else:
        try:
            with st.spinner("Translating..."):

                translator = MyMemoryTranslator(
                    source=languages[source_lang],
                    target=languages[target_lang]
                )

                result = translator.translate(text=text)

            if result:
                st.session_state.translated_text = result
                st.success("Translation completed!")

            else:
                st.session_state.translated_text = ""
                st.error("Translation result is empty.")

        except Exception as e:
            st.session_state.translated_text = ""
            st.error(f"Translation failed: {e}")

# Translation Result
if st.session_state.translated_text:

    st.subheader("Translated Text:")

    st.text_area(
        "Your Translation:",
        value=st.session_state.translated_text,
        height=150,
        disabled=True
    )

    # Copy Button
    st.button(
        "📋 Copy Translation",
        on_click=lambda: st.toast("Use Ctrl+C to copy the selected text.")
    )
