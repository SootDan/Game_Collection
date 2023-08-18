import random

class RPS():
    # Rock Paper Scissors: The Game!
    def __init__(self):
        self.stats = {'win': 0, 'tie': 0, 'loss': 0}
        self.dict_shapes = {'R': 0, 'P': 1, 'S': 2}
        self.list_shapes = ['Rock', 'Paper', 'Scissors']

    def game_calc(self, index_user, index_ai):
        # Calculates the outcome of the game. [0] beats [2], [1] beats [0], [2] beats [1]
        win_index = (index_user == 0 and index_ai == 2) or (index_user == 1 and index_ai == 0) or (index_user == 2 and index_ai == 1)
        
        if win_index:
            return f'{self.outcome_msg("win", 0, index_user, index_ai)}'
        elif index_user == index_ai:
            return f'{self.outcome_msg("tie", 1, index_user, index_ai)}'
        else:
            return f'{self.outcome_msg("loss", 2, index_user, index_ai)}'
    
    def outcome_msg(self, outcome, index, index_user, index_ai):
        # Calculates the outcome message.
        outcomes = ['beats', 'ties with', 'is beaten by']
        str_outcome = ['won', 'tied', 'lost']
        self.stats[outcome] += 1
        return_string = f'{self.list_shapes[index_user]} {outcomes[index]} {self.list_shapes[index_ai]}. You {str_outcome[index]}! '

        if self.stats['win'] != 0:
            win_rate = round((self.stats["win"] / sum(self.stats.values()) * 100), 2)
            return_string += f'Your win rate is {win_rate}%.'

        return return_string

    def game(self):
        # Interactions with the user.
        user_motive = ' '
        while user_motive[0].upper() != 'E':
            # Only checks for the first letter and makes it uppercase.
            user_motive = input('Choose: Rock, Paper, or Scissors or Exit?\n')

            try:
                index_user = self.dict_shapes[user_motive[0].upper()]
                index_ai = random.randint(0, 2)
                print(self.game_calc(index_user = index_user, index_ai = index_ai))
            except KeyError:
                print('Thanks for playing!')
                self.stats = {'win': 0, 'tie': 0, 'loss': 0}


class NumberGuesser():
    # Guessing numbers between 1 and 15!
    def __init__(self):
        self.ai_output = random.randint(1, 15)
        self.try_count = 0
        self.user_input = 0
        self.string_comparison = ['smaller', 'bigger', 'almost the same']
    
    def tries(self, comparison):
        # [0] < ai; [1] > ai; [2] +-1 ai
        self.try_count += 1
        print(f'Your current tries are {self.try_count}.')
        print(f'The number {self.user_input} is {self.string_comparison[comparison]} than the AI\'s number.')

    def game(self):
        while self.ai_output != self.user_input:
            self.user_input= int(input('Guess a number between 1 and 15.\n'))
            diff = abs(self.user_input - self.ai_output)
            comparison  = 2 if diff == 1 else (1 if self.user_input > self.ai_output else 0)
            self.tries(comparison)
        print (f'Thanks for playing! It took you {self.try_count + 1} tries to guess {self.ai_output} correctly.')