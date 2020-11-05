# hash(object) returns the hash value of the object (if it has one)
# Hash values are integers
# They are used to quickly compare dictionary keys during a dictionary lookup
# Numeric values that compare equal have the same hash value even if they are of different types, as is the case for 1 and 1.0
# For objects with custom __hash__() methods, note that hash() truncates the return value based on the bit width of the host machine

# hash for integer unchanged
print('The hash for 1 is:', hash(1))

# hash for decimal
print('The hash for 1.0 is:',hash(1.0))
print('The hash for 3.14 is:',hash(3.14))

# hash for string
print('The hash for Python is:', hash('Python'))

# hash for a tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
print('The hash for a tuple of vowels is:', hash(vowels))

# hash for a custom object
class Person:
    def __init__(self, age, name):
        """
        Initialize a new age.

        Args:
            self: (todo): write your description
            age: (str): write your description
            name: (str): write your description
        """
        self.age = age
        self.name = name
    def __eq__(self, other):
        """
        Determine if other.

        Args:
            self: (todo): write your description
            other: (todo): write your description
        """
        return self.age == other.age and self.name == other.name
    def __hash__(self):
        """
        Returns the hash of the field

        Args:
            self: (todo): write your description
        """
        return hash((self.age, self.name))
person = Person(23, 'Adam')
print('The hash for an object of person is:', hash(person))
