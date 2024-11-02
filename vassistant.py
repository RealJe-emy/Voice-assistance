import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

# Initialize pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # Set voice to female (1 for female, 0 for male)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak("I didn't understand")
        return "None"
    return query


if __name__ == '__main__':
    speak("Wassup am Jdawg.")
    speak("How can I help you?")

    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'are you' in query:
            speak("I'm Jdawg, developed by RealJe-emy")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open github' in query:
            speak("Opening GitHub")
            webbrowser.open("github.com")

        elif 'open stackoverflow' in query:
            speak("Opening Stack Overflow")
            webbrowser.open("stackoverflow.com")

        elif 'open spotify' in query:
            speak("Opening Spotify")
            webbrowser.open("spotify.com")

        elif 'play music' in query:
            speak("Opening music")
            webbrowser.open("spotify.com")

        elif 'local disk d' in query:
            speak("Opening Local Disk D")
            webbrowser.open("D://")

        elif 'local disk c' in query:
            speak("Opening Local Disk C")
            webbrowser.open("C://")

        elif 'local disk e' in query:
            speak("Opening Local Disk E")
            webbrowser.open("E://")

        elif 'sleep' in query:
            speak("Goodbye")
            exit(0)
