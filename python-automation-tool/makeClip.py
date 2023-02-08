import moviepy.editor as mp


def make_clip(input_file, start_time, end_time, output_file):
    clip = mp.VideoFileClip(input_file).subclip(start_time, end_time)
    clip.write_videofile(output_file)


def parse_time(time_str):
    h, m, s = map(int, time_str.split(':'))
    return 3600 * h + 60 * m + s


if __name__ == '__main__':
    input_file = input("Enter the input file name (mkv or mp4): ")
    start_time = parse_time(
        input("Enter the start time (in hh:mm:ss format): "))
    end_time = parse_time(input("Enter the end time (in hh:mm:ss format): "))
    output_file = input("Enter the output file name: ")
    make_clip(input_file, start_time, end_time, output_file)
