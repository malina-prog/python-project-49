from random import randint
import prompt
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        a = randint(1, 100)
        print(f'Question: {a}')
        if a % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'

        person_answer = prompt.string('Your answer: ')

        if person_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f"{person_answer} is wrong answer ;(. ", end='')
            print(f'Correct answer was {answer}')
            print(f"Let's try again, {name}")
            exit()

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
