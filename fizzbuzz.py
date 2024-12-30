# FizzBuzz 

# Steps to Create FizzBuzz
# 1. Create a function that takes in a number
# 2. Create a loop to iterate through the numbers
# 3. Check if the number is divisible by 3 and 5
# 4. Check if the number is divisible by 3
# 5. Check if the number is divisible by 5
# 6. Print the number or the corresponding word
# 7. Create a stop condition for the loop.


def fizzbuzz():
    number = 0
    while number < 200:
        number += 1
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

def main():
    fizzbuzz()

if __name__ == "__main__":
    main()