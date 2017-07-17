def wordcount(string):
    print(len(string.split(' ')))

# wordcount('this is my first string')

import nltk
from nltk import TweetTokenizer
string = 'This is my test string, where i also put some ...'

# tokenizer = TweetTokenizer()


def mulitple_of(start, end):
    results =  [str(number) for number in range(start, end) if number % 7==0 and number % 5 > 0]
    return ','.join(results)

# print(mulitple_of(2000, 3200))


def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)

# print(factorial(8))


def mult_dict(n):
    return [{i:i**2} for i in range(1,n+1)]

# print(mult_dict(8))
def list_tuple(string):
    list_return = string.split(',')
    print (list_return)
    print(tuple(list_return))
# list_tuple('1,2,3,4,5')


def calculate(string):
    import math
    C = 50
    H = 30
    
    return [ int(math.sqrt((2*C*int(D))/ H)) for D in string.split(',')]

# print(calculate('100,150,180'))

def generate_array(string):
    # Generate the empty array
    rows, cols = (int(x) for x in string.split(','))
    array = [[0 for col in range(cols)] for row in range(rows)]
    
    # Fill the array
    for i in range(rows):
        for j in range(cols):
            array[i][j] = i * j    
    return array
    
# print(generate_array('3,5'))

def sort_words(string):
    words = string.split(',')
    return ','.join(sorted(words))

# print(sort_words('das, ist, ein, neuer, text'))


def capitalize_text():
    lines = []
    while True:
        s = input('Please enter your text below:\n')
        if s:
            lines.append(s.upper())
        else:
            break
    
    for line in lines:
        print(line)

# capitalize_text()


def sort_word_deduplicat(string):
    return " ".join(sorted(set(string.split(' '))))

# print(sort_word_deduplicat('Das ist ein Das ist ein'))


def div_by_5(string):
    return ','.join([x for x in string.split(',') if int(x) % 5 ==0])

# print(div_by_5('0100,0011,1010,1001'))

def all_even(start, end):
    results = []
    for number in range(start, end):
        even = True
        for i in str(number):
            if int(i) % 2 > 0:
                even = False

        if even == True:
            results.append(number)

    return results

# print(all_even(10000, 30000))
            
        
def count_letter_digits(string):
    digits = 0
    chars = 0
    for char in string:
        if char.isdigit():
            digits += 1
        elif isinstance(char, str):
            chars += 1
    
    print('LETTERS:', chars,'\n', "DIGITS:", digits)

# count_letter_digits('This is a text 12348987987')

def count_upper(string):
    result= {'upper': 0, 'lower':0}
    for char in string:
        if char.istitle():
            result['upper'] += 1
        if char.islower():
            result['lower'] += 1
    
    print('Upper Case:', result['upper'],'\n', 'Lower Case:', result['lower'])

# count_upper('lakjsd LKLKlkjl lksd')


def sum_it(number):
    calculation = 'a+aa+aaa+aaaa'.replace('a', str(number)).split('+')
    sum = 0
    for i in calculation:
        sum += int(i)
    return sum
    

# print(sum_it(9))

def square_odd(string):
    return ','.join([str(int(n)**2) for n in string.split(',') if int(n) %2 > 0 ])

# print(square_odd('1,2,3,4,5,6,7'))


def book_transactions():
    s = []
    balance = 0
    # Collect transactions
    while True:
        transaction = input('Input your transaction below:\n')
        if transaction:
            s.append(transaction)
        else:
            break
    
    # Read out the individual transactions
    for line in s:
        type, amount = line.split(' ')
        if type == 'D':
            balance += int(amount)
        else: 
            balance -= int(amount)

    print("Your Final Balance today is:", balance)
    return

# book_transactions()


def check_password(password):
    import re
    if len(password) < 6 or len(password) > 13:
        return False
    elif re.search('[a-z]', password) and re.search('[0-9]', password) and re.search('[A-Z]', password) and re.search('[$#@]', password):
        return True
    else:
        return False

# print(check_password('lllllAAA0$lkjlkjlkj'))

def sort_it():
    from operator import itemgetter
    entries = []
    while True:
        s = input('Please enter Name, Age and Height:\n')
        if s:
            name, age, height = s.split(',')
            entries.append((name, int(age), int(height)))
        else:
            break

    # Sort the Results
    print(sorted(entries, key=itemgetter(0,1,2)))
        
# sort_it()


def divisible_by(n,div=7):
    yield [ x for x in range(n) if x % div == 0]
    

# counter = divisible_by(2000000, 3)
# for i in counter:
#     print(i)


def robot_moves(n):
    import random

    actions = {
        'up': (0,-1),
        'down': (0,1),
        'left': (-1,0),
        'right': (1,0)
    }

    # Robot starting position
    position = (0,0)

    for i in range(n):
        move, value = random.choice(list(actions.items()))
        position = max(tuple([sum(x) for x in zip(position, value)]), (0,0))

        # Trace movement
        print('Robot moved ', move)
        print('Robot is at position', position)
    
    # Calculate Distance to Start
    print('Robot moved ', sum(position))

robot_moves(10)
        
    

