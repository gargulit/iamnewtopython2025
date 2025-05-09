import random

print("Welcome to the Future Teller!")
name = input("What is your name? ")

questions = [
    "What do you want to know about your future?",
    "Ask me any yes/no question:"
]

print(random.choice(questions))
input("> ")  # we don't care about the question, just wait for input

answers = [
    "Yes, definitely!",
    "No way!",
    "Maybe... time will tell.",
    "I don't think so.",
    "Absolutely!",
    "Better not say now.",
    "Ask again later.",
    "It's unclear. Try again."
]

print(f"{name}, here is your answer:")
print(random.choice(answers))
