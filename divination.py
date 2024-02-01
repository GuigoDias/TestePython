import random;


def play_Divination():
    print("*********************************");
    print("** Welcome to Divination Game ***");
    print("*********************************");

    secretNumber = random.randrange(1,101);
    totalAttempts = 0;
    points = 1000;

    print("(1) Easy (2) Medium (3) Hard");
    level = int(input("Choose difficult: "));
    if (level == 1):
        totalAttempts = 20;
    elif (level == 2):
        totalAttempts = 10;
    else:
        totalAttempts = 5;

    for currentAttempt in range(1 , totalAttempts + 1):
        print("Attempt {} of {}".format(str(currentAttempt), str(totalAttempts)))
        guess = input("enter a number from 1 to 100:\n");
        print("You tried: " + guess);
        guessNumber = int(guess);

        if(guessNumber < 1 or guessNumber > 100):
            print("Invalid number, please enter a number from 1 to 100\n");
            continue;

        rightAnswer = secretNumber == guessNumber;
        bigger = guessNumber > secretNumber;
        smaller = guessNumber < secretNumber;

        if(rightAnswer):
            print("You got it and win {} points!".format(points));
            break;
        else:
            if(bigger):
                print("You missed! Your number is bigger than the secret number!");
            elif(smaller):
                print("You missed! Your number is smaller than the secret number!");
            lostPoints = abs(secretNumber - guessNumber);
            points = abs(points - lostPoints);
            if(currentAttempt == totalAttempts):
                print("the secret number is {} and you win {} points.".format(secretNumber,points));

    print("GAME OVER!");