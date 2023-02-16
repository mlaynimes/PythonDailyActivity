guess = "lion"
out_of_guesses = False
guess_count = 0
guess_limit = 3
guess_user = ""

while guess_user != guess and not(out_of_guesses):
    if(guess_count < guess_limit):
        guess_user = input("Enter secrete code: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You out of guesses...! YOU LOSE")
else:
    print("You Won!!")
