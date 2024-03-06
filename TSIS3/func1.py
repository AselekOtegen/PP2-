#1
def grams_to_ounces(grams):
    return grams * 28.3495231
#2
def fahrenheit_to_centigrade(F):
    return (5 / 9) * (F - 32)

F = float(input("Enter temperature in [F]: "))
C = fahrenheit_to_centigrade(F)
print(f"Temperature in [C]: {C}")
#3
def solve(numheads, numlegs):
    rabbits = numlegs // 2 - numheads 
    chikens = numheads - rabbits
    return (chikens, rabbits)

print(solve(35, 94))
#4
def prime(num):
    if num == 1:
        return False
    for d in range(2, num):
        if num % d == 0:
            return False
    return True

def filter_prime(nums): 
    return [num for num in nums if prime(num)] 

nums = map(int, input("Enter numbers: ").split(' '))
print(filter_prime(nums))
#5
from itertools import permutations

def all_permutations(s):
    for perm in permutations(s):
        print(''.join(perm))

s = input("Enter string: ")
all_permutations(s)
#6
def reverse():
    words = input().split(' ')
    words.reverse()
    print(' '.join(words))

reverse()
#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i:i+2] == [3, 3]:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
#8
def spy_game(nums):
    pat = [0, 0, 7]
    pos = 0

    for num in nums:
        if pos >= len(pat):
            break
        if num == pat[pos]:
            pos += 1

    return pos == len(pat)

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
#9
import math

def volume(r):
    return (4 / 3) * math.pi * r ** 3
#10
def unique(lst):
    res = []
    for el in lst:
        if res.count(el) == 0:
            res.append(el)
    return res

print(unique([1, 2, 1, 3, 2, 2]))
#11
def is_palindrom(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return False
    return True

print(is_palindrom("madam"))
print(is_palindrom("chair"))
print(is_palindrom("cabbac"))
#12
def histogram(widths):
    for width in widths:
        print("*" * width)

histogram([4, 9, 7])
#13
import random

name = input("Hello! What is your name?\n")

ans = random.randint(1, 20);
print(f"Well, {name}, I am thinking of a number between 1 and 20.")

guess = int(input("Take a guess.\n"))
attempts = 1

while guess != ans:
    if guess < ans:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    
    guess = int(input("Take a guess.\n"))
    attempts += 1
else:
    print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
#14
from exercise1 import grams_to_ounces
from exercise2 import fahrenheit_to_centigrade
from exercise7 import has_33

print(grams_to_ounces(33))
print(fahrenheit_to_centigrade(96))
print(has_33([3, 3, 3]))