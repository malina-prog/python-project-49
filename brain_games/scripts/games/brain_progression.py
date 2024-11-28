from random import randint
from brain_games.scripts.games.engine import welcome, print_question
from brain_games.scripts.games.engine import comparison, congratulation


def progression():
    a = randint(1, 70)
    b = randint(1, 6)
    c = []
    for i in range(10):
        c.append(a)
        a += b
    d = randint(0, 9)
    e = str(c[d])
    c[d] = '..'
    return c, e


def main():
    game_quest = 'What number is missing in the progression?'
    name = welcome(game_quest)
    count = 0
    while count != 3:
        question, answer = progression()
        q = str(' '.join(str(x) for x in question))
        print_question(f'Question: {q}')
        count += comparison(answer, name)
    congratulation(name)


if __name__ == '__main__':
    main()
