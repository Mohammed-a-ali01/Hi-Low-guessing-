low = 1
high = 1000

print("Please think of a number between {} and {}".format(low,high))
guesses = 1

while low != high:
    print("\tGuessing in the range of {} to {}".format(low,high))
    guess = low + (high-low) //2
    high_low = input("\nMy guess is {}. Should I guess higher or lower? "
                     "enter h or l or c if my guess if correct"
                     .format(guess)).casefold()
    if high_low =="h":
        low = guess + 1
    elif high_low =="l":
        high = guess - 1
    elif high_low =="c":
        print("I got the correct answer in {} guesses".format(guesses))
        break
    else:
        print("please enter h,l or c ")
    guesses +=1
else:
    print("You thought of the number {}".format(low))
    print(" I got it in {} guesses".format(guesses))