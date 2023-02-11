#一个粗劣的从视频生成srt的脚本，缺乏断句功能，几乎不可用


import moviepy.editor as mp
from pydub import AudioSegment
import speech_recognition as sr

def extract_audio(video_file, audio_file):
    video = mp.VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file)

def recognize_speech(audio_file, language='zh-CN'):
    recognizer = sr.Recognizer()
    sound = AudioSegment.from_file(audio_file, format="wav")

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    text = recognizer.recognize_google(audio_data, language=language)
    return text

def generate_subtitle(text, output_file):
    lines = text.split(".")
    lines = [line.strip() for line in lines if line.strip()]

    with open(output_file, 'w') as f:
        for i, line in enumerate(lines):
            start = i * 1000
            end = start + 1000
            f.write(f"{i}\n{start} --> {end}\n{line}\n\n")

if __name__ == '__main__':
    video_file = "/Users/xxxx.mp4"
    audio_file = "audio.wav"
    subtitle_file = "subtitle.srt"

    extract_audio(video_file, audio_file)
    text = recognize_speech(audio_file)
    generate_subtitle(text, subtitle_file)