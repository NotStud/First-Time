print('Hello World')

guess = int(input('Enter a number of trails you want to make: '))
name = input('What is your name: ')
while guess > 0:
    for x in range(guess):
        print('Hello', name)
    
