import vosk
import pyttsx3
import pyaudio
import serial
import firebase_admin
from firebase_admin import storage
import json
from time import sleep

# Initialize Firebase
cred = credentials.Certificate("vehicle-type-recognition-sys-firebase-adminsdk-kid7m-35c0a64ce8.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': "vehicle-type-recognition-sys.appspot.com"
})
bucket = storage.bucket()

# Initialize the Vosk model
model_path = "voice_commands/vosk-model-en-in-0.5"
vosk.SetLogLevel(-1)
model = vosk.Model(model_path)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize serial communication with Arduino
ser = serial.Serial('COM10', 9600)  # Change 'COM3' to the correct port for your Arduino

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
        response = "Opening the bin."
    elif "shut" in query:
        ser.write(b'c')  # Send 'c' command to Arduino to close the bin
        sleep(2)  # Wait for the servo to rotate
        response = "Closing the bin."
    elif "level" in query:
        # Request status from Arduino for wet waste bin
        ser.write(b's')  # Send 's' command to Arduino to request status
        sleep(2)  # Wait for Arduino to respond
        # Read status from Arduino for wet waste bin
        status_wet = ser.readline().decode().strip()
        
        # Request status from Arduino for dry waste bin
        ser.write(b's')  # Send 's' command to Arduino to request status
        sleep(2)  # Wait for Arduino to respond
        # Read status from Arduino for dry waste bin
        status_dry = ser.readline().decode().strip()
        
        response = f"Wet waste bin status: {status_wet}, Dry waste bin status: {status_dry}"
    elif query.strip() == "":
        response = ""  # Return nothing if query is empty
    else:
        response = "Sorry, I didn't understand that."  # Return message for unrecognized speech

    # Write response to Firebase Storage
    blob = bucket.blob('responses/response.txt')
    blob.upload_from_string(response)

    # Write response to local text file
    with open('response.txt', 'w') as f:
        f.write(response)

    return response


def main():
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        query = listen().lower()
        response = process_query(query)
        speak(response)

if __name__ == "__main__":
    main()
