import os
import random

from flask import Flask, request, render_template, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key")


def getPin():
    pinList = []
    while len(pinList) < 4:
        pinList.append(str(random.randint(0, 9)))
    return pinList

def numCorrect(guess, pin):
    count = 0
    temp_pin = pin.copy()
    for g_digit in guess:
        if g_digit in temp_pin:
            temp_pin.remove(g_digit)
            count += 1
    return count

def numInRightPlace(guess, pin):
    count = 0
    i = 0
    while i < 4:
        if guess[i] == pin[i]:
            count += 1
        i += 1
    return count

@app.route("/restart", methods=["POST"])
def restart():
    session.pop("pin", None)
    session.pop("guesses", None)
    session.pop("guess_count", None)
    flash("The pin has reset")
    return redirect(url_for("index"))

@app.route("/", methods=["GET", "POST"])
def index():
    if "pin" not in session:
        session["pin"] = getPin()
    if "guesses" not in session:
        session["guesses"] = []
    if "guess_count" not in session:
        session["guess_count"] = 0
    pin = session["pin"]
    guesses = session["guesses"]
    guess_count = session["guess_count"]

    guess = None
    correct_digits = 0
    right_place = 0
    message = ""
    message_kind = ""
    past_guesses_to_show = guesses.copy()

    if request.method == "POST":
        guess_text = request.form["guess"]
        if len(guess_text) == 4 and guess_text.isdigit():
            guess = list(guess_text)
            correct_digits = numCorrect(guess, pin)
            right_place = numInRightPlace(guess, pin)
            guesses.insert(0,{
                "guess": guess_text,
                "correct_digits": correct_digits,
                "right_place": right_place,
            })
            guess_count +=1
            session["guesses"] = guesses
            session["guess_count"] = guess_count

            past_guesses_to_show = guesses.copy()

            if guess == pin:
                message = f"Congratulations! You guessed the pin: {''.join(pin)} in {guess_count} attempts"
                message_kind = "success"
                session["pin"] = getPin()
                session["guesses"] = []
                session["guess_count"] = 0
            #else:
                #message = f"You entered {guess_text}. {correct_digits} digits correct, {right_place} in the right place."
        else:
            message = "Invalid input! Enter 4 digits."
            message_kind = "error"

    return render_template("index.html", message=message,
        guess="".join(guess) if guess else None,
        correct_digits=correct_digits, 
        right_place=right_place,
        past_guesses=past_guesses_to_show,
        guess_count=guess_count,
        message_kind=message_kind,
    )

if __name__ == "__main__":
    app.run(debug=True)
