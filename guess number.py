import random
r = random.randint(1, 100)
count = 0
while True:
    count += 1
    ans = int(input('Please guess the number from 1 to 100.: '))
    if r == ans:
        print('Your guess is correct.')
        if count < 2:
            print('You use', count, 'time.')
        else:
            print('You use', count, 'times.')
        break
    elif r > ans:
        print('Your guess is smaller than the answer.')
    elif r < ans:
        print('Your guess is larger than the answer.')
    if count < 2:
        print('You use', count, 'time.')
    else:
        print('You use', count, 'times.')