import streamlit as st
import time

st.set_page_config(page_title="Finance Assistant", layout="centered")

st.title("📈 AI-Powered Market Brief Assistant")
st.write("Simulated Voice/Text AI Agent | Intern Assignment")

st.markdown("---")

# Input mode
mode = st.radio("Input Mode", ["Text", "Voice (Simulated)"])

if mode == "Text":
    user_input = st.text_input("Enter your market query", "What’s our risk exposure in Asia tech stocks today?")
else:
    audio_file = st.file_uploader("Upload a voice (.mp3)", type=["mp3", "wav"])
    if audio_file:
        st.audio(audio_file, format='audio/mp3')
        user_input = "Simulated transcription: What’s our risk exposure in Asia tech stocks today?"

# Simulate backend call
if st.button("Ask Agent"):
    with st.spinner("Calling agents..."):
        time.sleep(2)

        st.subheader("✅ API Agent Output")
        st.json({
            "ticker": "TSMC",
            "current_price": 110,
            "previous_close": 105,
            "change_percent": 4.76
        })

        st.subheader("✅ Scraper Agent Output")
        st.write("TSMC beat estimates by 4%, Samsung missed by 2%.")

        st.subheader("✅ Retriever Agent Output")
        st.write("Past filings: TSMC and Samsung quarterly performance summary retrieved.")

        st.subheader("🧠 Language Agent Summary")
        st.success("Today, your Asia tech allocation is 22% of AUM, up from 18% yesterday. TSMC beat estimates by 4%, Samsung missed by 2%. Regional sentiment is neutral with a cautionary tilt due to rising yields.")

        st.subheader("🔊 Voice Agent (TTS)")
        st.write("Simulated audio playback")
        st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/gettysburg10.wav")  # placeholder audio

   
