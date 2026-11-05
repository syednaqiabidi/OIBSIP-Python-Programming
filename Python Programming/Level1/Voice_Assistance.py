import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import sounddevice as sd
import pyttsx3
import threading
import webbrowser
import datetime
engine = pyttsx3.init()
engine.setProperty("rate", 170)
recognizer = sr.Recognizer()
running = False
def speak(text):
    engine.say(text)
    engine.runAndWait()
def show_message(message):
    chat_box.insert(tk.END, message + "\n")
    chat_box.see(tk.END)
def process_command(command):

    command = command.lower()

    show_message("You: " + command)

    if "hello" in command:
        response = "Hello! How can I help you?"

    elif "your name" in command:
        response = "My name is Jarvis. I am your voice assistant."

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = "The current time is " + current_time

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        response = "Today's date is " + current_date

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        response = "Opening Google"

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube"

    elif "search" in command:
        query = command.replace("search", "", 1).strip()

        if query:
            webbrowser.open(
                "https://www.google.com/search?q=" + query.replace(" ", "+")
            )
            response = "Searching Google for " + query
        else:
            response = "Please tell me what to search."

    elif "stop" in command or "exit" in command:
        response = "Goodbye! Have a nice day."
        show_message("Jarvis: " + response)
        speak(response)
        stop_assistant()
        return

    else:
        response = "Sorry, I don't understand this command."

    show_message("Jarvis: " + response)
    speak(response)
def listen():
    global running

    while running:
        try:
            root.after(0, lambda: status_label.config(text="Listening..."))

            audio = sd.rec(
                int(5 * 16000),
                samplerate=16000,
                channels=1,
                dtype="int16"
            )

            sd.wait()

            audio_data = sr.AudioData(audio.tobytes(), 16000, 2)

            command = recognizer.recognize_google(audio_data)

            process_command(command)

        except sr.UnknownValueError:
            root.after(0, lambda: show_message("I could not understand."))

        except sr.RequestError:
            root.after(0, lambda: show_message("Internet connection problem."))

        except Exception as e:
            error = str(e)
            root.after(0, lambda: show_message("Error: " + error))
            running = False

    root.after(0, lambda: status_label.config(text="Assistant Stopped"))
def start_assistant():

    global running

    if not running:
        running = True

        status_label.config(text="Starting Assistant...")
        speak("Hello! I am Jarvis. How can I help you?")

        threading.Thread(
            target=listen,
            daemon=True
        ).start()
def stop_assistant():

    global running
    running = False
    status_label.config(text="Assistant Stopped")
root = tk.Tk()

root.title("Jarvis Voice Assistant")
root.geometry("600x550")
root.configure(bg="#101820")
heading = tk.Label(
    root,
    text="JARVIS VOICE ASSISTANT",
    font=("Arial", 20, "bold"),
    bg="#101820",
    fg="#00FFFF"
)
heading.pack(pady=20)
status_label = tk.Label(
    root,
    text="Assistant is Ready",
    font=("Arial", 12),
    bg="#101820",
    fg="white"
)
status_label.pack(pady=10)
chat_box = scrolledtext.ScrolledText(
    root,
    width=60,
    height=15,
    font=("Arial", 11),
    bg="#1B2838",
    fg="white"
)
chat_box.pack(padx=20, pady=20)
start_button = tk.Button(
    root,
    text="START LISTENING",
    font=("Arial", 13, "bold"),
    bg="#00AA88",
    fg="white",
    width=20,
    command=start_assistant
)
start_button.pack(pady=10)
stop_button = tk.Button(
    root,
    text="STOP ASSISTANT",
    font=("Arial", 13, "bold"),
    bg="#DD4444",
    fg="white",
    width=20,
    command=stop_assistant
)
stop_button.pack(pady=5)

root.mainloop()
