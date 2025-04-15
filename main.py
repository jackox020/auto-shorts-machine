from gpt_script_engine import generate_script
from voiceover import generate_voice
from video_editor import create_video
from uploader import upload_to_youtube

def run_pipeline(topic):
    print(f"Generating viral short for: {topic}")
    script = generate_script(topic)
    audio_path = generate_voice(script)
    video_path = create_video(script, audio_path)
    upload_to_youtube(video_path, script)
    print("Short created and uploaded!")

if __name__ == "__main__":
    run_pipeline("This AI tool makes you money while you sleep")
