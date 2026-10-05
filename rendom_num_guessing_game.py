import random 
num = random.randint(1,100)

trails =0

while True:
    guess = int(input("guess the num between 1 to 100="))
    trails += 1
    if guess == num:
        print(f"Congratulations! You guessed the number in {trails} trails.")
        break
    elif guess > num :
        print ("your guess is  to higher")
    elif guess < num:
        print ("your guess is  to lower")
    elif guess < 1 or guess > 100:
        print ("invalid input")
    else:
        print ("invalid input")
    
      

