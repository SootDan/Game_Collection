from game_collection import RPS, NumberGuesser

rps = RPS()
rng = NumberGuesser()

# The console needed to start playing a game.
print('Hello, welcome to my game collection!')
print('It is a collection of random coding exercises to train myself to become better at it.')
print('The current games are RPS and Number Guesser.')

user_choice = ' '
while user_choice != 'e':
    user_choice = input('What would you like to play?\n').lower()
    if user_choice == 'rps': rps.game()
    if user_choice == 'rng': rng.game()

print('Thank you for trying it out! More games, features, and UI will come soon.')