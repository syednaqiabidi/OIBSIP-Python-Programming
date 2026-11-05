# BMI Calculator

A simple command-line Python program that calculates a person's Body Mass Index (BMI) from their weight and height, and tells them which BMI category they fall into.

## Features

- Calculates BMI using the standard formula: weight (kg) divided by height (m) squared
- Rounds the result to two decimal places
- Classifies the result into one of four categories: Underweight, Normal weight, Overweight, or Obesity
- Handles non-numeric input gracefully with an error message

## Requirements

- Python 3.6 or higher (uses f-strings)
- No external libraries required

## Installation

1. Download or clone this repository.
2. Make sure Python is installed. You can check with:

   ```bash
   python --version
   ```

## Usage

Run the script from the terminal:

```bash
python BMI.py
```

You will be prompted to enter your weight and height:

```
Welcome to the BMI Calculator!

Enter your weight in kg: 70
Enter your height in meters: 1.75
Your BMI is: 22.86. Category: Normal weight.
```

If you enter something that is not a number, the program displays:

```
Invalid input! Please enter numbers only.
```

## How It Works

The script contains two functions and a main section:

### `calculate_bmi(weight, height)`

Takes the weight in kilograms and the height in meters, computes the BMI, and returns it rounded to two decimal places.

```
BMI = weight / height²
```

### `check_bmi_category(bmi)`

Takes a BMI value and returns a string describing the category:

| BMI Range            | Category       |
|----------------------|----------------|
| Below 18.5           | Underweight    |
| 18.5 to below 24.9   | Normal weight  |
| 25 to below 29.9     | Overweight     |
| 29.9 and above       | Obesity        |

### Main Section

The main section prints a welcome message, reads the weight and height from the user, calculates the BMI and category, and prints the result. All input and calculation is wrapped in a `try` block so that a `ValueError` (caused by non-numeric input) is caught and a friendly error message is shown.

## Known Issues

- **Gap in category ranges:** The category check uses `18.5 <= bmi < 24.9` for Normal weight and `25 <= bmi < 29.9` for Overweight, so BMI values from 24.9 up to (but not including) 25 do not match either condition and are labeled "Obesity". The Normal weight upper bound and the Overweight lower bound should be the same value (for example, `< 25`).
- **Zero height:** Entering a height of `0` causes a `ZeroDivisionError`, which is not caught by the current `try` block, so the program will crash.

## Possible Improvements

- Fix the category boundary gap and handle zero or negative values for height and weight.
- Wrap the program in an `if __name__ == "__main__":` block so the functions can be imported into other programs without running the prompts.
- Add unit tests for `calculate_bmi` and `check_bmi_category`.

## Disclaimer

This tool is for general informational purposes only and is not a substitute for professional medical advice. BMI does not account for factors such as muscle mass, bone density, or body composition.

## License

Add your preferred license here.
