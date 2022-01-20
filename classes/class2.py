class Person:
    name = "Vinay"

    def __init__(self, name):
        self.name = name


def main():
    person1 = Person("I am person")
    print(person1.name)


main()
