from random import randint
import prompt
import math
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    count = 0
    while count != 3:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f'Question: {a} {b}')
        answer = str(math.gcd(a, b))
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
