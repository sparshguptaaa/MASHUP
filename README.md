

# 🎵 YouTube Mashup Generator

A full-stack Python application that:
Downloads N YouTube videos of a given singer
Converts them to audio
Extracts first Y seconds from each
Merges them into a single mashup
Sends the mashup as a ZIP file via email

Built using:

Python 3.12

yt-dlp

MoviePy (1.0.3)

Pydub

Streamlit

# 📌 Features

✔ Command-line version (Program 1)

✔ Web-based Streamlit interface (Program 2)

✔ Email delivery with ZIP attachment

✔ Input validation

✔ Clean workspace handling

✔ Custom UI with gradient background

✔ Modular function design

# 🛠 Tech Stack 

| Tool       | Purpose                      |
|------------|-----------------------------|
| Python     | Core programming language   |
| yt-dlp     | Download YouTube videos     |
| MoviePy    | Convert video to audio      |
| Pydub      | Trim and merge audio        |
| Streamlit  | Web interface               |

# Command Line Version
python 102317228.py "Name of Singer" Number of songs duration of each clip output.mp3

#🌐 Program 2 — Streamlit Web Version
streamlit run app.py
http://localhost:8501

```mermaid
flowchart TD
    A[User Input] --> B[Streamlit UI]
    B --> C[Download YouTube Videos]
    C --> D[Extract Audio]
    D --> E[Trim First Y Seconds]
    E --> F[Merge Audio Files]
    F --> G[Create ZIP]
    G --> H[Send Email]
    H --> I[User Receives Mashup]
```

# 🔄 CLI Workflow
```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant yt-dlp
    participant MoviePy
    participant Pydub

    User->>CLI: Provide Arguments
    CLI->>yt-dlp: Download Videos
    yt-dlp-->>CLI: Videos Saved
    CLI->>MoviePy: Extract Audio
    CLI->>Pydub: Trim Clips
    CLI->>Pydub: Merge Clips
    CLI-->>User: Output MP3 Generated
```
# 📦 Web App Workflow
```mermaid
flowchart LR
    UI[Web Form] --> Validate[Validate Input]
    Validate --> Download
    Download --> Convert
    Convert --> Trim
    Trim --> Merge
    Merge --> Zip
    Zip --> Email
```
# 📊 Folder Data Flow
```mermaid
graph TD
    A[YouTube] --> B[raw_clips]
    B --> C[sound_tracks]
    C --> D[snippets]
    D --> E[custom_mashup.mp3]
    E --> F[final_package.zip]
```
# 🔐 Email Delivery Process
```mermaid
flowchart TD
    A[ZIP File Created] --> B[SMTP_SSL]
    B --> C[Login with App Password]
    C --> D[Attach ZIP]
    D --> E[Send Email]
```
# 🎉 Final Outcome
The application successfully:

Downloads content from YouTube

Processes audio

Generates mashup

Provides CLI interface

Provides Web interface

Sends mashup via email

# 👨‍💻 Author

## Name :Sparsh Gupta
Roll Number: 102317228
Course: Python Programming
Assignment: YouTube Mashup Generator


