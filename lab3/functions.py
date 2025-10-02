# 6. Prime filter with lambda
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

nums = [1, 2, 3, 5, 8, 13, 15]
prime_nums = list(filter(lambda x: is_prime(x), nums))
# print(prime_nums)


# 7. Grams to ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams


# 8. Fahrenheit to Celsius
def fahrenheit_to_celsius(F):
    return (5/9) * (F - 32)


# 9. Chickens and rabbits
def solve(numheads, numlegs):
    for chickens in range(numheads+1):
        rabbits = numheads - chickens
        if 2*chickens + 4*rabbits == numlegs:
            return chickens, rabbits
    return None


# 10. Prime filter
def filter_prime(numbers):
    return [x for x in numbers if is_prime(x)]


# 11. Permutations
from itertools import permutations
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]


# 12. Reverse words
def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])


# 13. Has 33
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] == 3:
            return True
    return False


# 14. Spy game
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False


# 15. Volume of sphere
def sphere_volume(r):
    return (4/3) * math.pi * r**3


# 16. Unique elements
def unique_list(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list


# 17. Palindrome check
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


# 18. Histogram
def histogram(lst):
    for num in lst:
        print('*' * num)


# 19. Guess the number
import random
def guess_game():
    name = input("Hello! What is your name?\n")
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0

    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
