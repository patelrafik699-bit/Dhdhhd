import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import requests

# Initialize the voice engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # speaking speed

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice input and convert to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query.lower()
    except Exception:
        speak("Sorry, I didn't catch that.")
        return ""

def wish_me():
    """Greet the user"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I help you today?")

def get_weather(city="London"):
    """Fetch weather info using wttr.in"""
    try:
        res = requests.get(f"https://wttr.in/{city}?format=3")
        return res.text
    except:
        return "Sorry, I couldn't fetch the weather."

def run_jarvis():
    wish_me()
    while True:
        query = listen()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except:
                speak("No results found on Wikipedia.")

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "weather" in query:
            city = "London"  # default, you can customize
            speak(f"The weather in {city} is {get_weather(city)}")

        elif "stop" in query or "quit" in query or "exit" in query:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("I can search Wikipedia, open YouTube, Google, and tell you the weather.")

if __name__ == "__main__":
    run_jarvis()
  
