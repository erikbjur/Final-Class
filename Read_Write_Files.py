names = ["Fred", "Bob", "Chuck"]

file = open('TestFile.txt', 'w')

try:
    for value in names:
        file.write(value + '\n')
finally:
    file.close()

# lets make a class to hold the person data in
class Person:
    def __init__(self, nameOfPerson) -> None:
        self.Name = nameOfPerson
    
    def PrintName(self) -> None:
        print(f"{self.Name} is my name!")

# now lets create a list of people from the list
listOfPeople = []

file = open('TestFile.txt', "r")

try:
    for line in file:
        # create a person with this name
        newPerson = Person(line.rstrip())
        # add them to the list of people
        listOfPeople.append(newPerson)
finally:
    file.close()

# now print off the names of the people in the list
for person in listOfPeople:
    person.PrintName()