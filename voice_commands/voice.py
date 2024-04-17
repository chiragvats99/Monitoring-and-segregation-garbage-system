import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_sphinx(audio)  # Use pocketsphinx for local recognition
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Error: {e}")
        return ""

def main():
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hello there!")

        elif "how are you" in query:
            speak("I'm doing well, thank you!")

        elif "goodbye" in query:
            speak("Goodbye! Have a great day!")
            break

        elif "status" in query and "bin" in query:
            # Code to check status of the bin and speak the result
            speak("The bin is half full.")

        elif "open" in query:
            # Code to open the bin and confirm
            speak("Opening the bin.")

        elif "close" in query:
            # Code to close the bin and confirm
            speak("Closing the bin.")

        else:
            speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
