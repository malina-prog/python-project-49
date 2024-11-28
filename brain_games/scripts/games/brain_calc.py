from random import randint
from brain_games.scripts.games.engine import welcome, print_question
from brain_games.scripts.games.engine import comparison, congratulation


def main():
    game_quest = 'What is the result of the expression?'
    name = welcome(game_quest)
    count = 0
    while count != 3:
        a = randint(1, 100)
        b = randint(1, 100)
        c = randint(1, 3)
        if c == 1:
            print_question(f'Question: {a} + {b}')
            answer = str(a + b)
            count += comparison(answer, name)
        elif c == 2:
            print_question(f'Question: {a} - {b}')
            answer = str(a - b)
            count += comparison(answer, name)
        elif c == 3:
            print_question(f'Question: {a} * {b}')
            answer = str(a * b)
            count += comparison(answer, name)
    congratulation(name)


if __name__ == '__main__':
    main()
