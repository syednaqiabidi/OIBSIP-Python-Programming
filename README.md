# OIBSIP-Python-Programming
Python Mini Projects

A collection of three small Python desktop and command-line programs: a voice assistant, a BMI calculator, and a password generator. Each project is self-contained and can be run on its own.

Contents
Jarvis Voice Assistant
BMI Calculator
Password Generator
Project Structure
License
Jarvis Voice Assistant

A simple desktop voice assistant built with Python and Tkinter. Click a button, speak a command, and Jarvis responds out loud and in a chat window. It can tell the time and date, open Google or YouTube, run Google searches, and hold a basic conversation.

Features
Graphical interface with a status label, a chat log, and Start/Stop buttons
Speech-to-text using Google's Web Speech API through SpeechRecognition
Text-to-speech responses using pyttsx3 (works offline once installed)
Built-in commands for greetings, time, date, web browsing, and searching
Listening runs in a background thread so the window stays responsive
Requirements
Python 3.8 or newer
A working microphone
An internet connection (speech recognition uses Google's online service)
Python packages
bash
pip install SpeechRecognition sounddevice pyttsx3 numpy

numpy is needed because sounddevice returns audio as NumPy arrays. Tkinter ships with most Python installers. On some Linux distributions you may need to install it separately, for example with sudo apt install python3-tk.

System dependencies
sounddevice requires the PortAudio library. It is bundled on Windows and macOS. On Linux, install it with sudo apt install libportaudio2.
pyttsx3 uses the platform's speech engine: SAPI5 on Windows, NSSpeechSynthesizer on macOS, and eSpeak on Linux (sudo apt install espeak).
Installation
Clone or download this project.
Install the requirements listed above.
Run the script:
bash
python Voice_Assistance.py
Usage
Launch the program. The window shows "Assistant is Ready."
Click START LISTENING. Jarvis greets you and begins listening.
Speak a command. Each listening session records for 5 seconds, then processes what it heard.
Jarvis writes the command and its response in the chat box and reads the response aloud.
Click STOP ASSISTANT to stop listening, or say "stop" or "exit."
Voice Commands
Say something like	What Jarvis does
"Hello"	Greets you
"What is your name"	Introduces itself
"What time is it" / any phrase containing "time"	Reads the current time
"What is the date" / any phrase containing "date"	Reads today's date
"Open Google"	Opens google.com in your default browser
"Open YouTube"	Opens youtube.com in your default browser
"Search python decorators"	Opens a Google search for the query
"Stop" or "Exit"	Says goodbye and stops the assistant

Anything else gets the reply "Sorry, I don't understand this command."

How It Works
start_assistant() sets the running flag, speaks a greeting, and starts a background thread running listen().
listen() records 5 seconds of audio from the default microphone at 16 kHz, then sends it to Google's speech recognition service.
The recognized text is passed to process_command(), which matches keywords and picks a response.
The response is shown in the chat box and spoken with pyttsx3.
stop_assistant() clears the running flag, which ends the listening loop.
Configuration

You can change these values near the top of Voice_Assistance.py:

Speech rate: engine.setProperty("rate", 170). Higher values speak faster.
Recording length: int(5 * 16000). The first number is the number of seconds to record.
Sample rate: 16000 appears in several places. Keep it consistent if you change it.
Window size and colors: set in the root.geometry and widget definitions at the bottom of the file.
Adding New Commands

Add an elif branch to process_command():

python
elif "weather" in command:
    response = "I can't check the weather yet."

Place it before the final else branch. Because matching uses simple substring checks, put more specific phrases before more general ones.

Known Limitations
Each listening session is a fixed 5 seconds, so long commands get cut off.
Keyword matching is simple substring search. For example, "time" also matches "sometime," and "stop" matches "stopwatch."
Speech recognition needs internet access. Without it, the assistant reports "Internet connection problem."
The greeting is spoken on the main thread, so the window may pause briefly when you click Start.
The assistant does not remember previous commands.
Troubleshooting
"Error" appears right after starting: Check that your microphone is set as the default input device and that sounddevice can see it (python -m sounddevice lists devices).
No voice output: Make sure pyttsx3 has a working speech engine on your system. On Linux, install eSpeak.
"Internet connection problem": Check your connection. Google's speech service must be reachable.
"I could not understand": Speak clearly, reduce background noise, and try again.
BMI Calculator

A simple command-line Python program that calculates a person's Body Mass Index (BMI) from their weight and height, and tells them which BMI category they fall into.

Features
Calculates BMI using the standard formula: weight (kg) divided by height (m) squared
Rounds the result to two decimal places
Classifies the result into one of four categories: Underweight, Normal weight, Overweight, or Obesity
Handles non-numeric input gracefully with an error message
Requirements
Python 3.6 or higher (uses f-strings)
No external libraries required
Installation
Download or clone this repository.
Make sure Python is installed. You can check with:
bash
   python --version
Usage

Run the script from the terminal:

bash
python BMI.py

You will be prompted to enter your weight and height:

Welcome to the BMI Calculator!

Enter your weight in kg: 70
Enter your height in meters: 1.75
Your BMI is: 22.86. Category: Normal weight.

If you enter something that is not a number, the program displays:

Invalid input! Please enter numbers only.
How It Works

The script contains two functions and a main section.

calculate_bmi(weight, height)

Takes the weight in kilograms and the height in meters, computes the BMI, and returns it rounded to two decimal places.

BMI = weight / height²
check_bmi_category(bmi)

Takes a BMI value and returns a string describing the category:

BMI Range	Category
Below 18.5	Underweight
18.5 to below 24.9	Normal weight
25 to below 29.9	Overweight
29.9 and above	Obesity
Main Section

The main section prints a welcome message, reads the weight and height from the user, calculates the BMI and category, and prints the result. All input and calculation is wrapped in a try block so that a ValueError (caused by non-numeric input) is caught and a friendly error message is shown.

Known Issues
Gap in category ranges: The category check uses 18.5 <= bmi < 24.9 for Normal weight and 25 <= bmi < 29.9 for Overweight, so BMI values from 24.9 up to (but not including) 25 do not match either condition and are labeled "Obesity". The Normal weight upper bound and the Overweight lower bound should be the same value (for example, < 25).
Zero height: Entering a height of 0 causes a ZeroDivisionError, which is not caught by the current try block, so the program will crash.
Possible Improvements
Fix the category boundary gap and handle zero or negative values for height and weight.
Wrap the program in an if __name__ == "__main__": block so the functions can be imported into other programs without running the prompts.
Add unit tests for calculate_bmi and check_bmi_category.
Disclaimer

This tool is for general informational purposes only and is not a substitute for professional medical advice. BMI does not account for factors such as muscle mass, bone density, or body composition.

Password Generator

A simple desktop password generator built with Python and Tkinter. Pick a password length, choose whether to include numbers and symbols, and generate a random password that you can copy to your clipboard with one click.

Features
Adjustable password length from 4 to 32 characters (default: 12)
Optional numbers (0-9) and symbols (!@#$% and other punctuation)
Letters (both upper and lower case) are always included
One-click copy to clipboard
Simple graphical interface with no external dependencies
Requirements
Python 3.6 or newer
Tkinter (included with most Python installers)

On some Linux distributions, Tkinter is not installed by default. You can add it with:

bash
# Debian / Ubuntu
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter
Installation

No installation is needed. Download or clone the script and keep it in any folder.

Usage

Run the script from a terminal:

bash
python Random_Password_Genarator.py

Or on some systems:

bash
python3 Random_Password_Genarator.py

Then:

Use the slider to set the password length.
Tick or untick Include Symbols and Include Numbers.
Click Generate Password. The result appears in the text box.
Click Copy Password to copy it to your clipboard. A confirmation message appears below the buttons.
How It Works
generate_password() reads the slider and checkbox values, builds a pool of allowed characters, and picks one at random for each position in the password.
copy_password() copies the password in the text box to the system clipboard.
The interface is built with tkinter: a title, a length slider, two checkboxes, a read-only-style entry box, and two action buttons.
Security Note

This script uses Python's random module, which is fine for everyday use and learning, but it is not designed for cryptographic security. For passwords that protect sensitive accounts, consider replacing random.choice with secrets.choice from Python's standard secrets module. That change is a single-line edit in generate_password().

Also be aware that generated passwords remain in the clipboard until you copy something else, so clear your clipboard after use on shared computers.

Project Structure
.
├── Voice_Assistance.py            # Jarvis Voice Assistant
├── BMI.py                         # BMI Calculator
├── Random_Password_Genarator.py   # Password Generator
└── README.md                      # This file
