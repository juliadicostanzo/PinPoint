# PinPoint

PinPoint is a responsive web-based PIN guessing game built with Python, Flask, Bootstrap, HTML, and CSS. The application generates a random four-digit PIN and gives users feedback after each guess.

## Features

- Generates a random four-digit PIN
- Validates guesses before processing them
- Counts correct digits while handling repeated numbers
- Identifies digits in the correct position
- Tracks the number of attempts
- Displays previous guesses and their results
- Stores game progress using Flask sessions
- Allows users to restart the game
- Uses Bootstrap for responsive desktop and mobile layouts

## Technologies

- Python
- Flask
- Bootstrap 5
- HTML5
- CSS3
- Jinja templates
- Flask sessions

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/juliadicostanzo/PinPoint.git
cd PinPoint
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 4. Install the dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python3 app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

## How to Play

1. Enter a four-digit number.
2. Select **Check PIN**.
3. Review how many digits are correct and how many are in the correct position.
4. Use the guess history to determine the PIN.
5. Continue until you crack the code.

Select **Start over** at any time to generate a new PIN and clear the current game.

## Project Structure

```text
PinPoint/
├── app.py
├── requirements.txt
├── README.md
├── documentation.md
├── static/
│   └── styles.css
└── templates/
    └── index.html
```

## Future Improvements

- Difficulty levels with different PIN lengths
- Game statistics and best scores
- Maximum attempt limits
- An online leaderboard
- Public deployment
