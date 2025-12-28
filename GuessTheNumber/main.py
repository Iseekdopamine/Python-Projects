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

