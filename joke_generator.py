import random

def random_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don’t programmers like nature? It has too many bugs.",
        "I would tell you a joke about an elevator, but it's an uplifting experience.",
        "I told my computer I needed a break, and now it won't stop sending me Kit-Kats.",
        "Why do cows wear bells? Because their horns don't work.",
        "I’m reading a book on anti-gravity. It’s impossible to put down.",
        "I used to play piano by ear, but now I use my hands.",
        "What do you get when you cross a snowman and a vampire? Frostbite.",
        "I couldn't figure out how to put my seatbelt on. Then it clicked.",
        "What do you call fake spaghetti? An impasta!",
        "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.",
        "How does a penguin build its house? Igloos it together!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "I don’t trust stairs because they’re always up to something.",
        "Why don't oysters share their pearls? Because they're shellfish."
    ]
    return random.choice(jokes)

print("Here's an infinite stream of jokes for you:")
while True:
    input("Press Enter for a new joke...")  # Waits for user to press Enter
    print(random_joke())  # Print a new joke
