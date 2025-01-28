print("Welcome to the car game")
started = False

while True:
    userInput = input()
    userInput = userInput.lower()

    if userInput == 'help':
        print('start - Start Car\nstop - Stop\nCar quit - Quit Game')
    elif userInput == 'start':
        if started:
            print('Car has started')
        else:
            started = True
            print('Starting Car...')
    elif userInput == 'stop':
        if not started:
            print('Car has stopped')
        else:
            started = False
            print('Stopping Car...')

    elif userInput == 'quit':
        print("See you next time")
        break
    else:
        print('Input Invalid, type help to see command list')

