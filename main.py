from game_collection import RPS, NumberGuesser, PigDice

rps = RPS()
rng = NumberGuesser()
pig = PigDice()

# The console needed to start playing a game.
print('Hello, welcome to my game collection!')
print('It is a collection of random coding exercises to train myself to become better at it.')
print('The current games are RPS, Number Guesser, and Pig Dice.')

user_choice = ' '
while user_choice != 'e':
    user_choice = input('What would you like to play?\n').lower()
    if user_choice == 'rps': rps.game()
    if user_choice == 'rng': rng.game()
    if user_choice == 'pig': pig.game()

print('Thank you for trying it out! More games, features, and UI will come soon.')