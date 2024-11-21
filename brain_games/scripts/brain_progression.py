from random import randint
import prompt
from brain_games.cli import welcome_user


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
    name = welcome_user()
    print('What number is missing in the progression?')
    count = 0
    while count != 3:
        question, answer = progression()
        print('Question: ', end='')
        print(*question, sep=' ')
        person_answer = prompt.string('Your answer: ')
        if person_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f"{person_answer} is wrong answer ;(. ", end='')
            print(f'Correct answer was {answer}')
            print(f"Let's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
