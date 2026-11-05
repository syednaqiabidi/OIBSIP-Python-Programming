# Jarvis Voice Assistant

A simple desktop voice assistant built with Python and Tkinter. Click a button, speak a command, and Jarvis responds out loud and in a chat window. It can tell the time and date, open Google or YouTube, run Google searches, and hold a basic conversation.

## Features

- Graphical interface with a status label, a chat log, and Start/Stop buttons
- Speech-to-text using Google's Web Speech API through `SpeechRecognition`
- Text-to-speech responses using `pyttsx3` (works offline once installed)
- Built-in commands for greetings, time, date, web browsing, and searching
- Listening runs in a background thread so the window stays responsive

## Requirements

- Python 3.8 or newer
- A working microphone
- An internet connection (speech recognition uses Google's online service)

### Python packages

```bash
pip install SpeechRecognition sounddevice pyttsx3 numpy
```

`numpy` is needed because `sounddevice` returns audio as NumPy arrays. Tkinter ships with most Python installers. On some Linux distributions you may need to install it separately, for example with `sudo apt install python3-tk`.

### System dependencies

- **sounddevice** requires the PortAudio library. It is bundled on Windows and macOS. On Linux, install it with `sudo apt install libportaudio2`.
- **pyttsx3** uses the platform's speech engine: SAPI5 on Windows, NSSpeechSynthesizer on macOS, and eSpeak on Linux (`sudo apt install espeak`).

## Installation

1. Clone or download this project.
2. Install the requirements listed above.
3. Run the script:

```bash
python Voice_Assistance.py
```

## Usage

1. Launch the program. The window shows "Assistant is Ready."
2. Click **START LISTENING**. Jarvis greets you and begins listening.
3. Speak a command. Each listening session records for 5 seconds, then processes what it heard.
4. Jarvis writes the command and its response in the chat box and reads the response aloud.
5. Click **STOP ASSISTANT** to stop listening, or say "stop" or "exit."

## Voice Commands

| Say something like | What Jarvis does |
|---|---|
| "Hello" | Greets you |
| "What is your name" | Introduces itself |
| "What time is it" / any phrase containing "time" | Reads the current time |
| "What is the date" / any phrase containing "date" | Reads today's date |
| "Open Google" | Opens google.com in your default browser |
| "Open YouTube" | Opens youtube.com in your default browser |
| "Search python decorators" | Opens a Google search for the query |
| "Stop" or "Exit" | Says goodbye and stops the assistant |

Anything else gets the reply "Sorry, I don't understand this command."

## How It Works

1. `start_assistant()` sets the running flag, speaks a greeting, and starts a background thread running `listen()`.
2. `listen()` records 5 seconds of audio from the default microphone at 16 kHz, then sends it to Google's speech recognition service.
3. The recognized text is passed to `process_command()`, which matches keywords and picks a response.
4. The response is shown in the chat box and spoken with `pyttsx3`.
5. `stop_assistant()` clears the running flag, which ends the listening loop.

## Configuration

You can change these values near the top of `Voice_Assistance.py`:

- **Speech rate:** `engine.setProperty("rate", 170)`. Higher values speak faster.
- **Recording length:** `int(5 * 16000)`. The first number is the number of seconds to record.
- **Sample rate:** `16000` appears in several places. Keep it consistent if you change it.
- **Window size and colors:** set in the `root.geometry` and widget definitions at the bottom of the file.

## Adding New Commands

Add an `elif` branch to `process_command()`:

```python
elif "weather" in command:
    response = "I can't check the weather yet."
```

Place it before the final `else` branch. Because matching uses simple substring checks, put more specific phrases before more general ones.

## Known Limitations

- Each listening session is a fixed 5 seconds, so long commands get cut off.
- Keyword matching is simple substring search. For example, "time" also matches "sometime," and "stop" matches "stopwatch."
- Speech recognition needs internet access. Without it, the assistant reports "Internet connection problem."
- The greeting is spoken on the main thread, so the window may pause briefly when you click Start.
- The assistant does not remember previous commands.

## Troubleshooting

- **"Error" appears right after starting:** Check that your microphone is set as the default input device and that `sounddevice` can see it (`python -m sounddevice` lists devices).
- **No voice output:** Make sure `pyttsx3` has a working speech engine on your system. On Linux, install eSpeak.
- **"Internet connection problem":** Check your connection. Google's speech service must be reachable.
- **"I could not understand":** Speak clearly, reduce background noise, and try again.

## Project Structure

```
.
├── Voice_Assistance.py   # Main application
└── README.md             # This file
```

## License

Add your license here.
