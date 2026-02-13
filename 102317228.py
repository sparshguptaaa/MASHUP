import sys
import os
import shutil
import yt_dlp
from moviepy.editor import VideoFileClip
from pydub import AudioSegment



def makefolders():
    folders = ["videos", "audios", "trimmed"]
    for folder in folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)



def downloadvideos(singer_name, total_videos):
    print("Downloading videos...")

    search_query = f"ytsearch{total_videos}:{singer_name}"

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'videos/%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])

    print("Download completed.\n")



def convert_to_audio():
    print("Converting videos to audio...")

    for file in os.listdir("videos"):
        video_path = os.path.join("videos", file)

        try:
            clip = VideoFileClip(video_path)
            audio_path = os.path.join("audios", file + ".mp3")
            clip.audio.write_audiofile(audio_path)
            clip.close()
        except Exception as e:
            print("Error converting:", file, e)

    print("Conversion completed.\n")



def trim_audio(duration):
    print(f"Trimming first {duration} seconds...")

    for file in os.listdir("audios"):
        audio_path = os.path.join("audios", file)

        try:
            sound = AudioSegment.from_file(audio_path)
            trimmed = sound[:duration * 1000]
            trimmed.export(os.path.join("trimmed", file), format="mp3")
        except Exception as e:
            print("Error trimming:", file, e)

    print("Trimming completed.\n")



def merge_audio(output_filename):
    print("Merging audio files...")

    final_audio = AudioSegment.empty()

    for file in os.listdir("trimmed"):
        file_path = os.path.join("trimmed", file)
        sound = AudioSegment.from_file(file_path)
        final_audio += sound

    final_audio.export(output_filename, format="mp3")

    print("Mashup created successfully:", output_filename)



def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <SingerName> <NumberOfVideos> <Duration> <OutputFile>")
        sys.exit()

    try:
        singer = sys.argv[1]
        number = int(sys.argv[2])
        duration = int(sys.argv[3])
        output_file = sys.argv[4]

        if number <= 10:
            raise ValueError("Number of videos must be greater than 10")

        if duration <= 20:
            raise ValueError("Duration must be greater than 20 seconds")

    except ValueError as ve:
        print("Input Error:", ve)
        sys.exit()

    makefolders()
    downloadvideos(singer, number)
    convert_to_audio()
    trim_audio(duration)
    merge_audio(output_file)


if __name__ == "__main__":
    main()
