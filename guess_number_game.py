import random

def guessgame(a, b, actual1):
    guess = int(input("fguess a number between {a} and {b}"))
    nguess = 1
    while guess != actual1:
        if guess < actual1:
            guess = int(input("Enter a bigger guess : \n"))
            nguess += 1
        else:
            guess = int(input("Enter a smaller guess : \n"))
            nguess += 1
    print(f"You guessed the number in {nguess} guesses \n")
    return guess

if __name__ == '__main__':
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    actual1 = random.randint(a, b)
    print("player_1's turn \n")
    g1 = guessgame(a, b, actual1)
    print("player_2's turn \n")
    actual2 = random.randint(a, b)
    g2 = guessgame(a, b, actual2)

    if g1 < g2:
        print("player_1 won the match \n")
    elif g2 < g1:
        print("player_2 won the match \n")
    else:
        print("Match tie\n")
    print(f"The guesses for player_1 was {actual1} and for player_2 was {actual2}")
