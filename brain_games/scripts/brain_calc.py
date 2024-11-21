from random import randint
import prompt
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    count = 0
    while count != 3:
        a = randint(1, 100)
        b = randint(1, 100)
        c = randint(1, 3)
        if c == 1:
            print(f'Question: {a} + {b}')
            answer = str(a + b)
            person_answer = prompt.string('Your answer: ')
            count += test(answer, person_answer)
        elif c == 2:
            print(f'Question: {a} - {b}')
            answer = str(a - b)
            person_answer = prompt.string('Your answer: ')
            count += test(answer, person_answer)
        elif c == 3:
            print(f'Question: {a} * {b}')
            answer = str(a * b)
            person_answer = prompt.string('Your answer: ')
            count += test(answer, person_answer)
    print(f'Congratulations, {name}!')


def test(answer, person_answer, name):
    if person_answer == answer:
        print('Correct!')
        return 1
    else:
        print(f"{person_answer} is wrong answer ;(. ", end='')
        print(f'Correct answer was {answer}')
        print(f"Let's try again, {name}!")
        exit()


if __name__ == '__main__':
    main()
