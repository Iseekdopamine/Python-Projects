import random
def guess(x):#the user is guessing the computer generated number 
    random_number=random.randint(1,x)
    guess =0
    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 and {x}."))
        print(guess)
        if guess<random_number:
            print("Try again. Too Low.")
        elif guess>random_number:
            print("Try again. Too high")
    print(f"Yay you have guessed the number {random_number} correctly!!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(
            f'Is {guess} too high (H), too low (L), or correct (C)? '
        ).lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yayy!! The computer guessed your number, {guess}, correctly!")


computer_guess(1000)

    

