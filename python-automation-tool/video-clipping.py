import moviepy.editor as mp

# defining variables
input_file = None
start_time = None
end_time = None
output_file = None


def make_clip(input_file, start_time, end_time, output_file):
    video_codec = 'h264'
    audio_codec = 'aac'
    clip = mp.VideoFileClip(input_file).subclip(start_time, end_time)
    # audio_codec = clip.audio.fps
    # clip.write_videofile(output_file, audio_codec=audio_codec)
    # clip.write_videofile(output_file, audio_codec='aac')
    clip.write_videofile(output_file, codec=video_codec,
                         audio_codec=audio_codec)


def parse_time(time_str):
    if not time_str:
        return None
    h, m, s = map(int, time_str.split(':'))
    return 3600 * h + 60 * m + s


if __name__ == '__main__':
    while not input_file:
        input_file = input("Enter the input file name (mkv or mp4): ")
    start_time = parse_time(input("Enter the start time (in hh:mm:ss format) (optional): ")
                            ) if not "start_time" in locals() or not start_time else start_time
    end_time = parse_time(input("Enter the end time (in hh:mm:ss format) (optional): ")
                          ) if not "end_time" in locals() or not end_time else end_time
    output_file = input("Enter the output file name (optional): ") if not "output_file" in locals(
    ) or not output_file else output_file

    if not "output_file" in locals() or not output_file:
        output_file = f"{input_file.split('.')[0]}_clipped.{input_file.split('.')[1]}"
    if not start_time:
        start_time = 0
    if not end_time:
        end_time = None

    make_clip(input_file, start_time, end_time, output_file)
