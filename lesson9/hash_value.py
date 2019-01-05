# hash for integer unchanged
print('The hash for 181 is:', hash(181))

# hash for decimal
print('The hash for 181.23 is:',hash(181.23))

# hash for string
print('The hash for Python is:', hash('Python'))

# hash for tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
print('The hash for a tuple of vowels is:', hash(vowels))

# hash for custom object
class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name
    def __hash__(self):
        return hash((self.age, self.name))
person = Person(23, 'Adam')
print('The hash for an object of person is:', hash(person))
