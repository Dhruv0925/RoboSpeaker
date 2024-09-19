import subprocess
import sys

# Function to install pyttsx3 if not already installed
def install_pyttsx3():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyttsx3"])

try:
    import pyttsx3
except ImportError:
    install_pyttsx3()
    import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.1. Created by Harry")
    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "q":
            speak("bye bye friend")
            break
        speak(x)
