import random
import answers


def game():
    while True:
        print('Задавай вопрос:')
        q = input()
        print(random.choice(answers.a))
        print('Хочешь задать ещё вопрос? Введи: да/нет')
        ut = input().lower()
        if ut != 'да':
            print('Возвращайся если возникнут вопросы!')
            break


print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос. Как мне тебя называть?')
name = input()
print(f'Привет, {name}')
game()

