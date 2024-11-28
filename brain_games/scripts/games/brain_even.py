from random import randint
from brain_games.scripts.games.engine import welcome, print_question
from brain_games.scripts.games.engine import comparison, congratulation


def main():
    game_quest = 'Answer "yes" if the number is even, otherwise answer "no".'
    name = welcome(game_quest)
    count = 0
    while count != 3:
        a = randint(1, 100)
        print_question(f'Question: {a}')
        if a % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'

        count += comparison(answer, name)
    congratulation(name)


if __name__ == '__main__':
    main()
