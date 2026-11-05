# Password Generator

A simple desktop password generator built with Python and Tkinter. Pick a password length, choose whether to include numbers and symbols, and generate a random password that you can copy to your clipboard with one click.

## Features

- Adjustable password length from 4 to 32 characters (default: 12)
- Optional numbers (`0-9`) and symbols (`!@#$%` and other punctuation)
- Letters (both upper and lower case) are always included
- One-click copy to clipboard
- Simple graphical interface with no external dependencies

## Requirements

- Python 3.6 or newer
- Tkinter (included with most Python installers)

On some Linux distributions, Tkinter is not installed by default. You can add it with:

```bash
# Debian / Ubuntu
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

## Installation

No installation is needed. Download or clone the script and keep it in any folder.

## Usage

Run the script from a terminal:

```bash
python Random_Password_Genarator.py
```

Or on some systems:

```bash
python3 Random_Password_Genarator.py
```

Then:

1. Use the slider to set the password length.
2. Tick or untick **Include Symbols** and **Include Numbers**.
3. Click **Generate Password**. The result appears in the text box.
4. Click **Copy Password** to copy it to your clipboard. A confirmation message appears below the buttons.

## How It Works

- `generate_password()` reads the slider and checkbox values, builds a pool of allowed characters, and picks one at random for each position in the password.
- `copy_password()` copies the password in the text box to the system clipboard.
- The interface is built with `tkinter`: a title, a length slider, two checkboxes, a read-only-style entry box, and two action buttons.

## Security Note

This script uses Python's `random` module, which is fine for everyday use and learning, but it is not designed for cryptographic security. For passwords that protect sensitive accounts, consider replacing `random.choice` with `secrets.choice` from Python's standard `secrets` module. That change is a single-line edit in `generate_password()`.

Also be aware that generated passwords remain in the clipboard until you copy something else, so clear your clipboard after use on shared computers.

## File Structure

```
Random_Password_Genarator.py   # Main application script
README.md                      # This file
```

## License

Add your preferred license here, or remove this section.
