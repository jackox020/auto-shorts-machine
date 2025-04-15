from moviepy.editor import *

def create_video(script, audio_path):
    video = ColorClip(size=(1080, 1920), color=(0, 0, 0), duration=60)
    audio = AudioFileClip(audio_path)
    video = video.set_audio(audio).set_duration(audio.duration)
    output_path = "short_output.mp4"
    video.write_videofile(output_path, fps=24)
    return output_path
