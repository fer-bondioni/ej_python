secret_word = "Fer"
guess = ""
guess_total = 0
guess_limit = 3
out_of_guesses = False

while secret_word != guess and not(out_of_guesses):
    if guess_total < guess_limit:
        guess = input("Enter guess: ")
        guess_total = 1 + guess_total
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You lose!")
else:
    print("You win!")
