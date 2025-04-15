from gtts import gTTS

def generate_voice(script_text):
    full_text = script_text.replace("HOOK:", "").replace("BODY:", "").replace("ENDING:", "")
    tts = gTTS(full_text)
    output_path = "voiceover.mp3"
    tts.save(output_path)
    return output_path
