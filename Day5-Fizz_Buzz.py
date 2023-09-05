fizz = "Fizz"
buzz = "Buzz"
fb = "FizzBuzz"

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0: # Divisible by 3 & 5; 
        print(fb) # this has to go first because it cannot be skipped at all (overlap) - 15 would be read by 3 or 5 and not be read as 3 AND 5
    elif number % 3 == 0: # Divisible by 3 
        print(fizz)
    elif number % 5 == 0: # Divisible by 5
        print(buzz)
    else:
        print(number)
# elif statements make the number get replaced
