import streamlit as st
import os
import shutil
import yt_dlp
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import zipfile
import smtplib
from email.message import EmailMessage



def initialize_environment():
    folders = ["raw_clips", "sound_tracks", "snippets"]

    for folder in folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)



def fetch_youtube_content(artist_name, clip_count):

    query = f"ytsearch{clip_count}:{artist_name}"

    options = {
    'format': 'bestaudio/best',
    'outtmpl': 'raw_clips/%(title)s.%(ext)s',
    'quiet': True,
    'noplaylist': True,
    'socket_timeout': 60
    }


    with yt_dlp.YoutubeDL(options) as downloader:
        downloader.download([query])



def extract_soundtracks():

    for file in os.listdir("raw_clips"):
        video_path = os.path.join("raw_clips", file)

        clip = VideoFileClip(video_path)
        audio_path = os.path.join("sound_tracks", file + ".mp3")
        clip.audio.write_audiofile(audio_path)
        clip.close()



def generate_audio_snippets(seconds):

    for file in os.listdir("sound_tracks"):
        track_path = os.path.join("sound_tracks", file)

        audio = AudioSegment.from_file(track_path)
        short_clip = audio[:seconds * 1000]

        short_clip.export(os.path.join("snippets", file), format="mp3")



def build_final_mix(output_name):

    combined_audio = AudioSegment.empty()

    for file in os.listdir("snippets"):
        snippet_path = os.path.join("snippets", file)
        segment = AudioSegment.from_file(snippet_path)
        combined_audio += segment

    combined_audio.export(output_name, format="mp3")



def package_output(file_name):

    zip_name = "final_package.zip"

    with zipfile.ZipFile(zip_name, 'w') as zipf:
        zipf.write(file_name)

    return zip_name



def deliver_to_email(receiver, attachment_file):

    sender = "ishug9578@gmail.com"
    app_password = "kddcjwavilwbogcc"

    message = EmailMessage()
    message["Subject"] = "Your Custom Mashup"
    message["From"] = sender
    message["To"] = receiver
    message.set_content("Please find your mashup attached.")

    with open(attachment_file, "rb") as file:
        message.add_attachment(
            file.read(),
            maintype="application",
            subtype="zip",
            filename=attachment_file
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, app_password)
        server.send_message(message)



st.set_page_config(
    page_title="Mashup Creator",
    page_icon="🎵",
    layout="wide"
)


st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1f1c2c, #928DAB);
        color: white;
    }

    .stTextInput>div>div>input {
        background-color: #2c2c54;
        color: white;
    }

    .stNumberInput>div>div>input {
        background-color: #2c2c54;
        color: white;
    }

    .stButton>button {
        background-color: #ff4b2b;
        color: white;
        border-radius: 10px;
        height: 50px;
        width: 100%;
        font-size: 18px;
    }

    .stButton>button:hover {
        background-color: #ff416c;
        color: white;
    }

    </style>
""", unsafe_allow_html=True)


st.sidebar.title("🎧 Mashup Settings")
st.sidebar.markdown("Enter details below to generate your custom mashup.")

artist = st.sidebar.text_input("Singer Name")
video_count = st.sidebar.number_input("Number of Videos (>10)", min_value=11)
clip_duration = st.sidebar.number_input("Clip Duration (>20 sec)", min_value=21)
user_email = st.sidebar.text_input("Email Address")

generate = st.sidebar.button("🚀 Generate Mashup")


st.title("🎶 Custom Mashup Creator")

artist = st.text_input("Enter Singer Name")
video_count = st.number_input("Number of Videos (must be >10)", min_value=11)
clip_duration = st.number_input("Clip Duration in Seconds (must be >20)", min_value=21)
user_email = st.text_input("Enter Email Address")

if st.button("Create Mashup"):

    if not artist or not user_email:
        st.error("All fields are required.")
    else:
        try:
            st.write("Setting up workspace...")
            initialize_environment()

            st.write("Fetching videos...")
            fetch_youtube_content(artist, video_count)

            st.write("Extracting audio...")
            extract_soundtracks()

            st.write("Generating snippets...")
            generate_audio_snippets(clip_duration)

            final_file = "custom_mashup.mp3"

            st.write("Combining audio...")
            build_final_mix(final_file)

            st.write("Packaging file...")
            zip_file = package_output(final_file)

            st.write("Sending to email...")
            deliver_to_email(user_email, zip_file)

            st.success("Mashup successfully created and delivered!")

        except Exception as error:
            st.error(f"Something went wrong: {error}")
