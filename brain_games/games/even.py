import random

def b_even():
    print('May I have your name? ', end='') 
    name = input()
    print('Hello', name + '!')
    print("Answer 'yes' if number even otherwise answer 'no'.")
    a = 0
    for i in range(3):
        x = random.randint(1, 100)
        y = ''
        print('Question:', x)
        z = input('Your answer:')
        if x % 2 == 0:
            y = 'yes'
            if y == z:
                print('Correct!')
                a += 1
            elif y != z:
                print(z, "is wrong answer ;(. Correct answer was 'yes'.")
                print("Let's try again,", name + "!")
                break
        elif x % 2 != 0:
            y = 'no'
            if y == z:
                print('Correct!')
                a += 1
            elif y != z:
                print(z, "is wrong answer ;(. Correct answer was 'no'.")
                print("Let's try again,", name + "!")
                break
    if a == 3:
        print('Congratulations', name + '!')
