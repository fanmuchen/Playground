#还没测试过不知道好不好用

import os
import ffmpeg

input_dir = ""
output_dir = ""
output_format = "mp4"
video_codec = "libx264"
audio_codec = "aac"

# prompt the user for the 5 options if not specified in the script
if not 'input_dir' in locals() or not input_dir:
    input_dir = input("Enter the input directory: ")
if not 'output_dir' in locals() or not output_dir:
    output_dir = input("Enter the output directory: ")
if not 'output_format' in locals() or not output_format:
    output_format = input("Enter the output format (e.g. mp4): ")
if not 'video_codec' in locals() or not video_codec:
    video_codec = input("Enter the video codec to use (e.g. libx264): ")
if not 'audio_codec' in locals() or not audio_codec:
    audio_codec = input("Enter the audio codec to use (e.g. aac): ")

for filename in os.listdir(input_dir):
    if filename.endswith(".mp4") or filename.endswith(".avi"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[
                                   0] + "." + output_format)
        (
            ffmpeg
            .input(input_path)
            .output(output_path, codec=output_format, video_codec=video_codec, audio_codec=audio_codec)
            .overwrite_output()
            .run()
        )
