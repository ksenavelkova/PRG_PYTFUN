import datetime  # we will use this for date objects

# Person is a class defined in the global scope. It is a global variable.
class Person:
    # We define class attributes in the body of a class(TITLES)
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')
    # surname is a parameter passed into the __init__ method, and it is a local variable
    def __init__(self, title,name, surname, birthdate, address, telephone, email):
        # use the self variable to refer to an object inside
        self.title = title
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email
    # age is a method of the class Pearson
    def age(self):
        today = datetime.date.today()
        # age-local variable used  inside the scope of the age method.
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

#  person is an instance of the class Person,it is also global variable
person = Person(
    "Mrs"
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12),  # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)
# Wherever person is defined, we can use person.email, person.age()
# print(person.title)
# print(person.name)
# print(person.email)
print(Person().age())
