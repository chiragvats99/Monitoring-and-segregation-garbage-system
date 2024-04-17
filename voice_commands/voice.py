import vosk
import pyttsx3
import pyaudio
import serial
from time import sleep

# Initialize the Vosk model
model_path = "voice_commands/vosk-model-en-in-0.5"
vosk.SetLogLevel(-1)
model = vosk.Model(model_path)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize serial communication with Arduino
ser = serial.Serial('COM3', 9600)  # Change 'COM3' to the correct port for your Arduino

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Listening...")

    frames = []

    for i in range(0, int(RATE / CHUNK * 3)):  # Adjust the duration as needed
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    audio_data = b''.join(frames)

    try:
        print("Recognizing...")
        recognizer = vosk.KaldiRecognizer(model, RATE)
        recognizer.AcceptWaveform(audio_data)

        # Get the final result
        result = json.loads(recognizer.FinalResult())
        query = result["text"]
        print(f"You said: {query}")
        return query
    except Exception as e:
        print(f"Error: {e}")
        return ""

def process_query(query):
    if "open" in query:
        ser.write(b'o')  # Send 'o' command to Arduino to open the bin
        sleep(2)  # Wait for the servo to rotate
        return "Opening the bin."
    elif "close" in query:
        ser.write(b'c')  # Send 'c' command to Arduino to close the bin
        sleep(2)  # Wait for the servo to rotate
        return "Closing the bin."
    else:
        return "I'm sorry, I didn't understand that."

def main():
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        query = listen().lower()
        response = process_query(query)
        speak(response)

if __name__ == "__main__":
    main()
