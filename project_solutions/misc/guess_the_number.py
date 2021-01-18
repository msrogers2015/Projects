import random as r

upper_limit = 0

while True:
    try:
        upper_limit = int(input("Please select an upper limit:"))
    except ValueError:
        print('Please input a numerical value')

    
    if upper_limit != 0:

        hidden_value = r.randint(0, upper_limit)
        upper_limit = 0

        while hidden_value != 0:
            try:
                guess = int(input("Make a guess:"))
            except ValueError:
                print('Please input a numerical value.')
        
            if guess != hidden_value:
                if guess > hidden_value:
                    try:
                        guess = int(input("Too high! Make a guess:"))
                    except ValueError:
                        print('Please input a numerical value.')
                
                if guess < hidden_value:
                    try:
                        guess = int(input("Too low! Make a guess:"))
                    except ValueError:
                        print('Please input a numerical value.')

                if guess == hidden_value:
                    print('Correct!')
                    break
    break
        