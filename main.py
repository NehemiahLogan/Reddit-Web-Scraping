import random

def generate_response(user_input):
  responses = [
    "How has your day been?",
    "You don't say!",
    "Very cool!",
    "Programming is fun!",
    "Ok Bye!"
  ]
  return random.choice(responses)

def init_chat():
  quit_character = 'q'

  user_input = input("Hello, how are you?\n")

  while user_input != quit_character:
    user_input = input(generate_response(user_input) + "\n")

if __name__ == "__main__":
  init_chat()