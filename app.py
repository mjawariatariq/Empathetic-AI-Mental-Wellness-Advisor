# app.py

import streamlit as st
from mental_peace_advisor.model_api import get_bot_response
from mental_peace_advisor.chat_ui import display_conversation
import speech_recognition as sr
import google.generativeai as genai

st.set_page_config(page_title="🧘 Mental Peace Advisor Bot", page_icon="💬", layout="centered")

# Inject CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f8;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 10px;
    }
    .stForm button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧘 Mental Peace Advisor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Your personal emotional support bot 🤖</p>", unsafe_allow_html=True)

# Language selection
lang_map = {
    "English": "en", "اردو": "ur", "سندھی (Sindhi)": "sd", "پنجابی (Punjabi)": "pa",
    "中文 (Chinese)": "zh", "العربية (Arabic)": "ar", "Français (French)": "fr",
    "Español (Spanish)": "es", "Deutsch (German)": "de", "فارسی (Persian)": "fa", "Türkçe (Turkish)": "tr"
}

LANGUAGE_CODES = {
    "en": "en-US", "ur": "ur-PK", "sd": "sd", "pa": "pa-IN", "zh": "zh-CN", "ar": "ar-SA",
    "fr": "fr-FR", "es": "es-ES", "de": "de-DE", "fa": "fa-IR", "tr": "tr-TR"
}

lang_display = st.selectbox("🌐 Select Language / زبان منتخب کریں:", list(lang_map.keys()))
selected_lang = lang_map[lang_display]
st.session_state.lang = selected_lang

if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Show conversation
display_conversation(st.session_state.conversation)

# Text input area
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 Message:", placeholder="Type your message here...")
    submitted = st.form_submit_button("✉️ Send")

if submitted:
    if user_input.strip():
        st.session_state.conversation.append(("user", user_input.strip()))
        reply = get_bot_response(user_input.strip(), language=st.session_state.lang)
        st.session_state.conversation.append(("bot", reply))
        display_conversation(st.session_state.conversation)
    else:
        st.warning("⚠️ Please enter a message before submitting.")

# Voice input section
st.markdown("---")
st.markdown("🎤 **Or speak to the bot:**")

if st.button("🗣️ Start Speaking"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎧 Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            lang_code = LANGUAGE_CODES.get(st.session_state.lang, "en-US")
            user_input = recognizer.recognize_google(audio, language=lang_code)
            st.success("✅ Audio recognized successfully!")
            st.write(f"🗨️ You said: {user_input}")

            st.session_state.conversation.append(("user", user_input.strip()))
            reply = get_bot_response(user_input.strip(), language=st.session_state.lang)
            st.session_state.conversation.append(("bot", reply))

            display_conversation(st.session_state.conversation)

        except sr.UnknownValueError:
            st.error("❌ Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"⚠️ Could not request results; {e}")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")