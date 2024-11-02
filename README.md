# Voice Assistant

A simple Python-based voice assistant that uses `speech_recognition` for voice input, `wikipedia` for information retrieval, and `pyttsx3` for text-to-speech. This assistant can perform various tasks, like opening websites, searching Wikipedia, and playing music, using voice commands.

## Features

- **Voice Input**: Recognizes voice commands using Google's Speech Recognition API.
- **Text-to-Speech**: Responds with voice output using `pyttsx3`.
- **Commands Supported**:
  - Search Wikipedia
  - Open popular websites (YouTube, Google, GitHub, Stack Overflow, Spotify)
  - Play music
  - Open specific local disk drives
  - Exit the program with a "sleep" command

## Prerequisites

Make sure you have the following packages installed:

- `pyttsx3` for text-to-speech
- `speech_recognition` for recognizing voice commands
- `wikipedia-api` for retrieving information from Wikipedia
- `pyaudio` for accessing the microphone
- `webbrowser` (usually comes pre-installed with Python)
- `os` (built-in Python library)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/RealJe-emy/Voice-Assistant.git
2. Change into the project directory:
cd Voice-Assistant
3. Install the required packages:
pip install pyttsx3 SpeechRecognition wikipedia-api pyaudio
Note: If pyaudio installation fails on Windows, download the appropriate .whl file from here and install it with:
pip install path/to/pyaudio‑0.2.11‑cp311‑cp311‑win_amd64.whl
Usage
4. To start the voice assistant, run the following command:
python vassistant.py
Once running, the assistant will greet you and wait for voice commands. Here are some example commands:

"Wikipedia Python programming" - Searches Wikipedia for "Python programming" and reads a short summary.
"Open YouTube" - Opens the YouTube website.
"Play music" - Opens Spotify.
"Local disk D" - Opens the D:\ drive on your computer.
"Sleep" - Exits the program.
Project Structure
vassistant.py: The main script that runs the voice assistant.
Troubleshooting
Error: No module named 'pyaudio':
Install pyaudio by downloading the appropriate .whl file and installing it via pip.
Speech Recognition not working:
Ensure that your microphone is set up correctly and that you have an active internet connection, as Google Speech Recognition API requires it.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Google Speech Recognition API
Wikipedia API
pyttsx3
