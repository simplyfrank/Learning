def wordfrequency(string):
    words = {}
    for word in string.split(' '):
        word = word.lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    return words

# string = "This is my teststring that i am working on. It has a teststring and i am working on it"

# word_count = wordfrequency(string)
# print(word_count)

def map_square(numbers):
    return map(lambda x: x**2, numbers)

# print(list(map_square([1,2,3,4,5,6])))

def map_square_even(numbers):
    evenNumbers =  map(lambda x: x**2, filter(lambda x: x%2 ==0, numbers))
    print(list(evenNumbers))

# map_square_even([1,2,3,4,5, 6, 8, 10])

def map_even_between(start, end):
    print(list(map(lambda x: x**2, filter(lambda x: x%2==0, range(start,end)))))

# map_even_between(1,20)


class American(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @staticmethod
    def printNationality():
        print('American')
    
    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)



class NewYorker(American):
    
    def __init__(self, *args, **kwargs):
        pass
    

# a = NewYorker('Frank', 23)
# a.getAge()
# a.getName()

import numpy as np
class Circle(object):

    def __init__(self,radius):
        self.radius = radius
        self.area = self.computeArea()
    
    def getArea(self):
        print(self.area)

    def computeArea(self):
        return self.radius **2 * np.pi


# c = Circle(5)
# c.getArea()


class Rectangle(object):

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = calculateArea()

    def calculateArea(self):
        return self.length * self.width


class Triangle(object):

    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.area = self.computeArea()

    def computeArea(self):
        return 0.5 * self.base * self.height

    def getArea(self):
        print(self.area)


# t = Triangle(5,15)
# t.getArea()



# break_calculation()

def extract_email(string):
    name, company = string.split('@')
    print(name)
    print(company.split('.')[0])

# extract_email('frank.fichtenmueller@outlook.com')


def extract_company(string):
    import re
    pat_comp = "(\w+\.)@(\w+)\.(com)"
    company = re.match(pat_comp, string)
    print(company)

# extract_company('frank.fichtenmueller@outlook.com')


string = "AABCAAADA"

def function(string):
    result = []
    part = round(len(string) / 3)
    subset_idx = 0
    for i in range(3):
        subset = string[subset_idx: subset_idx + part]
        subset_idx += part

        result.append("".join(sorted(set(subset))))

    for line in result:
        print(line)

# function(string)

print(set(enumerate(['a', 'b', 'c', 'd'])))
