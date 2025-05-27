# agents/voice_agent.py
import whisper
from gtts import gTTS
import os

class VoiceAgent:
    def __init__(self):
        self.stt_model = whisper.load_model("base")
    
    def speech_to_text(self, audio_file):
        try:
            result = self.stt_model.transcribe(audio_file)
            confidence = result["segments"][0]["confidence"] if result["segments"] else 0.0
            if confidence < 0.7:
                return {"text": result["text"], "fallback": "Please clarify your query."}
            return {"text": result["text"], "fallback": None}
        except Exception as e:
            return {"text": "", "fallback": f"Error processing audio: {str(e)}"}
    
    def text_to_speech(self, text, output_file="output.mp3"):
        tts = gTTS(text=text, lang='en')
        tts.save(output_file)
        return output_file