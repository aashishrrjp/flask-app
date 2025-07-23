from flask import Flask
import random

app = Flask(__name__)

# Initialize game state
secret_number = random.randint(1, 100)
guess_count = 0

@app.route('/')
def home():
    return (
        "<h1>🎯 Welcome to Guess the Number!</h1>"
        "<p>I’m thinking of a number between <strong>1 and 100</strong>.</p>"
        "<p>🎮 Try guessing by going to: <code>/guess/&lt;your-number&gt;</code></p>"
        "<p>🔄 You can reset the game using <code>/reset</code></p>"
        "<p>📊 View attempts with <code>/status</code></p>"
    )

@app.route('/guess/<int:number>')
def guess(number):
    global secret_number, guess_count
    guess_count += 1

    if number < secret_number:
        return f"🔻 Too low! Try something higher than {number}. Total guesses: {guess_count}"
    elif number > secret_number:
        return f"🔺 Too high! Try something lower than {number}. Total guesses: {guess_count}"
    else:
        msg = (
            f"🎉 Correct! {number} was the number! "
            f"You guessed it in {guess_count} attempts! "
            "Starting a new game.. 🔄"
        )
        # Reset game
        secret_number = random.randint(1, 100)
        guess_count = 0
        return msg

@app.route('/reset')
def reset():
    global secret_number, guess_count
    secret_number = random.randint(1, 100)
    guess_count = 0
    return "🔄 Game has been reset now! I'm thinking of a new number between 1 and 100."

@app.route('/status')
def status():
    return f"📊 You have made {guess_count} guess(es) so far."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
