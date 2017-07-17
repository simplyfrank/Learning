import pandas as pd

def print_words(string):
    """
    Takes a given string, splits in into words and returns them to the screen
    """
    words = string.split(' ')
    for word in words:
        print(word)

# print_words('this is my first string')


def count_to(start, end, step=1):
    last_pos = start
    while last_pos <= end:
        print(last_pos)
        last_pos += step

# print(count_to(25,50,5))

def print_chars(string):
    for char in string:
        print(char)

# print_chars('this is my test string')


def print_vowels(string):
    consonants = ['a','e', 'i', 'o', 'u']
    result = []
    for char in string:
        if char in consonants:
            pass
        else:
            result.append(char)
    print(('').join(result))

# print_vowels('Das is ein Test')



def odd_numbers(integers):
    for i in integers:
        if int(i) % 2 > 0:
            print(i)

def even_numbers(integers):
    for i in integers:
        if int(i) % 2 == 0:
            print(i)

def divisible_and_multiple(start, end, divisor=4, multiplicator=3):
    pos = start
    while pos <= end:
        if pos % 4 == 0 and pos % 3 == 0 :
            print(pos)
        pos += 1

# divisible_and_multiple(10, 100)

# odd_numbers('123456')
# even_numbers('1234567')

# print(ord('a'))


# print(98- ord('A'))

def square_of_sum(string):
    result = 0
    for char in string:
        result += int(char)
    return result ** 2

# print(square_of_sum('1239485838'))
# print(dir('directory'))

def filter_um(string):
    words = list(string.split(' '))
    return [word for word in words if word != "um"]

# print(filter_um('lak um um um sdflkj um alsdkjf l um um '))
# print(dir(list))

# Matches over all possible 
def match_lotto(given, match):
    if len(given) != len(match):
        return False
    for number in given:
        if number not in list(match):
            return False
    return True

# print(match_lotto('12346', '23451'))

def selectively_append(string, length=5):
    return [word for word in string.split(' ') if len(word) > 5]

# print(selectively_append('lakjsdlfkj asdlf lkjkkkkk lkj   lkj  l lkj  lkjlkj lkj lkj', 6))


def list_overlap(listA, listB):
    a = set(listA)
    b = set(listB)

    if len(a) > len(b):
        return [word for word in a if word in b]
    else:
        return [word for word in b if word in a]

# b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(list_overlap(a,b))



def is_palindrome(string):
    
    string = string.lower()
    for i in range(len(string)):
        print(string[i], string[-i-1])
        if string[i] != string[-i-1]:
            return False
    return True

# print(is_palindrome('Anna'))

def keep_even(numbers):
    return [number for number in numbers if number % 2 == 0]
# print(keep_even([1,2,3,4,5]))


# Rock Paper Scissors
import random
def rock_paper_scissors(rounds=3):
    wins = []
    actions = ['Rock', 'Paper', 'Scissors']
    while True:
        print('Round:', len(wins)+ 1)
        print('Whats your choice')
        player = input("-->")
        computer = actions[random.randint(0,2)]
        print('Computer chooses:', computer)
        
        # Generate a random gameplay
        if player == computer:
            pass
        elif player == 'Rock' and computer =='Scissors':
            wins.append(0)
        elif player == "Scissors" and computer == "Paper":
            wins.append(0)
        elif player == "Paper" and computer == "Rock":
            wins.append(0)
        else:
            wins.append(1)

        # Check if somebody already won
        if wins.count(0) == 3:
            print('Congratulations! You beat it!!')
            break
        elif wins.count(1) == 3:
            print('DAAAHHH! You sucked!')
            break

        print('You:', wins.count(0), 'Computer:', wins.count(1))

# rock_paper_scissors()

def guessing_game(rng=9):
    goal = random.randint(1,rng)
    count = 0
    while True:
        count += 1
        print('Take a guess')
        guess = int(input('-->'))
        if guess == goal:
            print('You got it!! It took you only', count, 'tries...')
            break
        elif guess < goal:
            print('Guess higher')
        else:
            print('Guess lower')


# guessing_game(1000)


def generate_password(length=5):
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    return "".join(random.sample(s, length))

print(generate_password(16))
# for i in range(49, 123):
#     print(chr(i))
