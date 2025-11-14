from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define snakes and ladders
snakes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

# AI messages
messages = [
    "You're climbing fast... but I see your weakness!",
    "Pathetic move, human. Watch this!",
    "I'm the king of this jungle. Bow down!",
    "Your strategy is as predictable as a snake's strike.",
    "I'll crush you like a vine under my foot!",
    "Nice try, but I'm always one step ahead.",
    "The jungle favors the strong. And that's me!",
    "You're just a pawn in my game.",
    "Feel the burn as I ascend!",
    "Game over for you, soon enough."
]

def get_final_position(pos):
    if pos in ladders:
        return ladders[pos]
    elif pos in snakes:
        return snakes[pos]
    return pos

def ai_choose_roll(player_pos, ai_pos):
    best_roll = 1
    best_score = -1000
    for roll in range(1, 7):
        new_pos = ai_pos + roll
        if new_pos > 100:
            continue
        final_pos = get_final_position(new_pos)
        score = final_pos
        if new_pos in ladders:
            score += 20  # bonus for ladder
        elif new_pos in snakes:
            score -= 15  # penalty for snake
        score += random.randint(-5, 5)  # randomness
        if score > best_score:
            best_score = score
            best_roll = roll
    return best_roll

@app.route('/ai_decision', methods=['GET'])
def ai_decision():
    player_pos = int(request.args.get('playerPos', 0))
    ai_pos = int(request.args.get('aiPos', 0))
    # Simulate thinking
    time.sleep(random.uniform(0.5, 2.0))
    roll = ai_choose_roll(player_pos, ai_pos)
    message = random.choice(messages)
    return jsonify({'roll': roll, 'message': message})

if __name__ == '__main__':
    app.run(debug=True)
